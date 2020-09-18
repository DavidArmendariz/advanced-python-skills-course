#!/usr/bin/env python
# coding: utf-8

# # XOR
# 
# XOR (exclusive or) is a boolean operator with the following truth table:
# 
# ``` 
# XOR(0,0) = 0
# 
# XOR(0,1) = 1
# 
# XOR(1,0) = 1
# 
# XOR(1,1) = 0
# ```
# 
# You must write a function that receives two lists as the arguments. These lists must consist of zeros and ones. Let's call them A and B.
# 
# The function should return a list where the i-th element is `XOR(A[i], B[i])`.
# 
# Example:
# 
# ``` 
# Input data:
# First argument: [0, 0, 1, 1]
# Second argument: [0, 1, 0, 1]
# Output:
# [0, 1, 1, 0]
# ```
# Please, use the map and zip functions.

# In[3]:


def xor(A, B):
    return list(map(lambda x: x[0] ^ x[1], zip(A, B)))


# In[4]:


xor([0,0,1,1], [0,1,0,1])


# In[5]:


xor([1,0,1,1], [1,0,0,1])


# In[ ]:




