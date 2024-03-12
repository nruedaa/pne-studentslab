from Client0 import Client
IP = "127.0.0.1"  # your IP address
PORT = 8080
c = Client(IP, PORT)
print(c)
# 1 TESTING PING
message = input("Enter message:")
print(f"* Testing {message} ...")
response = c.talk(message)
print(f"Response: {response}")
