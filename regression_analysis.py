import pandas as pd
import os
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

path = '/Users/guangbo_niu/Library/Mobile Documents/com~apple~CloudDocs/Academics/Autumn 2022/DPPP 2/Political_Polarization/tables'
congress_polarity = pd.read_csv(os.path.join(path, 'roll_call.csv'))
public_opinion = pd.read_csv(os.path.join(path, 'public_opinion.csv'))
speech = pd.read_csv(os.path.join(path, 'speech.csv'))

# calculate absolute values of roll_call polarity and get means by date
congress_polarity['roll_call_polarity_abs'] = congress_polarity['polarity'].abs()
roll_call_polarity = pd.DataFrame(congress_polarity.groupby('level_2')['roll_call_polarity_abs'].mean())
roll_call_polarity = roll_call_polarity.reset_index()

# merge roll call and speech data for regression
speech['speech_polarity']=speech['Polarity']
roll_call_plus_speech = pd.merge(roll_call_polarity, speech.loc[:, ['Time', 'speech_polarity']], left_on='level_2', right_on='Time')

roll_call_plus_speech_reg = smf.ols('roll_call_polarity_abs ~ speech_polarity', data=roll_call_plus_speech).fit()
print(roll_call_plus_speech_reg.summary())