from pathlib import Path
# -- Constant with the new of the file to open
FILENAME = "sequences/ADA.txt"
# -- Open and read the file
first_line = Path(FILENAME).read_text().find("\n")
body = Path(FILENAME).read_text()[first_line:]
body = body.replace("\n", "")
# -- Print the contents on the console
print(len(body))