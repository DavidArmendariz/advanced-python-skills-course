#!/usr/bin/env python
# coding: utf-8

# # Have you seen this number before?
# 
# Write a function that receives as an argument a list of numbers. For each number, append to an empty list the word "YES" if this number was previously encountered in the sequence, or "NO" if it was not.
# 
# Example:
# ```
# Input data:
# [1,2,1,2,4,5]
# Output:
# ["NO", "NO", "YES", "YES", "NO", "NO"]
# ```

# In[1]:


def number_seen(list_of_numbers):
    result_set = set()
    result = []
    for x in list_of_numbers:
        if x not in result_set:
            result_set.add(x)
            result.append("NO")
        else:
            result.append("YES")
    return result


# In[2]:


number_seen([1,2,1,2,4,5])


# In[ ]:




