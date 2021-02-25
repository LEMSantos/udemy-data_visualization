import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

title = 'Scatterplot: gráfico de dispersão'
x_axis = 'Eixo X'
y_axis = 'Eixo Y'

plt.title(title)
plt.xlabel(x_axis)
plt.ylabel(y_axis)

plt.scatter(x, y, label='Meus pontos', color='r')
plt.plot(x, y)
plt.legend()

plt.show()
