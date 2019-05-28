#@D plotting with matplotlib

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0,2.0,0.01)
s = 1+np.sin(2*np.pi*t)
plt.plot(t,s)

plt.xlabel('time(s)')
plt.ylabel('voltage(mV)')

plt.title('Sine wave')
plt.grid(True)
plt.savefig('sinewave.png')
plt.show()