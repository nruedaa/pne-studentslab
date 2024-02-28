import socket
class Client:
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT

    def ping(self):
        print("OK!")
    def __str__(self):
        return "Connection to SERVER at " + self.IP + " PORT: " + str(self.PORT)
    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.IP, self.PORT))

        # Send data.
        s.send(str.encode(msg))

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return response

