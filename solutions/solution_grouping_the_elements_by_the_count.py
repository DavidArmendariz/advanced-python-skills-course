#!/usr/bin/env python
# coding: utf-8

# # Grouping the elements by the count
# 
# So, we already know how to find the most common elements using the Counter class right? But what if two or more elements have the same count? Remember that the most_common() method returns a list of tuples. Instead of that, we want to return a dictionary where they keys are the counts and the values are lists that contain the elements with that count.
# 
# Example:
# 
# ```
# Input data:
# ["apple", "apple", "grapes", "grapes", "watermelon"]
# Output:
# {2: ["apple", "grapes"], 1: ["watermelon"]}
# ```
# 

# In[1]:


from collections import Counter


# In[2]:


def find_counts(list_of_elements):
    counts = Counter(list_of_elements)
    result = dict()
    for element, count in counts.items():
        result[count] = result.setdefault(count, []) + [element]
    return result


# In[3]:


find_counts(["apple", "apple", "grapes", "grapes", "watermelon"])


# In[ ]:




