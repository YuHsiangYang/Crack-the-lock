import json
import numpy as np

valid_numbers = np.full((1, 4), 0)

for i in range(9999):
    numpy_original = np.array([int(i) for i in str(i)]) #Convert the number to a numpy array
    pad_array = np.pad(numpy_original, (4 - len(numpy_original), 0), 'constant', constant_values=(0, 0)) #Pad the array with zeros
    if len(np.unique(pad_array)) == 4: #If the array has four unique numbers
        valid_numbers = np.concatenate((valid_numbers, pad_array.reshape(1, 4)), axis=0)

with open('valid_numbers.json', 'w') as f:
    json.dump(valid_numbers[1:].tolist(), f)

print(valid_numbers)