import numpy as np
import json

#The class for guessing numbers
class guess_number:
    def __init__(self):
        self.valid_numbers = np.full((1, 4), 0)
        self.filtered = np.full((1, 4), 0)
        #load valid_numbers.json
        with open('valid_numbers.json') as f:
            self.valid_numbers = json.load(f)
        self.valid_numbers_np = np.array(self.valid_numbers)
        
    def Generate_Number(self):
        # Generate an array with the numbers 0 to 9
        arr = np.arange(10)

        # Select four random elements from the array without replacement
        unique_numbers = np.random.choice(arr, size=4, replace=False)
        return unique_numbers
    
    #Evaluate the guess and return the feedback
    def Evaluate(self, guess:np.ndarray, answer:np.ndarray):
        a = 0
        b = 0
        #Check if the guess has four numbers
        #Prevent running into errors when the length of the guess is not four(4)
        if len(answer) == 4:
            for i in range(0, 4):
                if guess[i] == answer[i]:
                    a += 1
                elif guess[i] in answer:
                    b += 1
            return a, b
    
    #Narrow down the possbile answer by searching for the requirements based on the feedback
    def Filter_Requirements(self, guess: np.ndarray, a, b):
        #Check if self.filtered is an empty array
        if len(self.filtered) == 1:
            for number in self.valid_numbers_np:
                a_temp, b_temp = self.Evaluate(guess, number)
                if a_temp == a and b_temp == b:
                    self.filtered = np.concatenate((self.filtered, number.reshape(1, 4)), axis=0)
        #If self.filtered is not an empty array. I start by searching the numbers in the array to filter out the numbers that do not meet the requirements
        elif len(self.filtered) > 1:
            filtered_temp = np.full((1, 4), 0)
            for number in self.filtered:
                a_temp, b_temp = self.Evaluate(guess, number)
                if a_temp == a and b_temp == b:
                    filtered_temp = np.concatenate((filtered_temp, number.reshape(1, 4)), axis=0)
            self.filtered = filtered_temp[1:]
        print(f"filtered: \n{self.filtered}") #Print the filtered numbers
