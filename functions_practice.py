for i in range(1,11):
    print(i)

foods =["Burger", "Pizza", "Salmon", "Pussy"]

for food in foods:
    print(f"I love, {food}!")

password = "python123"

guess = input("Enter password: ")

password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = input("Enter password: ")
    
    if guess == password:
        print("Access granted!")
        break
    else:
        attempts = attempts + 1
        remaining = max_attempts - attempts
        print(f"Wrong password. {remaining} attempts remaining.")

if attempts == max_attempts:
    print("Account locked. Too many failed attempts.")