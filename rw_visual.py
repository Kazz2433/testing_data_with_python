import matplotlib.pyplot as plt
from random_walk import Random_Walk

while True:
    rw = Random_Walk(5000)
    rw.fill_walk()

    plt.figure(figsize=(10,6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values,rw.y_values,linewidth=3)

    plt.scatter(0,0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
    edgecolors='none', s=100)

    plt.show()

    keep_running = input("Quer continuar(y/n)")
    if keep_running == "n":
        break