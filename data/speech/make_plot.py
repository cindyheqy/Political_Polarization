import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization/data/speech/output.csv')

f = plt.figure()
f.set_figwidth(20)
f.set_figheight(10)
plt.plot( 'Time', 'Polarity', data=df, marker='.', markerfacecolor='blue')
plt.legend()
plt.savefig("/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization/data/speech/plot.png")
