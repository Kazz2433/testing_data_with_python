import matplotlib.pyplot as plt

squares = [0, 15, 0, 15, 0, 15, 0, 15, 0, 7.5, 15]
input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
plt.plot(input_values, squares, linewidth=3)

# Define o titulo do grafico e nomeia os eixos
plt.title("Sqares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)
plt.axis([1, 30, 1, 31])
plt.tick_params(axis='both', labelsize=14)

plt.show()
