isbn = 0
valid_input = 0
total = 0

while valid_input == 0:
    try:
        isbn = str(input("Enter the ISBN: "))
        if int(isbn) < 0 or len(isbn) != 10:
            print("Invalid input.")
        else:
            valid_input = 1
    except ValueError:
        print("Invalid input.")

for i in range(10):
    next = int(isbn[i]) * (i+1)
    total = total + next

if total % 11 == 0:
    print("Valid ISBN.")
else:
    print("Invalid ISBN.")
