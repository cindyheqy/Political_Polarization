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

path = "/Users/qingyihe/Documents/GitHub/Political_Polarization/data/speech/speech_data_content"
flag = 0
# try:
for fname in os.listdir(path): 
    # flag += 1
    # if flag > 10: 
    #     break
    # if fname.startswith('2016'):
        date = fname.replace(".txt", "")
        date = datetime.strptime(date, '%Y-%m-%d').date()
        date_list.append(date) 

        with open(f"{path}/{fname}") as page: 
            text = page.read()
        # if len(text) >= 2000000:
        #     print(fname)
        doc = nlp(text)
        polarity = doc._.blob.polarity
        polarity_list.append(polarity) 
        print(date, polarity)
        data = {'Time': date_list, 'Polarity': polarity_list}
# except ValueError:
#     print(fname)
#     pass

df = pd.DataFrame(data)
df_sorted = df.sort_values(by='Time')
df_sorted = df_sorted.reset_index(drop=True)
df_sorted.to_csv('/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization/tables/speech.csv')