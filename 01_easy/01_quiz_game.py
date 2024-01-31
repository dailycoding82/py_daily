"""
My Daily Python Coding Journey

Coding Skill Level: Beginner 

Game Name: QUIZ GAME

Room for Improvement: Improvement Notes at bottom of the code
"""

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play : )")
score = 0

answer = input("Spell the color 'red'? ")
if answer == "red":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

"""
IMPROVEMENT NOTES:
- Ask user their name, then assign scores to name at the end of the game  
- Try to improve this by adding the numbers of incorrect answers show the incorrect percentage as well

"""
