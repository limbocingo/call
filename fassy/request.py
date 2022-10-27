from .base import BaseRequest

"""
Manager of the requests 
gived by the client.
"""


class Request:
    """
    Transform the raw HTTP request to an more
    easy to manage version. This is so useful for getting
    the HTTP data gived by the client.

    Public methods of the class:
        - `args`: The arguments gived in the URL.
        - `payload`: Data gived by the request.        
    """

    def __init__(self, response: BaseRequest) -> None:
        """
        Initializator of :class:`Request`.

        Variables of the intializator:
            - `response`: The current response gived by the client.
            - `http`: A splited verison of the HTTP request gived by the client.
            - `path`: Path where the HTTP request was made.
            - `method`: Method that was made the HTTP request.
            - `version`: Verion of the HTTP request.
        """

        #: The HTTP response gived by the client.
        #: And if uses for checking if the response needs
        #: to be decoded.
        self.response: bytes | str = response.receive
        if isinstance(self.response, bytes):
            self.response: str = response.receive.decode()

        #: A set of extracted information from the
        #: current response gived by the client.
        #:
        #: This will have very basic information,
        #: necessary for managing the requests gived by
        #: client.

        #: HTTP
        #: All the information gived by the client
        #: in the response splited in diferent parts.
        #:
        #: This information is raw and
        #: difficult to understand.
        self.http: list[str] = self.response.split('\r\n')

        #: PATH
        #: Current path where the request was
        #: maked by the client.
        self.path = ''
        for address in self.response.split()[1].split('/'):
            if address:
                self.path += '/' + address.split('?')[0]
        if not self.path:
            self.path = '/'

        #: METHOD
        #: Type of method gived by the client.
        self.method = self.http[0].split()[0]

        #: VERSION
        #: The version of HTTP that uses the
        #: web client that maked the request.
        #:
        #: The most supported is `HTTP/1.1`.
        #: If there is another version used the program
        #: can have bugs.
        self.version = self.http[0].split()[2]

    def args(self) -> list[dict[str, str]]:
        """
        Get all the parameters gived for every address.
        """
        parameters = []
        for address in self.http[0].split()[1].split('/'):
            if not address:
                continue
            parameters.append({})

            # split the address in two pieces, path and parameters,
            # for then split another time in every parameter.
            raw_parameters = address.split('?')[-1].split('&')
            for parameter in raw_parameters:
                if address.split('?').__len__() <= 1:
                    continue

                key, value = parameter.split('=')
                parameters[-1][key] = value

        return parameters

    def payload(self) -> dict:
        """
        JSON gived by the client in the HTTP request.
        """
        import json

        try:
            return json.loads(self.http[-1])
        except json.JSONDecodeError:
            return None
