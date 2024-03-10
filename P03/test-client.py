from Client0 import Client
IP = "127.0.0.1"  # your IP address
PORT = 8080
c = Client(IP, PORT)
print(c)
message = input("Enter command")
print("* Testing", message, "...")
response = c.talk(message)
print(f"Response: {response}")
