#Question #3: I need some space"
import numpy as np
myarr = np.array(['python', 'is', 'cool!'])

def spaceBetween(arr):
    string1 = arr[0]
    string2 = arr[1]
    string3 = arr[2]

    for i in string1:
        string1=string1.replace(i,i+" ")

    for i in string2:
        string2=string2.replace(i,i+" ")

    for i in string3:
        string3=string3.replace(i,i+" ")
    
    newarr = np.array([string1, string2, string3])
    print(newarr)


spaceBetween(myarr)