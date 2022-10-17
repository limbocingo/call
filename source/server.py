from socket import socket


class Server(socket):
    
    """
    A inheritance of the base class socket and simplified to make it more easy to manage.
    The better way that you can inheritance :class:`Server`::
        
        from fassy.server import Server
        
        class Handler(Server):
            
            def __init__(self):
                super().__init__('127.0.0.1', 8000)

            def request(self, petition: tuple[socket.socket, tuple[str, int]]):
                client, address = petition
                client.send("hello world")
    If you don't understand this example you can watch the documentation.
    
    ### Methods\n
    :method `start`: Start the socket server at the port gived.\n
    :method `request`: The handler of the requests. you can rewrite.
    
    ### Arguments\n
    :arg `address`: The IP of the socket server.\n
    :arg `port`: Port where the requests will be gived.
    """
    
    def __init__(self, address: str, port: int) -> None:
        #: Initialize socket class
        super().__init__()
        #: and bind the current socket to the
        #: gived address.
        self.bind((address, port))
        
        #: Status, you can change this var to false
        #: if you want to close the socket.
        self.status = True

    def request(self, petition: tuple[socket, tuple[str, int]], receive: bytes) -> None:
        """
        Handler for the requests.
        """
        
        client, address = petition
        client.send(b'default')

    def stop(self, key: str) -> None:
        """
        Wait for a keyboard response and if is equal to the key selected
        will close the server.
        """
        import keyboard
        
        while self.status:
            #: Checking in a loop if the key selected
            #: is pressed.
            if keyboard.is_pressed(key):
                self.status = False
        self.close()    

    def start(self) -> None:
        """
        Open a socket server to the port gived and handle the requests gived to that port. 
        """
        #: Start listening to the requests gived.
        self.listen()
        
        #: This will be executed in the background
        #: and waiting for selected key to close
        #: the socket server.
        import threading
        threading.Thread(target = self.stop, args=['Q']).start()
        
        #: Make this first accept for handle 2 requests
        #: at the same time.
        try:
            petition, address = self.accept()
            
            #: Handle the request and
            #: close it.
            self.request((petition, address), petition.recv(16384))
            petition.close()
        
        except OSError as socket_error:
            #: If there happens any error will raise it,
            #: but if the error is equal to 10038 (the error
            #: that throws when the socket server is close) will
            #: ignore it.
            if not socket_error.winerror == 10038:
                raise socket_error
        
        #: Accept requests and handle it.
        while self.status:
            #: Get the information of the
            #: request maked.
            try: 
                petition, address = self.accept()
            
                self.request((petition, address), petition.recv(16384))
                petition.close()
                
            except OSError as socket_error:
                if not socket_error.winerror == 10038:
                    raise socket_error
        
class Handler(Server):
    
    def __init__(self):
        super().__init__('127.0.0.1', 8000)
        
    def request(self, petition: tuple[socket, tuple[str, int]], receive: bytes):
        client, address = petition
        client.send(b"hello world")
        
Handler().start()