import numpy as np
import matplotlib.pyplot as plt
## Softmax function:
def softmax(arr):
    return np.exp(arr) / np.sum(np.exp(arr), axis=0)

## Hardlimit function:
def hardlim(arr):
    return (arr > 0) * 1.0

## Linear Transfer Function
def pureline(arr):
    return arr

## Saturating Linear Transfer Function
def satlin(arr):
    res = []
    for i in x:
        if(i<=0):
            res.append(0)
        elif 0<i and  i<=1:
            res.append(i)
        else:
            res.append(1)
    return res

## Hyperbolic Tangent Sigmoid Transfer Function
def hypTanSig(arr):
    numerator = np.exp(x) - np.exp(-x)
    denominator = np.exp(x) + np.exp(-x)

    return numerator/denominator
x = np.linspace(-10, 10)
plt.plot(x, softmax(x))
plt.title('Activation Function : Softmax')
plt.show()

x = np.linspace(-10, 10)
plt.plot(x, hardlim(x))
plt.title('Hardlimit function')
plt.show()

x = np.linspace(-10, 10)
plt.plot(x, pureline(x))
plt.title('Linear Transfer Function')
plt.show()

x = np.linspace(-10, 10)
plt.plot(x, satlin(x))
plt.title('Saturating Linear Transfer Function')
plt.show()

x = np.linspace(-10, 10)
plt.plot(x, hypTanSig(x))
plt.title('Hyperbolic Tangent Sigmoid Transfer Function')
plt.show()
