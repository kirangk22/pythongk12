import numpy as np

n=[1,2,3,4]

na=np.array(n)

print(na*2) # doubling the values

# All other mathematical operations
# apply mathematical function ontop of each element in numpy array.
print(np.sin(n))
print(np.sin(na))

print(np.tan(na))
print(np.sin(na))
print(np.exp(na))

print(help(np.exp))