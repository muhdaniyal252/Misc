#Bar Chart

#Start


import matplotlib.pyplot as plt
import numpy as np
# import csv
from collections import Counter
import pandas as pd

plt.style.use('fivethirtyeight')

data = pd.read_csv('data/data2.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith'].fillna(' ')

language_counter = Counter()
for response in lang_responses:
    language_counter.update(response.split(';'))

# with open('data/data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     language_counter = Counter()
#     for row in csv_reader:
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))
#     # row = next(csv_reader)
#     # print(row['LanguagesWorkedWith'].split(';'))

languages = list()
popularity = list()

for item in language_counter.most_common(15):
    lang, popular = item
    languages.append(lang)
    popularity.append(popular)
languages.reverse()
popularity.reverse()
plt.barh(languages, popularity) #y axis first and then x axis
# plt.bar(languages, popularity)


plt.xlabel('Number of people who use')




# plt.xticks(ticks=x_indexes,labels=ages_x)



# plt.legend()
plt.tight_layout()
# plt.savefig('imgs/plot2.png')
plt.show()

