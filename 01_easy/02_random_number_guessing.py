import random

# example 1
# r = random.randrange(1, 10) # does not include 10
# print(r)

# r = random.randint(1, 10) # includes number 10
# print(r)

# r = random.randint(10) # includes number 10
# print(r)

# example 2

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")


"""
Ideas for imporovement:
- Add guess limits 
- add game over message if guess limits are reach
"""


"""
my modified version
"""
# import random

# top_of_range = input("Type a number: ")

# if top_of_range.isdigit():
#     top_of_range = int(top_of_range)

#     if top_of_range <= 0:
#         print("Please type a number larger the 0 next time.")
#         quit()
# else:
#     print("Please type a number next time.")
#     quit()

# random_number = random.randint(0, top_of_range)


# guesses = 0

# while True:
#     guesses += 1
#     user_guess = input("Make a guess: ")
#     if user_guess.isdigit():
#         user_guess = int(user_guess)
#     else:
#         print("Please type a number next time.")
#         continue

#     if user_guess == random_number:
#         print("You got it!")
#         break
#     elif user_guess > random_number:
#         print("You were above the number!")
#     else:
#         print("You were below the number!")

# if guesses == 1:
#     print("You got it in", guesses, "guess.")
# elif guesses > 1:
#     print("You got it in", guesses, "guesses.")
