import Functions
import numpy as np

guess_number = Functions.guess_number()

initial_guess = guess_number.Generate_Number()
num_guess = 0
i = len(guess_number.valid_numbers_np)
while i > 1:
    print(f"guess: {initial_guess}")
    a = int(input("a: "))
    b = int(input("b: "))
    guess_number.Filter_Requirements(initial_guess, a, b)
    i = len(guess_number.filtered)
    initial_guess = guess_number.filtered[np.random.randint(0, i)]
    num_guess += 1
    
print(f"used {num_guess} times to get the answer")