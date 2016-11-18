# LR as a prediction model
# fitting a line to your data points 
# using R squared to measure accuracy 
''' Using R squared- scipy.stats.linregress'''
# https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.linregress.html
''' refference to documentation '''
from scipy import stats
import numpy as np 

import matplotlib.pyplot as plt
# random distributed data 
x = np.random. normal(3.0,1.0,1000)
# values of x cenetres around 3 , standard deviation 1 
y = 100 - (x + np.random.normal(0, 0.1, 1000)) * 3
# linear relationship between x and y 

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print "r_squared", r_value**2

# plotting the randomly generated data and plotting the line that fits the data



def predict(x1):
	return slope * x+ intercept 

fitLine = predict(x)
plt.scatter(x, y)
plt.plot(x, fitLine, c='r' )
plt.show()
