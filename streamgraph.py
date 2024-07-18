import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
y1 = np.sin(x)
y2 = np.cos(x)

colors = ['#39FF14', '#000000']
#(#000000): code for black color
#(#39FF14): code for Neon Green color

plt.stackplot(x, y1, y2, baseline='wiggle', colors=colors)
plt.title('Streamgraph')
plt.show()
