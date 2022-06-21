import matplotlib.pyplot as plt
import numpy as np

plt.figure()

game_platforms = ['PS5' , 'Series X', 'Nitendo Switch', 'PC', 'Mobile']
pos = np.arange(len(game_platforms))
popularity = [38, 25, 42, 55, 21]

#change the bar colors to be less bright blue
bars = plt.bar(pos, popularity, align = 'center', linewidth = 0, color = 'lightslategrey')
#make  the PS5 bar a contrasting color
bars[0].set_color('#1F77B4')


plt.xticks(pos, game_platforms)
plt.ylabel('% Popularity')
plt.title('Top 5 Gaming platforms', alpha = 0.8)

#remove all the ticks (both axes) and tick labels on the Y axis
plt.tick_params(top = 'off', bottom = 'off', left = 'off', right = 'off', labelleft = 'off', labelbottom = 'on')

for spine in plt.gca().spines.values():  #Remove the frame of the chart
    spine.set_visible(False)

#direct label for each bar with Y axis values
for bar in bars:
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str(int(bar.get_height())) + '%',
                  ha = 'center', color = 'w', fontsize = 11)

plt.show()
