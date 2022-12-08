import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import random
import pandas as pd
plt.style.use('fivethirtyeight')


# slices = [120,80,30,20]
# labels = ['one-twenty','eighty','thirty','twenty']
# colors = ['#008fd5','#fc4f30','yellow','green']

# plt.pie(slices,labels=labels,colors=colors,wedgeprops={'edgecolor':'black'})
data = pd.read_csv('data/data2.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith'].fillna(' ')

language_counter = Counter()
for response in lang_responses:
    language_counter.update(response.split(';'))


languages = list()
popularity = list()

for item in language_counter.most_common(5):
    lang, popular = item
    languages.append(lang)
    popularity.append(popular)
languages.reverse()
popularity.reverse()
explode_range = np.arange(0,1,0.1)
# explode = [random.choice(explode_range) for _ in range(len(languages))]
explode = [0,0,0,0,0.1]
plt.pie(popularity,labels=languages,explode=explode,wedgeprops={'edgecolor':'black'},shadow=True,startangle=90,autopct='%1.2f%%')
# plt.pie(popularity,labels=languages,explode=explode,wedgeprops={'edgecolor':'black'},shadow=True,startangle=90,autopct='%1.0f%%')


plt.title('My Awesome Pie Chart')
plt.tight_layout()
plt.savefig('imgs/plot3.png')
plt.show()