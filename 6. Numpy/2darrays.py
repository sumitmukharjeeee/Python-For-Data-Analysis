import numpy as np

np_height = np.array([1.73,1.68,1.71,80,33])
np_weight = np.array([65.4,1.68,58.72,80.6])

print(type(np_height))

print(type(np_weight))

# 2d

np_2d = np.array([[11,12,13,14],
                 [21,22,23,24]])

print(np_2d)

# SHows rows and colums here 2 rows and 3 columns
print(np_2d.shape)

import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)