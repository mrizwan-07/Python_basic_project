
# value error handeling
 
def get_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("invalid input! enter a number")


# 1. calculator

def calcuator():
    x = get_int("Enter a first number : ")
    y = get_int("enter a second number : ")

    print(" 1. Add(+) \n 2. Sub(-) \n 3. Mul(*) \n 4. Div(/)")


    sel = get_int("Enter a number of operator : ")

    if sel == 1:
        ans = x + y
        print("x + y : ", ans)
    elif sel == 2:
        ans = x - y
        print("x - y : ", ans)
    elif sel == 3:
        ans = x * y
        print("x * y : ", ans)
    else:
        ans = x / y
        print("x / y : ", ans)




# 2. number guessing game 

import random

def numberGuessingGame():
    number = random.randint(1,10)

    guess = get_int("Guess a number between 1 to 10 : ")

    if guess == number:
        print("You choose a correct number!")
    else :
        print("your number is :",guess,"and the correct number is :",number)




# 3. stone paper scissor game 

import random

def stonePaperScissor():
    choices = ["stone","paper","scissor"]
    com = random.choice(choices)

    user = input("Enter you choise [stone , paper , scissor] : ").lower()

    if user not in choices:
        print("Invalid choise Enter a correct choise ")
    elif com == user:
        print("Match tie!")
    elif (
        (user == "paper" and com == "stone")
        or (user == "stone" and com == "scissor")
        or (user == "scissor" and com == "paper") 
    ):
        print(f"your choise is {user} and computer choise is {com} you won!")
    else:
        print(f"your choise is {user} and computer cjoise is {com} , you loose! try again")




# 4. to-do list 

def toDo_list():
    tasks = []

    while True:
        print(" These are the tasks select any one \n 1.Add Task \n 2.view task \n 3.Exit")

        choice = get_int("Enter a number to perform task : ")
        
        if choice == 1:
            task = input("Enter a task : ")
            tasks.append(task)
            print("successfully added.")
        elif choice == 2:
            for i,task in enumerate(tasks, start = 1):
                print(i,task)
            if not tasks:
                print("NO task available")
        elif choice == 3:
            break
        else:
            print("Invaid choice")



# 5. digital clocker

import tkinter as tk
import time

def digital_clocker():
    root = tk.Tk()
    root.title("Digital Clock")

    label = tk.Label(root, font=("arial",230),background="gray")
    label.pack(padx=20,pady=20)


    def update_clock():
        current_time = time.strftime("%H:%M:%S")
        label.config(text=current_time)
        root.after(1000,update_clock)

    update_clock()
    root.mainloop()


# 6. expence tracker

def expence_tracker():
    
    expences = []

    while True:
        print("\n 1. Add Expences ")
        print("\n 2. View Expences ")
        print("\n 3. total Expences ")
        print("\n 4. Exit \n")

        choice = get_int("Enter your choice number : " )

        if choice == 1:
            name = input("Enter expence Name :")
            amount = get_int("Enter expence amount :")
            expences.append((name,amount))

        elif choice == 2:
            for name,amount in expences:
                print(name,amount)

        elif choice == 3:
            total = sum(amount for name , amount in expences)
            print("total expence is ",total)
        elif choice == 4:
            break
        else:
            print("invaid choice")






