from .request import Request

"""
View base class.
"""


class View:
    """
    A base for creating a CRUD view, 
    you can use this for creating you'r views.

    Public variables of the class:
        - `path`: The address of the view.

    Public methods of the class:
        - `get`: Used commonly for getting information.
        - `post`: Adding new information.
        - `update`: Change the value of any data.
        - `delete`: Delete information.
    """
    #: The address of the view,
    #: and where the clients make
    #: the requests.
    path = None

    @staticmethod
    def get(
        request: Request) -> dict: return {'method': request.method}

    @staticmethod
    def post(
        request: Request) -> dict: return {'method': request.method}

    @staticmethod
    def update(
        request: Request) -> dict: return {'method': request.method}

    @staticmethod
    def delete(
        request: Request) -> dict: return {'method': request.method}
