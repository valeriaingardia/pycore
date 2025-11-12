import matplotlib.pyplot as plot
import numpy as np


x = np.linspace(0,45,900)
y = np.sin(x)



Figure1= plot.figure("Plotting...", figsize=(10,5))
axis = Figure1.add_subplot()

axis.plot(x,y,)

plot.draw()
plot.show()