# inputInt
def inputInt(some_number=None):
    try:
        some_number = int(input("Introduceti o cifra intreaga: "))
        if some_number > 0:
            return int(some_number)
        elif some_number < 0:
            return int(some_number)
    except:
        print("That's not a valid option!")
        exit()

sum_int_1 = inputInt()
sum_int_2 = inputInt()

print(sum_int_1 + sum_int_1)


# inputFloat
def inputFloat(some_float_number=None):
    try:
        some_float_number = float(input("Introduceti o cifra zecimala: "))
        if some_float_number > 0:
            return float(some_float_number)
        elif some_float_number < 0:
            return float(some_float_number)
    except:
        print("That's not a valid option!")
        exit()

sum_float_1 = inputFloat()
sum_float_2 = inputFloat()

print(sum_float_1 + sum_float_2)


# inputBoolean
def inputBoolean(value=True):
        value = input("Sunteti deacord, True sau False? ")

        if value == "True":
            return str(value)
        if value == "False":
            return str(value)
        else:
            print("Alegeti doar True sau False")
            exit()


a = inputBoolean()
b = inputBoolean()
print(a + " / " + b)
