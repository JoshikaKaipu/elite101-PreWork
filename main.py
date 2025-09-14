print("Hello! Welcome to the Elite 101 Chatbot!")
name = input("What is your name? ")

print(f"Hello {name}, it's so nice to meet you!")

age = int(input("How old are you? "))

print(f"{age}! That's pretty cool, isn't it!")
print("How can I assist you today? ")

print("Options: ")
print("1. Option 1")
print("2. Option 2")
print("3. Option 3")
print("4. Exit the conversation")

userChoice = int(input("How would you like to continue?"))
if userChoice == 1:
    print("Perfect!")
elif userChoice == 2:
    print("Sounds good!")
elif userChoice == 3:
    print("Nice!")
elif userChoice == 4:
    print(f"Bye {name}! It was fun getting to know you!")
else:
    print("Sorry, please enter a valid input next time!")