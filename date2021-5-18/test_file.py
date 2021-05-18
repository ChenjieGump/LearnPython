import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

filead = 'LES.txt'
b=np.loadtxt(filead, comments = 'x', dtype = np.float32)
#print(b)
x = b[:,0]
y1 = b[:,1]
y2 = b[:,2]
y3 = b[:,3]

# linear
H = np.ones((len(x),2),dtype=np.float32)
for i in range(len(x)):
    H[i,0] = x[i]
the_1 = np.dot(np.dot(np.mat(np.dot(H.T,H)).I,H.T),y1)
print(the_1[0,0],the_1[0,1])
yy_1 = the_1[0,0]*x + the_1[0,1]
plt.figure(1)
plt.plot(x,yy_1)
plt.plot(x,y1)
plt.legend()

# square
H = np.ones((len(x),3),dtype=np.float32)
for i in range(len(x)):
    H[i,0] = x[i]*x[i]
    H[i,1] = x[i]
the_2 = np.dot(np.dot(np.mat(np.dot(H.T,H)).I,H.T),y2)
print(the_2[0,0],the_2[0,1],the_2[0,2])
yy_2 = the_2[0,0]*x*x + the_2[0,1]*x + the_2[0,2]
plt.figure(2)
plt.plot(x,yy_2)
plt.plot(x,y2)

# cubic
H = np.ones((len(x),4),dtype=np.float32)
for i in range(len(x)):
    H[i,0] = x[i]*x[i]*x[i]
    H[i,1] = x[i]*x[i]
    H[i,2] = x[i]
the_3 = np.dot(np.dot(np.mat(np.dot(H.T,H)).I,H.T),y3)
print(the_3[0,0],the_3[0,1],the_3[0,2],the_3[0,3])
yy_3 = the_3[0,0]*x*x*x + the_3[0,1]*x*x + the_3[0,2]*x + the_3[0,3]
plt.figure(3)
plt.plot(x,yy_3)
plt.plot(x,y3)

plt.show(block = False)
plt.show()

