import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science','notebook','grid'])

x = np.linspace(0,18,20)
y = np.sin(x) + 0.1 * np.random.randn(len(x))

plt.plot(x,y,'o--', color = 'green',lw=0.7)
plt.xlabel('Ascissa')
plt.ylabel('Ordinata')

plt.show()

