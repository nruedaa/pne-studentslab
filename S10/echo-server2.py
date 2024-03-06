import socket
import termcolor


# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.139" # the IP address depends on the machine running the server

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
n = 1

# -- Waits for a client to connect
while True:
    (rs, address) = ls.accept()
    print(f"Waiting for Clients to connect")
    print("CONNECTION", n, f". Client IP, PORT:, {address}")
    n += 1
    msg = rs.recv(2048).decode("utf-8")
    print(f"Message received: " + termcolor.colored(msg,"green")) #esto es para que se imprima en verde por separado
    newMsg = "ECHO " + msg
    rs.send(newMsg.encode())
    rs.close()

# -- Close the socket
ls.close()
