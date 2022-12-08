import matplotlib.pyplot as plt
import pandas as pd
import random
from  itertools import count
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

index = count()

def animate(i):

    data = pd.read_csv('data/data9.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    
    plt.cla()
    plt.plot(x,y1, label='Channer 1')
    plt.plot(x,y2, label='Channer 2')
    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()