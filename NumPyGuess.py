print("----------Welcome to NumPy Guess game----------\n")
print("1. You guess a number between 1 and 100\n")
print("2. I will tell you if your guess is too low, too high, or correct\n")

i = 100
j = 1
while True: 
    a = int(input(f"\nis your number greater than ({(i + j) // 2})? OR if ({(i + j) // 2}) correct ENTER 0 ? \nEnter 1 for yes\nEnter 2 for no : "))
    if a == 1:
        j = (i + j) // 2
    elif a == 2:
        i = (i + j) // 2
    elif a == 0:
        print(f"Your number is {(i + j) // 2}")
        break
    elif j >= i:
        print(f"Your number is {i}")
        break 
    else:
        print("Please enter a valid input (1 for yes/2 for no)")
    

print("Thanks for playing!")
