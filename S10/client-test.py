from Client0 import Client
PRACTICE = 3
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.198"  # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
count = 0
while count < 5:
    message = input("Enter message")
    count += 1
    print(c)
    print("Sending a message to the server...")
    response = c.talk(message)
    print(f"Response: {response}")
