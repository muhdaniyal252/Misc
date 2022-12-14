import matplotlib.pyplot as plt
import pandas as pd
# plt.style.use('fivethirtyeight')

data = pd.read_csv('data/data5.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages,dev_salaries,color='#444444',linestyle='--',label='All Devs')
plt.plot(ages,py_salaries,label='Python')

overall_median = 57287

# plt.fill_between(ages, py_salaries,overall_median, where=(py_salaries > overall_median), interpolate=True, alpha=0.25)
# plt.fill_between(ages, py_salaries,overall_median, where=(py_salaries < overall_median), interpolate=True, color='red',alpha=0.25)
plt.fill_between(ages, py_salaries,dev_salaries, where=(py_salaries > dev_salaries), interpolate=True, alpha=0.25,label='Above Avg')
plt.fill_between(ages, py_salaries,dev_salaries, where=(py_salaries < dev_salaries), interpolate=True, color='red',alpha=0.25,label='Below Avg')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()
plt.savefig('imgs/plot5.png')
plt.show()