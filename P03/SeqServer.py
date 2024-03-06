import socket
import termcolor
class Server:
    def __init__(self):
        PORT = 8082
        IP = "127.0.0.1"
        MAX_OPEN_REQUESTS = 5
        number_con = 0
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            serversocket.bind((IP, PORT))
            serversocket.listen(MAX_OPEN_REQUESTS)
            print("SEQ server configured")
            while True:
                print("Waiting for clients...")
                (clientsocket, address) = serversocket.accept()
                number_con += 1
                msg = clientsocket.recv(2048).decode("utf-8")
                message = self.execute_response(str(msg)) + "\n"
                send_bytes = str.encode(message)
                clientsocket.send(send_bytes)
                clientsocket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()

    def execute_response(self, msg):
        if msg.startswith("PING"):
            return self.ping_response()
    def ping_response(self):
        termcolor.cprint("PING command", "green")
        print("OK!")
        return "OK\n"
c = Server()