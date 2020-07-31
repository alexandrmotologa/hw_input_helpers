def inputInt(message):
    my_nr = int(input(message))
    return int(my_nr)

a = inputInt("Enter the first integer number: ")
b = inputInt("Enter the second integer number: ")

print(a + b)


def inputFloat(message):
    my_nr = float(input(message))
    return float(my_nr)

c = inputFloat("Enter the first float number: ")
d = inputFloat("Enter the second float number:  ")

print(c + d)

#bool
def inputBoolean(message):
    value = bool(input(message))
    if value == 1:
        return "True"
    if value == 0:
        return "False"

e = inputBoolean("Enter 1 == True or 0 == False: ")
f = inputBoolean("Enter 1 == True or 0 == False: ")

print (e + " / " + f )
