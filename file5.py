with open("example.txt", "w") as file:
    file.write("Hello, World!\n")

with open("example.txt", "r") as file:
    print(file.read())

with open("example.txt", "a") as file:
    file.write("making this a new line.\n")
