#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question_1
from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
num_list = array_num.tolist()
print("Convert the said array to an ordinary list with the same items:")
print(num_list)


# In[2]:


#Question_2
import numpy as np
  
# creating a 3X3 Numpy matrix
n_array = np.array([[55, 25, 15],
                    [30, 44, 2],
                    [11, 45, 77]])
  
# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)
  
# calculating the Trace of a matrix
trace = np.trace(n_array)
  
  
print("\nTrace of given 3X3 matrix:")
print(trace)


# In[3]:


#Question_3
import numpy as np
x = np.array([[0, 10, 20], [20, 30, 40]])
print("Original array: ")
print(x)
print("Values bigger than 10 =", x[x>10])
print("Their indices are ", np.nonzero(x > 10))


# In[1]:


#Question_4
import numpy as np

A = np.array([1,2,3,4])
B = np.array([4,5,6,7])
C = A + B
print(C)


# In[16]:


#Question_5
import numpy as np
print("Original matrix:\n")
X = np.random.rand(5, 10)
print(X)
print("\nSubtract the mean of each row of the said matrix:\n")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)


# In[ ]:




