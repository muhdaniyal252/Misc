import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('fivethirtyeight')

# ages = [18,19,21,25,26,26,30,32,38,45,55]

# plt.hist(ages,bins=5,edgecolor='black')
# bins = [10,20,30,40,50,60]
# plt.hist(ages,bins=bins,edgecolor='black')

data = pd.read_csv('data/data6.csv')
ids = data['Responder_id']
ages = data['Age']
bins = [10,20,30,40,50,60,70,80,90,100]
plt.hist(ages,bins=bins,edgecolor='black',log=True)

median_age = 29
color = '#fc4f30'

plt.axvline(median_age, color=color,label='Age Median',linewidth='2')
plt.legend()
plt.title('Age of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')
plt.tight_layout()
plt.savefig('imgs/plot6.png')
plt.show()