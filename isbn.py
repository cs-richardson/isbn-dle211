"""
This program will check if an ISBN given the user is real or fake.
Coded by Justin Le
"""

# Defines variables isbn (isbn-10 given by the user),
# valid_input (if the user's input is valid),
# and total (the total from the given isbn).
isbn = 0
valid_input = 0
total = 0

# Asks the user for 10-digit positive digits.
while valid_input == 0:
    try:
        isbn = str(input("Enter the ISBN: "))
        if int(isbn) < 0 or len(isbn) != 10:
            print("Invalid input.")
        else:
            valid_input = 1
    except ValueError:
        print("Invalid input.")

# Multiplies the 1st number by 1, the 2nd number by 2, the 3rd number by 3, etc.
# Results are then added to variable total, the sum of the multiplication.
for i in range(10):
    next = int(isbn[i]) * (i+1)
    total = total + next

# Checks if variable total, the sum, modular 11 equals 0. If it's true, it's a
# real ISBN. Otherwise, it's a fake ISBN.
if total % 11 == 0:
    print("Valid ISBN.")
else:
    print("Invalid ISBN.")
