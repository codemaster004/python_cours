corect_password = "python1234"
name = input("Enter your name: ")
password = input("Enter password: ")

while corect_password != password:
    password = input("Wrong password. Try again: ")
print("Hi %s you are logged in" % name)
