import numpy as np 
np.random.seed(12345)
a = np.random.randint(1,50, (4,5))
arr = np.sort(a, axis=0)
print(a)

print(arr)