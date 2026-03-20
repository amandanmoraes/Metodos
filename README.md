import numpy as np
import math 
import matplotlib.pyplot as plt



gm = 9.81
cd= 0.25 
t = 4
v= 36

#(a= inicio do intervalo,b= final do intervalo,x= numero de termos)#
m = np.linspace (100,200,100)
def bang_jump(m):
    return np.sqrt((gm/cd)) * np.tanh
(np.sqrt(((gm * cd/m)) * t))


plt.figure()
plt.plot(m, bang_jump(m),'or', label = "$e^x$")
plt.legend()
plt.xlabel(cd)
plt.ylabel(bang_jump(m))
plt.grid()
plt.show()
