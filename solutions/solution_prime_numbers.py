#!/usr/bin/env python
# coding: utf-8

# # Prime numbers
# 
# Write an infinite generator that yields prime numbers.
# 
# This is one of those generators that you have to be very careful about. Checking if a number is prime or not is a really expensive task. In fact, all of the cryptography and security over the Internet relies on this fact. If it weren't like this, then surely your bank account would have been compromised long time ago!
# 
# Your task here is to write a generator that generates prime numbers, and that is what is going to be evaluated. But as a bonus do the following:
# 
# Modify the generator so that it yields not only the next prime number, but also the time that it took to find that prime number.
# 
# Make a scatter plot (maybe using matplotlib) where the x-axis consists of the prime numbers and the y-axis is the value it took to find that prime number.

# In[55]:


import time


# In[56]:


def prime_numbers():
    n = 2
    yield (n, 0)
    while True:
        start_time = time.time()
        n += 1
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            end_time = time.time() - start_time
            yield (n, end_time)


# In[57]:


import matplotlib.pyplot as plt


# In[58]:


x = []
y = []


# In[59]:


prime_numbers = prime_numbers()


# In[60]:


for i in range(1000):
    result = next(prime_numbers)
    x.append(result[0])
    y.append(result[1])


# In[61]:


plt.plot(x,y)
plt.title("Time taken to calculate prime numbers")
plt.xlabel("Prime numbers")
plt.ylabel("Time in seconds")


# In[ ]:




