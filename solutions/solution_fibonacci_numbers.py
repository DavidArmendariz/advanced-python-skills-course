#!/usr/bin/env python
# coding: utf-8

# # Fibonacci Numbers
# 
# Let's apply what we learned about generators by creating the so famous Fibonacci sequence.
# 
# You must create a generator that yields fibonacci numbers. This must be an infinite stream generator. Thus, the function won't receive any arguments. You should not use recursion.
# 
# Instead, you should take advantage of the fact that generators "remember" the state of the function.
# 
# Remember that the first element (index 0) is 0 and the second element (index 1) is 1.

# In[18]:


def fibonacci_numbers():
    a = 0
    b = 1
    yield a
    yield b
    while True:
        c = a + b
        a, b = b, c
        yield b


# In[19]:


fib = fibonacci_numbers()


# In[29]:


next(fib)


# In[ ]:




