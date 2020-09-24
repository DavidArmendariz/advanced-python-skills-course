#!/usr/bin/env python
# coding: utf-8

# # The complement of a set
# 
# When I teach operations of a set, some people ask: How can we find the complement of a set?
# 
# Well, you can't.
# 
# The complement of a set is everything not in the set, but part of the "universal set". Without a definition of the universal set, you can't really give a standard-library definition of the complement of a set.
# 
# Thus, the purpose of this task is to define a function that calculates the complement of a set. Your function will receive two arguments: the universal set and the set you want to calculate its complement.
# 
# If you can't calculate the complement (because the set is not a subset of the universal set), your function should return None.

# In[7]:


A = {'a','e','i','o','u'}
universal_set = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
                 'r','s','t','u','v','w','x','y','z'}


# In[8]:


def complement(universal_set, A):
    if A.issubset(universal_set):
        return universal_set - A
    else:
        return None


# In[9]:


complement(universal_set, A)


# In[ ]:




