import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
import os
path = '/Users/guangbo_niu/Library/Mobile Documents/com~apple~CloudDocs/Academics/Autumn 2022/DPPP 2/final-project-political_polarization/'

polarity_change = pd.read_csv(os.path.join(path, 'tables/roll_call.csv'))
polarity_change['Date'] = pd.to_datetime(polarity_change['Date'])
polarity_change['party'] = np.sign(polarity_change['polarity'])
fig, ax = plt.subplots(figsize = (15, 10))
cmap = colors.ListedColormap(['red', 'blue'])
ax.scatter('Date', 'polarity', data=polarity_change, s=1, c='party', cmap=cmap)
plt.axhline(y = 0, color = 'black', linestyle = '-', linewidth=0.3)
plt.title('Congressional Voting Records')
plt.savefig(os.path.join(path, 'images/roll_call.png'))