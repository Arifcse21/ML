import numpy as np
import matplotlib.pyplot as plt


sin90 = np.sin(90)
sin90rad = np.sin(90 * np.pi/180)

print(sin90)
cos90 = np.cos(90)
print(cos90)

x_sin = np.arange(0, 3*np.pi, 0.1)
print(x_sin)

y_sin = np.sin(x_sin)

plt.plot(x_sin, y_sin)

y_cos = np.cos(x_sin)

plt.plot(x_sin, y_cos, color='red')

x_tan = np.arange(0, 4*np.pi, 1.8)
y_tan = np.tan(x_tan)

plt.plot(x_tan, y_tan)
plt.show()


