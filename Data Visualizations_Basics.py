%matplotlib notebook

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
plt.get_backend()

#BASIC PLOTTING
plt.plot?
plt.plot(3, 2, '.', color = "red")

linear_data =  np.array([1,2,3,4,5,6,7,8])
quadratic_data = linear_data**2
plt.plot(linear_data, quadratic_data, color = "purple")

#SCATTERPLOTS
poly_data = linear_data**3
plt.scatter(linear_data, poly_data, color = "orange")

colors = ['blue']*(len(linear_data)-1)
colors.append('yellow')
plt.scatter(linear_data, linear_data, s = 10, color = colors)

#BAR CHARTS
plt.figure()
xvals = range(len(linear_data))
yvals = linear_data
plt.bar(xvals, yvals, width = 0.3, color = "black")

new_xvals = []
for item in xvals:
    new_xvals.append(item+0.3)
    
plt.bar(new_xvals, quadratic_data, width=0.3,color='red')

#from random import randint
#linear_err = [randint(0,150) for x in range(len(linear_data))]
#plt.bar(xvals, linear_err, width = 0.3)
