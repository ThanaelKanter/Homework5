import numpy as np 
ray = np.array([[4,4,4],[6,9,3], [4,7,2]])
equal = np.all(ray[:, 1:] == ray[:, :-1], axis=1)
equal_rows = np.where(equal)[0]
print(ray[equal_rows])