from matplotlib import pyplot as plt
import numpy as np

dt = np.array([
          [0.05, 0.12],
          [0.13, 0.16],
          [0.19, 0.18],
          [0.24, 0.21],
          [0.27, 0.24],
          [0.29, 0.31],
          [0.32, 0.30],
          [0.36, 0.38],
          [0.37, 0.43],
          [0.40, 0.39],
          [0.07, 0.08],
          [0.02, 0.04],
          [0.15, 0.18],
          [0.39, 0.33],
          [0.43, 0.49],
          [0.44, 0.42],
          [0.47, 0.49],
          [0.50, 0.58],
          [0.53, 0.59],
          [0.57, 0.51],
          [0.58, 0.60]
])

x = dt[:, 0].reshape(dt.shape[0], 1)
X = np.append(x, np.ones((dt.shape[0], 1)), axis=1)
y = dt[:, 1].reshape(dt.shape[0], 1)

t = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

print(f'The parameters of the line: {t}')

y_line = X.dot(t)

plt.scatter(x, y)
plt.plot(x, y_line, 'r')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.show()

