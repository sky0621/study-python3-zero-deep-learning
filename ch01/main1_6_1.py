import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1) # 0から6まで0.1刻みで生成
print(x)
print(" ")

y = np.sin(x)
print(y)
print(" ")

plt.plot(x, y)
plt.show()
