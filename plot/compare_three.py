import pandas as pd
import os

path = '/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization/tables'
public_opinion = pd.read_csv(os.path.join(path, 'public_opinion.csv'))
speech = pd.read_csv(os.path.join(path, 'speech.csv'))
# roll_call = pd.read_csv(os.path.join(path, 'roll_call.csv'))