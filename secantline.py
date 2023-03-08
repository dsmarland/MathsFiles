import numpy as np
import matplotlib.pyplot as plt
x0 = 1
h = 0.000000001
x1 = x0+h
y1=(x0+h)**2
gradient = (y1-1)/(h)
print(gradient)
def f(x): 
    return x**2

def g(x):
    return gradient*x+1-gradient*1

# Define x data range for parabola
x = np.linspace(-5,5,100)

plt.plot(x, f(x))
plt.plot(x, g(x))
xpoints = np.array([1,x1])
ypoints = np.array([1,y1])
plt.plot(xpoints,ypoints, 'ro-')
plt.axis('equal')
plt.show()