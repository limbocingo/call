from .response import Response
from .request import Request
from .base import BaseServer
from .view import View

from sys import modules
import inspect

import datetime


class Application(BaseServer):
    """
    Create you'r server making an instance of 
    this class and execute `start`.

    Public variables of the class:
        - `page_not_found`: The not found page error.
        - `unknow_method`: If the method isn't registered will throw this error.
    """

    #: If the path requested doesn't exists
    #: will throw this message.
    page_not_found = Response({'error': 'Page not found!'}, 404)
    #: The method that was make the request
    #: isn't registered will return this.
    unknow_method = Response({'error': 'This method isn"t registered.'}, 422)

    def __init__(self, module: str, address: str = '127.0.0.1', port: int = 8000) -> None:
        """
        Initilaizator of the main class
        :class:`Application`.
        """

        super().__init__()

        #: Asign the address and the port
        #: where all the requests will be received
        #: and handled.
        self.address, self.port = address, port

        #: The module parameter is ussed for getting
        #: all the members of the file.
        self.module = module

    def response(self, request) -> bytes:
        receive: Request = Request(request)
        for name, view in inspect.getmembers(modules[self.module], inspect.isclass):
            if not issubclass(view, View):
                continue

            if not view.path:
                raise ValueError('None PATH gived for the view.')

            if view.path == receive.path:
                response: Response

                if receive.method == 'GET':
                    response = Response(
                        view.get(receive))

                elif receive.method == 'POST':
                    response = Response(
                        view.post(receive))

                elif receive.method == 'PATCH':
                    response = Response(
                        view.update(receive))

                elif receive.method == 'DELETE':
                    response = Response(
                        view.delete(receive))
                else:
                    response = self.unknow_method

                print(
                    f'[{datetime.datetime.now()}] "{receive.http[0]}"', response.status)
                return response.response()
        return self.page_not_found.response()
