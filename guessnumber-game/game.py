import socket
import random
class NumberGuesser:
    def __init__(self):
        PORT = 8080
        IP = "127.0.0.1"
        self.secret_number = random.randint(1,100)
        self.attempts = []
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((IP, PORT))
        serversocket.listen()
        while True:
            print("Waiting for player's number...")
            try:
                (clientsocket, address) = serversocket.accept()
            except socket.error:
                print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))
            except KeyboardInterrupt:
                print("Server stopped by the user")
                serversocket.close()
                exit()
            else:
                number = clientsocket.recv(2048).decode("utf-8")
                message = self.guess(number)
                response = message.encode()
                clientsocket.send(response)
                clientsocket.close()
    def guess(self, number):
        self.attempts.append(number)
        try:
            if self.secret_number == int(number):
                return f"You won after {len(self.attempts)} attempts"
            elif self.secret_number < int(number):
                return "Lower"
            elif self.secret_number > int(number):
                return "Higher"
        except ValueError:
            pass
c = NumberGuesser()