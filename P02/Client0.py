import socket
class Client:
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT

    def ping(self):
        print("OK!")
    def __str__(self):
        print("Connection to SERVER at", self.IP, "PORT:", self.PORT)
