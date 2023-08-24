#hello name
custom = []
def inputname(round):
    for index in range(round):
        custom.append(input("Name of user" + str(index) + " : "))

def helloUser():
    for data in custom:
        print("hello", data)

input_User = int(input())
inputname(input_User)
helloUser()