from Client0 import Client
import termcolor
PRACTICE = 3
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"  # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
count = 0
while count < 5:
    message = input("Enter message")
    count += 1
    response = c.talk(message)
    print(f"To server:", termcolor.colored(message, "blue"))

    print("From server:" + termcolor.colored(f"{response}", "green"))
