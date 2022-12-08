#Start


import matplotlib.pyplot as plt

# plt.style.use('ggplot')
plt.xkcd()

ages_x = [i for i in range(25,36)]

py_dev_y = [45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]
plt.plot(ages_x,py_dev_y, label='Python')
# plt.plot(ages_x,py_dev_y, color='b', marker='o', label='Python')
# plt.plot(ages_x,py_dev_y, 'b',label='Python')

js_dev_y = [39810,43515,46823,49293,53437,56373,62375,66674,68745,68746,74583]
plt.plot(ages_x,js_dev_y, label='JavaScript')

dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
plt.plot(ages_x,dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')
# plt.plot(ages_x,dev_y, color='k', linestyle='--', marker='.', label='All Devs')
# plt.plot(ages_x,dev_y, 'k--', label='All Devs')


plt.xlabel('Ages')
plt.ylabel('Median Saraly (USD)')
plt.title('Median Saraly (USD) by age')

# plt.legend(['All Devs', 'Python'])
# fmt = '[marker][line][color]'
plt.legend()
# plt.grid(True)
plt.tight_layout()
plt.savefig('imgs/plot.png')
plt.show()

