import Functions
import numpy as np

guess_number = Functions.guess_number() #Create an instance of the class guess_number
answer = input("Enter the answer: ")

#Check if the answer has four numbers
while len(answer) != 4:
    answer = input("The answer should be exactly four digits, try again:")

#Convert the answer to a numpy array
answer_np = np.array([int(i) for i in answer])

#Run the while loop if a is less than 4, meaning the answer is not correct
a = 0
while a < 4:
    guess = input("Enter your guess: ")
    while len(guess) != 4:
        guess = input("The guess should be exactly four digits, try again:")
    #Check if the guess has four numbers
    guess_np = np.array([int(i) for i in guess])
    a, b = guess_number.Evaluate(guess_np, answer_np)
    print(f"a: {a}, b: {b}")