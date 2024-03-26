import numpy as np
import matplotlib.pyplot as plt
theta = np.linspace(0, 2*np.pi, 100)
r = 2 * np.cos(1.5+theta)
plt.polar(theta, r, label='r = 2*cos(1.5+theta)',color='red')
plt.title('love for WHR')
plt.show()
