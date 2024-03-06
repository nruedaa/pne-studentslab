import socket

# Configure the Server's IP and PORT
PORT = 8081
IP = "212.128.255.139" # the IP address depends on the machine running the server

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

# -- Waits for a client to connect
print("Waiting for Clients to connect")
while True:
    (rs, address) = ls.accept()
    print(f"Client {address}")
    msg = rs.recv(2048).decode("utf-8")
    print("The client says..." + msg)
    newMsg = "I'm a happy server\n"
    rs.send(newMsg.encode())
    rs.close()

# -- Close the socket
ls.close()

