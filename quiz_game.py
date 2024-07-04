print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
	quit()

print("Okay! lets play")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
	print("Correct!")
	score += 1
else:
    print("Incorrect!")	
    print("The correct answer is central processing unit")
    score -= 1

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
	print("Correct!")
	score += 1
else:
    print("Incorrect!")	
    print("The correct answer is random access memory")
    score -= 1

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
	print("Correct!")
	score += 1
else:
    print("Incorrect!")	
    print("The correct answer is graphics processing unit")
    score -= 1

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply":
	print("Correct!")
	score += 1
else:
    print("Incorrect!")	
    print("The correct answer is power supply")
    score -= 1    

print("Your final score is " + str(score))
print("Your final score is " + str((score/4) * 100) + "%.")












