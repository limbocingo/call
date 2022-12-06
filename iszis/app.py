from .base import BaseApplication
from .response import Response
from .request import Request
from .view import View

from sys import modules
import inspect

import datetime

"""
Main application.
"""


class Application(BaseApplication):
    """
    Create you'r server making an instance of 
    this class and execute `start`.

    Public variables of the class:
        - `page_not_found`: The not found page error.
        - `unknow_method`: If the method isn't registered will throw this error.
    """

    #: If the path requested doesn't exists
    #: will throw this message.
    page_not_found = {'error': 'Page not found!'}
    #: The method that was make the request
    #: isn't registered will return this.
    unknow_method = {'error': 'This method isn\'t registered.'}

    def __init__(self, module: str, address: str = '127.0.0.1', port: int = 8000) -> None:
        """
        Initilaizator of the main class
        :class:`Application`.
        """
        super().__init__(address, port)

        #: The module parameter is ussed for getting
        #: all the members of the file.
        self.module = module

    def response(self, request) -> bytes:
        receive: Request = Request(request)
        # Going class by class that is an inheritance of
        # :class:View, basicly is a view, get it and handle it.
        for _, view in inspect.getmembers(modules[self.module], inspect.isclass):
            if not issubclass(view, View):
                continue

            if not view.path:
                raise ValueError('None PATH gived for the view.')

            response = self.page_not_found, 404
            if view.path == receive.path:
                response: Response

                if receive.method == 'GET':
                    response = view.get(receive), 200

                elif receive.method == 'POST':
                    response = view.create(receive), 200

                elif receive.method == 'PATCH':
                    response = view.update(receive), 200

                elif receive.method == 'DELETE':
                    response = view.delete(receive), 200

                else:
                    response = self.unknow_method, 405        
        response = Response(response[0], response[1])

        print(
            f'[{datetime.datetime.now()}] "{receive.http[0]}"', response.status)
        return response.response()
