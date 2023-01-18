import pandas as pd
import os
import re
from datetime import datetime
import matplotlib.pyplot as plt

# unzip
# delete W14.5_Diary16
# rename "W36_Jun 18" to "W36_Jun18"

def convert_time(fname): 
    time = folder
    time = re.sub('W10|W13', '2015', time)
    time = re.sub('W14|W15|W16|W17|W18|W19|W20|W21|W22|W23', '2016', time)
    time = re.sub('W24|W26|W27|W28|W29|W30', '2017', time)
    time = re.sub('W31|W32|W33|W34|W35|W36|W37|W38|W39|W40|W41', '2018', time)
    time = datetime.strptime(time, '%Y_%b%d').date()
    return time

def get_ideo(df):
    df['count'] = 0
    if 'F_IDEO_FINAL' in df.columns: 
        df_ideo = df.groupby('F_IDEO_FINAL').count()['count']
    elif 'F_IDEO' in df.columns:
        df_ideo = df.groupby('F_IDEO').count()['count']

    df_ideo = df_ideo.to_frame() 
    df_ideo.loc['Moderate', 'weight'] = 0
    df_ideo.loc['Conservative', 'weight'] = -0.5
    df_ideo.loc['Liberal', 'weight'] = 0.5
    df_ideo.loc['Very conservative', 'weight'] = -1
    df_ideo.loc['Very liberal', 'weight'] = 1
    df_ideo['count*weight'] = df_ideo['count'] * df_ideo['weight']
    df_ideo = df_ideo.dropna()
    return df_ideo

def get_polarity(df): 
    df_ideo = get_ideo(df)
    polarity = ((abs(df_ideo['count*weight'])).sum())/df_ideo['count'].sum()
    return polarity

def get_polarity_change_table(data): 
    polarity_change = pd.DataFrame(data)
    polarity_change = polarity_change.sort_values(by='Time')
    polarity_change = polarity_change.reset_index(drop=True)
    return polarity_change

time_list = []
polarity_list = []
path = '/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization/data/public_opinion/data'
for folder in os.listdir(path): 
    if folder.startswith('W'): 
        time = convert_time(folder)
        time_list.append(time)
        for file in os.listdir(os.path.join(path, folder)): 
            if file.endswith(".sav"): 
                df = pd.read_spss(os.path.join(path, folder, file))
                polarity = get_polarity(df)
                polarity_list.append(polarity)

data = {'Time': time_list, 'Polarity': polarity_list}
polarity_change = get_polarity_change_table(data)
polarity_change.to_csv('/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization/tables/public_opinion.csv')

# print(polarity_change)