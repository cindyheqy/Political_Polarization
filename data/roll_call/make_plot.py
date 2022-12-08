import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

polarity_change = pd.read_csv('/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization/tables/roll_call.csv')

polarity_change['Date'] = pd.to_datetime(polarity_change['Date'])
polarity_change['party'] = np.sign(polarity_change['polarity'])
fig, ax = plt.subplots(figsize = (15, 10))
cmap = colors.ListedColormap(['red', 'blue'])
# ax.scatter('Date', 'polarity', data=polarity_change.loc[polarity_change['party']==1], s=1, c='party', cmap=cmap)
ax.scatter('Date', 'polarity', data=polarity_change, s=1, c='party', cmap=cmap)
#plt.xticks(np.arange())
plt.axhline(y = 0, color = 'black', linestyle = '-', linewidth=0.3)
plt.show()