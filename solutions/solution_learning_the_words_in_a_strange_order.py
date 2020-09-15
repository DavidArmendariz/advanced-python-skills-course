#!/usr/bin/env python
# coding: utf-8

# # Learning the words in a strange order
# 
# One of your friends wants to learn new English words, but wants to do it in a certain order. 
# 
# - First, he chooses short words
# 
# - If the words are the same length, he chooses them in lexicographical order when reading from right to left (he is Arab!). 
# 
# Write a function that receives a list of words, and returns a list in the order specified.
# 
# Here is an example:
# 
# ``` 
# Input data:
# ["west", "tax", "size", "sea", "use", "think", "yard", "word", "town"]
# 
# Program output:
# ["sea", "use", "tax", "yard", "word", "size", "town", "west", "think"]
# ```

# In[20]:


def learning_words(list_of_words):
    words = dict()
    # words = {4: ["west", "size", "yard", "word", "town"], 3: ["tax", "sea", "use"], 5: ["think"]}
    result = []
    for word in list_of_words:
        length = len(word)
        words[length] = words.get(length, []) + [word]
    for length in sorted(words):
        # length = 3
        # words[length] = ["tax", "sea", "use"]
        # -> ["xat", "aes", "esu"]
        # -> ["aes", "esu", "xat"]
        # -> ["sea", "use", "tax"]
        for word in sorted([x[::-1] for x in words[length]]):
            result.append(word[::-1])
    return result


# In[21]:


learning_words(["west", "tax", "size", "sea", "use", "think", "yard", "word", "town"])


# In[ ]:




