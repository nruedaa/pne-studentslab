
import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")
print(data1)
# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1)  #data 1 está en formato json con los parentesis y corchetes etc,
                            #entonces esto lo hacemos para crear un objeto con la informacion que hemos recibido
                            #y la imprimimos para ver unicamente los valores, sin () ni []

print("CONTENT: ")
print("Total people in the database:", len(person["People"]))
for i, per in enumerate(person["People"]):
    termcolor.cprint("Name: ", 'green', end="")
    print(per['Firstname'], per['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(per['age'])
    phoneNumbers = per['phoneNumber']
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))
    for i, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')
        # The element num contains 2 fields: number and type
        termcolor.cprint("\t- Type: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dictnum['number'])