import matplotlib.pyplot as plt
import pandas as pd
import os

def draw_change(df): 
    f = plt.figure()
    f.set_figwidth(20)
    f.set_figheight(10)
    plt.plot( 'Time', 'Polarity', data=df, marker='.', markerfacecolor='blue')
    plt.legend()

path = '/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization'
public_opinion = pd.read_csv(os.path.join(path, 'tables', 'public_opinion.csv'))
draw_change(public_opinion)
plt.savefig(os.path.join(path, 'images', 'public_opinion.png'))