import random
import os
clear = lambda: os.system('cls')


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

user_score = 0
computer_score = 0

while True:
    print("\n\nROCK PAPER SCİSSORS\n\nfor Rock => 1 \nfor Paper => 2 \nfor Scissors => 3\nfor Exit => 9\n\nWhich one?")
    user_choice = int(input())
    computer_choice = random.randint(1,3)
    clear()
    
    if user_choice not in [1,2,3,9]:
        print("Only 1, 2, 3 and 9 for exit. Try again")
        continue
    if user_choice == 9:
        break


    print("\n")
    print("User Choice:")
    if user_choice == 1:
        print(rock)
    elif user_choice == 2:
        print(paper)
    elif user_choice == 3:
        print(scissors)

    print("Computer Choice:")
    if computer_choice == 1:
        print(rock)
    elif computer_choice == 2:
        print(paper)
    elif computer_choice == 3:
        print(scissors)


    print("\n")
    if user_choice == 1 and computer_choice == 2:
        print("You lose!")
        computer_score+=1
    elif user_choice == 1 and computer_choice == 3 :
        print("You win!")
        user_score+=1
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
        user_score+=1
    elif user_choice == 2 and computer_choice == 3 :
        print("You lose!")
        computer_score+=1
    elif user_choice == 3 and computer_choice == 1:
        print("You lose!")
        computer_score+=1
    elif user_choice == 3 and computer_choice == 2 :
        print("You win!")
        user_score+=1
    elif computer_choice == user_choice:
        print("It's a draw")
    

    print(f"                                                        User Score: {user_score}")
    print(f"                                                        Computer Score: {computer_score}")
    
    continue
    








