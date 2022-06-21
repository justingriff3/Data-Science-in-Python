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

from random import randint  #python library for generating random numbers
linear_err = [randint(0,15) for x in range(len(linear_data))] #theoretical list of error values generating from random int
plt.bar(xvals, linear_data, width=0.3, color =  yerr = linear_err) #

#Stacked bar charts: Cummalative values while keeping values independent
plt.figure()
xvals = range(len(linear_data)) 
plt.bar(xvals, linear_data, width = 0.3, color = 'b')
plt.bar(xvals, quadratic_data, width = 0.3, bottom = linear_data, color ='r')

#Horizontal bar graph
plt.figure()
xvals = range(len(linear_data))
plt.barh(xvals, linear_data, height = 0.3, color = 'blue')
plt.barh(xvals, quadratic_data, height = 0.3, left = linear_data, color = 'r')


