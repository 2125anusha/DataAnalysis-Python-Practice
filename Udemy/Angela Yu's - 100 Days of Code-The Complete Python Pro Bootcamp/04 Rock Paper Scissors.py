import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

total_choices=[rock,paper,scissors]
choice_names = ["rock", "paper", "scissors"]
computer_choice=random.randint(0,2)

user_choice=input("What do you choose? 0 for Rock, 1 for Paper and 2 for Scissors: ")
if user_choice!="0" and user_choice!="1" and user_choice!="2":
    print("Not a valid number, You Lose!")

else:
    user_choice = int(user_choice)
    print(f"You chose: {choice_names[user_choice]} \n {total_choices[user_choice]}")
    print(f"Computer chose: {choice_names[computer_choice]} \n {total_choices[computer_choice]}")

    if user_choice == computer_choice:
        print("Its a Draw")

    elif ((user_choice == 0 and computer_choice==2)
          or (user_choice == 1 and computer_choice==0)
          or (user_choice == 2 and computer_choice==1)):
        print("You Win !")
    else:
        print("The computer Wins")



