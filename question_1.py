#Question #1: Hey Twin
import numpy as np
arr1 = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])
print(arr1)
for i in arr1:
    z = 0
    print(i)
    print(np.count_nonzero(i == i[0]))
    if np.count_nonzero(i == i[0]) == 3:
        arr1 = np.delete(arr1, i, axis=None)

print(arr1)