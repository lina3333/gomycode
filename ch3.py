#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Question_1
list=str=int(input("enter your list of numbers"))
product = 1
for item in list: 
   product = product * item
print(product)


# In[ ]:


#Question_2
def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# In[16]:


#Question_3
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)


# In[11]:


#Question_4
n = int(input("Enter the value of n: "))
squares = {i : i*i for i in range(1, n+1)}
print(squares)


# In[14]:


#Question_5
list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(price, key=lambda x: float(x[1]), reverse=True))


# In[ ]:




