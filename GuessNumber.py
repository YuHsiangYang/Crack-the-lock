import Functions
import numpy as np

# ar = np.full((4, 7), 0)
# print(ar)



guess_number = Functions.guess_number()

# guess = np.array([1, 2, 7, 0])
# guess_number.Filter_Requirements(np.array([1, 3, 4, 8]), 0, 0)
# print(f"length: {len(guess_number.filtered)}")
# print(f"filtered: {guess_number.filtered}")
# guess_number.Filter_Requirements(np.array([7, 4, 3, 9]), 0, 1)
# print(f"length: {len(guess_number.filtered)}")
# print(f"filtered: {guess_number.filtered}")
# guess_number.Filter_Requirements(np.array([2, 9, 8, 0]), 2, 0)
# print(f"length: {len(guess_number.filtered)}")
# print(f"filtered: {guess_number.filtered}")
# for i in guess_number.filtered:
#     print(i)

initial_guess = guess_number.Generate_Number()
# print(guess_number.Generate_Number())
i = len(guess_number.valid_numbers_np)
while i > 1:
    print(f"guess: {initial_guess}")
    a = int(input("a: "))
    b = int(input("b: "))
    guess_number.Filter_Requirements(initial_guess, a, b)
    i = len(guess_number.filtered)
    initial_guess = guess_number.filtered[np.random.randint(0, i)]

# # # print(guess_number.valid_numbers)
