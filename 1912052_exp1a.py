import numpy as np
inputs = np.array([
    [0,0], # both no
    [0,1], # one no, one yes
    [1,0], # one yes, one no
    [1,1]  # bot yes
])

print(f'input table:\n{inputs}')

W = np.array([1,1])

dot_products = inputs @ W
print(f'Dot products: {dot_products}')

#Returns the binary threshold output
def and_gate(dot, T):
    if dot > T:
        return 1
    else:
        return 0

T = int(input("Enter Threshold: "))
for i in range(0,4):
    activation = and_gate(dot_products[i], T)
    print(f'Activation: {activation}')