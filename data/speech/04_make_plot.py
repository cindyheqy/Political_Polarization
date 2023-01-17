import pandas as pd
import matplotlib.pyplot as plt
import os

path = pd.read_csv('/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization')
df = pd.read_csv(os.path.join(path, 'tables/speech.csv'))

f = plt.figure()
f.set_figwidth(20)
f.set_figheight(10)
plt.plot( 'Time', 'Polarity', data=df, marker='.', markerfacecolor='blue')
plt.legend()
plt.savefig(os.path.join(path, 'images/speech_plot.png'))