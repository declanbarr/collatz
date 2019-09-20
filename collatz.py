# Declan Barr 20/09/2019
# Program to show demonstrate the collatz conjecture

# Ask the user for a postive integer
n = int(input("Enter a positive integer"))

# Keep looping until 1 is reached
while n != 1:
    print(n)
    # Divide even numbers by 2
    if n % 2 == 0:
        n = int(n / 2)
    # Multiply odd numbers by 3 and add 1
    else:
        n = (3 * n) + 1
# Print the number 1 reached at the end
print(n)


