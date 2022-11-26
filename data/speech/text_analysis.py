import os
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
import matplotlib.pyplot as plt
import re
from datetime import datetime

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('spacytextblob')
nlp.max_length = 2000000

date_list = []
polarity_list = []

path = "/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization/data/speech/speech_data_content"
flag = 0
# try:
for fname in os.listdir(path): 
    if flag > 30: 
        break
    date = fname.replace(".txt", "")
    date = datetime.strptime(date, '%Y-%m-%d').date()
    date_list.append(date) 

    with open(f"{path}/{fname}") as page: 
        text = page.read()
    # if len(text) >= 2000000:
    #     print(fname)
    doc = nlp(text)

    polarity_list.append(doc._.blob.polarity) 
    data = {'Time': date_list, 'Polarity': polarity_list}
# except ValueError:
#     print(fname)
#     pass

df = pd.DataFrame(data)
df_sorted = df.sort_values(by='Time')
print(df_sorted)

f = plt.figure()
f.set_figwidth(20)
f.set_figheight(10)
plt.plot( 'Time', 'Polarity', data=df_sorted, marker='.', markerfacecolor='blue')
plt.legend()
plt.savefig("/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization/data/speech/polarity_2017.png")
