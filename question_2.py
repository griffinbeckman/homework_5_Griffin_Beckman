#Question #2: Checkers
import numpy as np
arr1 = []
arr2 = []

z = 0
x = 1

def create_initial_arr(arr, z):
    for i in range(8):
        if z == 0:
            arr .append(z)
            z += 1
        else:
            arr.append(z)
            z -= 1
    return arr

create_initial_arr(arr1, z)
print(arr1)

create_initial_arr(arr2, x)
print(arr2)

checkerboard = np.array([arr1, arr2, arr1, arr2, arr1, arr2, arr1, arr2])
print(checkerboard)