import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)
# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'
# Print the information on the console, in colors
print()
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

