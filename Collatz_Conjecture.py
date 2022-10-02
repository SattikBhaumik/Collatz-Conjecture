import matplotlib.pyplot as plt
import numpy as np
c=0
a=[]
b=[]
x=input('Enter the initial number:')
x=float(x)
while(x!=1):
  if(x%2==0):
    x=x/2
    a.append(x)
    c=c+1

  elif(x%2!=0):
    x=3*x+1
    a.append(x)
    c=c+1
for i in range(len(a)):
  b.append(i)
print(a)
print(b)
print('Iterations:',c)
xpoints=np.array([b])
ypoints=np.array([a])
plt.ylabel('Output value')
plt.xlabel('Input value')
plt.scatter(xpoints, ypoints)
plt.show()