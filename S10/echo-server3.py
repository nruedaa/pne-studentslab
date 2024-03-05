import socket
import termcolor


# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.89" # the IP address depends on the machine running the server

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
n = 1
client_list = []
# -- Waits for a client to connect
while n <= 5:
    (rs, address) = ls.accept()
    print(f"Waiting for Clients to connect")
    print("CONNECTION", n, f". Client IP, PORT:, {address}")
    client_list.append(f"{address}")
    n += 1
    msg = rs.recv(2048).decode("utf-8")
    print(f"Message received: " + termcolor.colored(msg,"green")) #esto es para que se imprima en verde por separado
    newMsg = "ECHO " + msg
    rs.send(newMsg.encode())
    rs.close()
clients_dic = {"Client 0:": "",
               "Client 1:": "",
               "Client 2:": "",
               "Client 3:": "",
               "Client 4:": "",
               }
for i in client_list:
    print(i)
    clients_dic["Client 0:"] += i[0]
    clients_dic["Client 1:"] += i[1]
    clients_dic["Client 2:"] += i[2]
    clients_dic["Client 3:"] += i[3]
    clients_dic["Client 4:"] += i[4]

print("The following clients have connected to the server:", "\n", clients_dic)
# -- Close the socket
ls.close()
