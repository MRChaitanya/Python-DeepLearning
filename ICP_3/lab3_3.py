import numpy as np

x = np.random.randint(1, 20, 15)
print(x)

y = x.reshape(3, 5)
print(y)

max_value = np.amax(y, axis=1)
print(max_value)

y = np.where(y==np.max(y,axis=1).reshape(-1,1), 0, y)
print(y)