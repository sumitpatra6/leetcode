number = 0.72
binary_rep = ""
counter = 0
while True:
    number = number * 2
    binary_rep += str(int(number))
    if number == 1:
        break
    counter += 1
    if counter > 32:
        binary_rep = "ERROR"
        break
    if number > 1:
        number = number - 1

print(binary_rep)