#!/usr/bin/env python
# coding: utf-8

# # Anagrams
# 
# You will write a function that receives a word and a list of words and stay with all of those words in the list that are anagrams of the word passed. 
# ``` 
# Input:
# First argument: "code"
# Second argument: ["code", "deco", "ecod", "first", "strif", "frist"]
# Output:
# ["code", "deco", "ecod"]
# ```

# In[1]:


def find_anagrams(word, list_of_words):
    sorted_word = sorted(word)
    # code -> cdeo
    return list(filter(lambda x: sorted(x) == sorted_word, list_of_words))


# In[2]:


find_anagrams("code", ["code", "deco", "ecod", "first", "strif", "frist"])


# In[ ]:




