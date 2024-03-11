from Client0 import Client
IP = "127.0.0.1"  # your IP address
PORT = 8080
c = Client(IP, PORT)
print(c)
# 1 TESTING PING
message = "PING"
print(f"* Testing {message} ...")
response = c.talk(message)
print(f"Response: {response}")

# 2 TESTING GET0
message = "GET0"
print(f"* Testing {message} ...")
response = c.talk(message)
print(f"Response: {response}")


# 3 TESTING INFO
message = "INFO AACCGGTT"
print(f"* Testing {message} ...")
response = c.talk(message)
print(f"Response: {response}")


# 4 TESTING COMP
message = "COMP ACGTTGACT"
print(f"* Testing {message} ...")
response = c.talk(message)
print(f"Response: {response}")


# 5 TESTING REV
message = "REV AGCTGTACGT"
print(f"* Testing {message} ...")
response = c.talk(message)
print(f"Response: {response}")


# 6 TESTING GENE U5
message = "GENE U5"
print(f"* Testing {message} ...")
response = c.talk(message)
print(f"Response: {response}")


# 6 TESTING GENE ADA
message = "GENE ADA"
print(f"* Testing {message} ...")
response = c.talk(message)
print(f"Response: {response}")


# 6 TESTING GENE FRAT1
message = "GENE FRAT1"
print(f"* Testing {message} ...")
response = c.talk(message)
print(f"Response: {response}")


# 6 TESTING GENE FXN
message = "GENE FXN"
print(f"* Testing {message} ...")
response = c.talk(message)
print(f"Response: {response}")


# 6 TESTING GENE RNU6_269P
message = "GENE RNU6_269P"
print(f"* Testing {message} ...")
response = c.talk(message)
print(f"Response: {response}")