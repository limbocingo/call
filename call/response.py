from http import HTTPStatus
from json import dumps
from sys import version


class Response:
    """
    Takes you'r `JSON` and trasform it to an 
    HTTP readeable bytes object.

    Parameters of the class:
        - `json`: JSON value of the return.
        - `status`: The status that will be receveied. 
    """

    def __init__(self, json: list | dict, status: int = 200) -> None:
        """
        Transform you'r JSON to an HTTP
        readeble encoded text.
        """
        self.json = json
        self.status = status

    def response(self):
        """
        The encoded and formated HTTP text.
        """
        return f'''HTTP/1.1 {self.status} {HTTPStatus(self.status).phrase}\r
HTTP-Version: HTTP/1.1\r
Server: Cast/0.0.1 Python/{version}\r
Accept: application/json\r
Content-Type: application/json\r
Content-Lenght: {len(self.json) if self.json else 0}\r

{dumps(self.json) if self.json else "null"}'''.encode()
