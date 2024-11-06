import numpy as nm
import matplotlib.pyplot as plt

def convolution(x,h):
    l1 = len(x)
    l2 = len(h)
    y = nm.zeros(l1+l2-1)

    for n in range(l1+l2-1):
        for k in range(l1):
            if n-k>=0 and n-k<l2:
                y[n] += x[k]*h[n-k]
    return y

h = [1,2,1,-1]
x = [1,2,1,-1]

#convolution
y = convolution(x,h)

#correlation
R_xy = convolution(x,h[::-1]) 

plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.stem(x,'b')
plt.xlabel('n')
plt.ylabel('amplitute')
plt.title('x(n)')

plt.subplot(2,2,2)
plt.stem(h,'c')
plt.xlabel('n')
plt.ylabel('amplitute')
plt.title('h(n)')

plt.subplot(2,2,3)
plt.stem(y,'y')
plt.xlabel('n')
plt.ylabel('amplitute')
plt.title('y(n) = x(n)*h(n)')

plt.subplot(2,2,4)
plt.stem(R_xy,'y')
plt.xlabel('l')
plt.ylabel('y(l)=x(n).h(n)')
plt.title('Correlation')
plt.show()