import numpy as np
import scipy
import matplotlib.pyplot as plt
import sys

def compute_r_squared(data, predictions):
    '''
    In exercise 5, we calculated the R^2 value for you. But why don't you try and
    and calculate the R^2 value yourself.
    
    Given a list of original data points, and also a list of predicted data points,
    write a function that will compute and return the coefficient of determination (R^2)
    for this data.  numpy.mean() and numpy.sum() might both be useful here, but
    not necessary.

    Documentation about numpy.mean() and numpy.sum() below:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html
    '''
    
    # your code here
    average = np.mean(data)
    sum_num = 0
    sum_deno = 0
    for d, p in zip(data, predictions):
        sum_num = sum_num + ((d - p)**2)
    for d in data:
        sum_deno = sum_deno + ((d - average)**2)
    
    r_squared = 1 - (sum_num / sum_deno)  
    return r_squared