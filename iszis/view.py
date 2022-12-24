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

    def __init__(self, request: Request, path: str = None) -> None:
        #: The address of the view, and where the
        #: clients make the requests.
        self.path = path

        #: Basic information of the request
        #: gived at the server.
        self.request = request

    #: Basic CRUD (create, remove, update, delete).
    def get(self) -> dict: return {'message': 'default-message'}

    def create(self) -> dict: return {'message': 'default-message'}

    def update(self) -> dict: return {'message': 'default-message'}

    def delete(self) -> dict: return {'message': 'default-message'}
