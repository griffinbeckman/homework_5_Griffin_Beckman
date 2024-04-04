#Question #4: Everything is in order
import numpy as np
np.random.seed(12345)
a = np.random.randint(1,50,(4,5))
print(a)
b = a[0]
c = a[1]
d = a[2]
e = a[3]

column_1 = [b[0] , c[0] , d[0] , e[0]]
column_2 = [b[1] , c[1] , d[1] , e[1]]
column_3 = [b[2] , c[2] , d[2] , e[2]]
column_4 = [b[3] , c[3] , d[3] , e[3]]
column_5 = [b[4] , c[4] , d[4] , e[4]]

column_1.sort()
column_2.sort()
column_3.sort()
column_4.sort()
column_5.sort()

print(column_1)

b_new = [column_1[0], column_2[0], column_3[0], column_4[0], column_5[0]] 
c_new = [column_1[1], column_2[1], column_3[1], column_4[1], column_5[1]]
d_new = [column_1[2], column_2[2], column_3[2], column_4[2], column_5[2]]
e_new = [column_1[3], column_2[3], column_3[3], column_4[3], column_5[3]]

a_new = np.array([b_new, c_new, d_new, e_new])
print(a_new)