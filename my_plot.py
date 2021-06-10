import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plot():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

    ani = FuncAnimation(fig, lambda *args: animate(ax1=ax1, ax2=ax2, ax3=ax3, ax4=ax4, *args), interval=1000)

    # print(plt.style.available)
    plt.style.use('bmh')

    plt.show()


def animate(i, ax1, ax2, ax3, ax4):
    data = pd.read_csv('../data/plots_data.csv')
    x = data['sim_time']
    occupation = data['occupation_value']
    current_working = data['current_working_value']
    warehouse_empty_number = data['warehouse_empty_number']
    warehouse_idle_number = data['warehouse_idle_number']
    deliveries_number = data['deliveries_number']
    orders_number = data['orders_number']

    ax1.cla()
    ax1.set_ylim(ymax=101, ymin=-1)
    ax1.set_xlabel('Czas [min]')
    ax1.set_title('Procentowe zapełnienie magazynu w czasie')
    ax1.plot(x, occupation, label='Procent zapełnienia')

    ax2.cla()
    ax2.set_ylim(ymax=101, ymin=-1)
    ax2.set_xlabel('Czas [min]')
    ax2.set_title('Procent pracowników aktualnie wykonujących zadanie')
    ax2.plot(x, current_working, label='Aktualnie wykonujący zadanie')

    ax3.cla()
    ax3.set_xlabel('Czas [min]')
    ax3.set_title('Liczba dotychczasowych problemów')
    ax3.plot(x, warehouse_empty_number, label='Magazyn pusty')
    ax3.plot(x, warehouse_idle_number, label="Pracownik bezczynny")
    ax3.legend(loc='upper left')

    ax4.cla()
    ax4.set_xlabel('Czas [min]')
    ax4.set_title('Liczba nieobsłużonych zadań')
    ax4.plot(x, deliveries_number, label='Liczba dostaw')
    ax4.plot(x, orders_number, label='Liczba zamówień')
    ax4.legend(loc='upper left')

    plt.tight_layout()
