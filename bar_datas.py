import matplotlib.pyplot as plt
import numpy as np

xlabels = ('121-2(1) #1', '121-2(1) #2', '121-2(1) #3')
bad_ones =  [5, 4, 1]
good_ones = [4.5, 6, 5]
bad_read = [0,0,2]
good_read = [0,0,4]

x = np.arange(len(xlabels))
width = 0.20
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,bad_ones, width,label='BAD DAY')
rects3 = ax.bar(x - width/0.73,bad_read,width,label='BAD READ')
rects2 = ax.bar(x + width/2,good_ones,width,label='GOOD DAY')
rects4 = ax.bar(x + width/0.67,good_read,width,label='GOOD READ')

ax.set_title('121-2(1)')
ax.set_ylabel('Measuring')
ax.set_xticks(x,xlabels)
ax.legend()

ax.bar_label(rects1,padding=3)
ax.bar_label(rects2,padding=3)
ax.bar_label(rects3,padding=3)
ax.bar_label(rects4,padding=3)

fig.tight_layout()

plt.show()