number = input("Please enter your number: ")

letter = 0
for i in number:
    if i in "abcdefghijklmnopqrstuvwxyz":
        letter += 1
    else:
        pass

if letter != 0:
    print("Do not use any entries other than numeric values")

elif ("." or "," or "+" or "-") in number:
    print("Please enter an integer number")

elif int(number) < 0:
    print(" Please enter a positive number")

elif int(number) >= 0:
    total = 0
    for i in number:
        total += int(i)**int(len(number))
    if total == int(number):
        print("{} is an Armstrong number".format(number))
    else:
        print("{} is not an Armstrong number".format(number))
