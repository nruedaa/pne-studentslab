from Client0 import Client
IP = "127.0.0.1"  # your IP address
PORT = 8080
c = Client(IP, PORT)
correct = True
while correct:
    number = input("Enter number")
    print(f"* Number: {number} ...")
    response = c.talk(number)
    print(f"Game says: {response}")
    if response.startswith("You won"):
        correct = False
