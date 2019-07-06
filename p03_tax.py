num = input("Please enter your amount:\n>> ")
while True:
    try:
        if float(num) < 0:
            raise ValueError
        else:
            break
    except ValueError:
        num = input("Number is incorrect, try again.\n>> ")
ra = input("Please enter tax rate:\n>> ")
while True:
    try:
        if 1 < int(ra) < 99:
            break
        else:
            raise ValueError
    except ValueError:
        ra = input("Rate is incorrect, try again.\n>> ")
print("===== "*4)
print(f"AMOUNT: ${num}")
print(f"RATE: ${ra}")
print("===== "*4)
print("TAX: " + str('{:.2f}'.format(float(num)*int(ra)/100)) + "$")
print("NET: " + str('{:.2f}'.format(float(num)-float(num)*int(ra)/100)) + "$")
print("===== "*4)
