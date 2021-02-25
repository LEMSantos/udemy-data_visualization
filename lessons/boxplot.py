import matplotlib.pyplot as plt
import random

x = [random.randint(0, 100) for i in range(10000)]

plt.boxplot(x)
plt.title('Boxplot')

plt.show()
