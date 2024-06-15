print("Hello Guys Wellcome To The Quizzzz Game....!!!!")

player = input("Do you want to play the game (yes/no) :")

if player.lower() == "yes":
    print("lets Start The game...")
else:
    quit()
score=0

qustion = input("How many legs does a spider have? :")

if qustion.lower() == "eight":
        print("Your correct")
        score=score+1
else:
        print("Your Wrong")

qustion = input(" What's the name of a place you go to see lots of animals? :")

if qustion.lower() == "zoo":
        print("Your correct")
        score = score + 1
else:
        print("Your Wrong")

qustion = input(" If you freeze water, what do you get? :")

if qustion.lower() == "ice":
        print("Your correct")
        score = score + 1
else:
        print("Your Wrong")

qustion = input("What colors are the stars on the American flag? :")

if qustion.lower() == "white":
        print("Your correct")
        score = score + 1
else:
        print("Your Wrong")

qustion = input("Which planet is known as the 'Blue Planet'? :")

if qustion.lower() == "earth":
        print("Your correct")
        score = score + 1
else:
        print("Your Wrong")

qustion = input("Which is the largest planet in the solar system? :")

if qustion.lower() == "jupiter":
        print("Your correct")
        score = score + 1
else:
        print("Your Wrong")

qustion = input("How many Olympic rings are there? :")

if qustion.lower() == "five":
        print("Your correct")
        score = score + 1
else:
        print("Your Wrong")

qustion = input("How many chambers are there in the human heart? :")

if qustion.lower() == "four":
        print("Your correct")
        score = score + 1
else:
        print("Your Wrong")

qustion = input(" Name the coldest place in the world ? :")

if qustion.lower() == "antarctica":
        print("Your correct")
        score = score + 1
else:
        print("Your Wrong")

qustion = input("Do you know the creater of the project ? :")

if qustion.lower() == "manoj":
        print("Your correct")
        score = score + 1
else:
        print("Your Wrong")

print("Your Total Score Is :"+str(score))

print("Thanks For Playing")