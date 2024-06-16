import random

user=0
computer=0

options=["rock","paper","scissor"]

while True:

    user_type = input(" Type Rock/Paper/Scissor or Exit :")

    if user_type=="exit":
        quit()
    if user_type not in options:
        continue

    random_num= random.randint(0,2)

    computer_type = options[random_num]

    print("Computer Types :",computer_type)

    if user_type == "rock" and computer_type=="scissor":
        print("You Won")
        user=user+1

    elif user_type == "paper" and computer_type == "rock":
            print("You Won")
            user = user + 1

    elif user_type == "scissor" and computer_type == "paper":
                print("You Won")
                user = user + 1

    elif user_type == "scissor" and computer_type == "scissor":
                print("Ones More Please...")

    elif user_type == "paper" and computer_type == "paper":
                print("Ones More Please...")

    elif user_type == "rock" and computer_type == "rock":
                print("Ones More Please...")

    else:
        print("You Lost")
        computer = computer+1

    print("Your Score :",user)
    print("Computer Score :",computer)