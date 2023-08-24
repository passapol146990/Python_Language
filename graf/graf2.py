from cProfile import label
import matplotlib.pyplot as plt,numpy as np
a = np.random.random(10)
b = np.random.random(10)

plt.title('passapol')
plt.plot(a,label='A')
plt.plot(b,label='B')
plt.legend()
plt.xlabel('NumberA')
plt.ylabel('NumberB')
plt.show()