import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

title = 'Gráfico de barras'
x_axis = 'Eixo X'
y_axis = 'Eixo Y'

plt.title(title)
plt.xlabel(x_axis)
plt.ylabel(y_axis)

plt.bar(x, y)
plt.show()
