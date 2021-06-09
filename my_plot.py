import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plot():
    # plt.title('Procentowe zapełnienie magazynu w czasie')
    # print(plt.style.available)
    # plt.style.use('fivethirtyeight')

    fig, (ax1, ax2) = plt.subplots(nrows=2)

    ani = FuncAnimation(fig, lambda *args: animate(ax1=ax1, ax2=ax2, *args), interval=1000)

    plt.style.use('fivethirtyeight')
    ax1.set_xlabel('Czas')
    # ax1.set_ylabel('Procent zapełnienia magazynu [%]')

    plt.tight_layout()
    plt.show()

def animate(i, ax1, ax2):
    data = pd.read_csv('../data/warehouse_occupation.csv')
    x = data['sim_time']
    occupation = data['occupation_value']
    current_working = data['current_working_value']
    # y2 = data['total_2']

    ax1.cla()
    ax1.set_ylim(ymax=100, ymin=0)
    ax1.set_title('Procentowe zapełnienie magazynu w czasie')
    ax1.plot(x, occupation, label='Procent zapełnienia')

    ax2.cla()
    ax2.set_ylim(ymax=100, ymin=0)
    ax2.set_title('Procent pracowników aktualnie wykonujących zadanie')
    ax2.plot(x, current_working, label='Aktualnie wykonujący zadanie')

    # ax1.legend(loc='upper left')
    plt.tight_layout()
