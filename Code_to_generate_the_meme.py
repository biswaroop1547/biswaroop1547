import matplotlib.pyplot as plt
import numpy as np


plt.rcParams["figure.figsize"] = [14,9]
plt.rcParams['font.family'] = 'TSCu_Comic'
plt.rcParams["font.cursive"] = 'cursive'
plt.rcParams["axes.titlesize"] = 50
plt.rcParams["font.fantasy"] = 'xkcd'
fig, ax = plt.subplots()
Y_axis = ['Training\nSOTA models', 'Making this\nmeme in\nMatplotlib', 'Using my\ncustomized\nManjaro i3\nlinux OS in\nfront of my\nnon-coder\nfriends']
y_pos =   np.arange(len(Y_axis))
plt.axis('auto')
performance = [12, 30, 90]

# fig.subplots_adjust(top=0.8)
fig.subplots_adjust(left=0.2, top=0.8)
ax.barh(y_pos, performance, align='center', height=0.4, color=['#97d67c', '#7cb6d6', '#cf7a89'], edgecolor=['#000000', '#000000', '#000000'], linewidth=[7, 7, 7])
ax.set_yticks(y_pos)
ax.set_yticklabels(Y_axis, fontsize=24)
ax.tick_params(axis='y', which='major', pad=48)
ax.invert_yaxis()
plt.xticks([])

ax.set_title('\nWhat gives me the feeling of power ?\n', fontsize=46, loc='left', ha='left', position=(-0.17, 1))

ax.spines['left'].set_linewidth(7)


for axes in ['right', 'top', 'bottom']:
  ax.spines[axes].set_visible(False)

# plt.show()

fig.savefig('graph.png')
