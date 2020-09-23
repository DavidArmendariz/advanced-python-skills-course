#!/usr/bin/env python
# coding: utf-8

# # Transforming data formats
# 
# The reduce function is extremely useful to transform data structures. When I say data structure, I am not talking about queues, linked lists and all of those things. I am talking about how a dataset is presented (or structured). For example, suppose we have a list of dictionaries like this:
# 
# ```
# invitees = [{"email": "alex@example.com", "name": "Alex", "status": "attending"},
# {"email": "brian@example.com", "name": "Brian", "status": "declined"},
# {"email": "carol@example.com", "name": "Carol", "status": "pending"},
# {"email": "david@example.com", "name": "David", "status": "attending"},
# {"email": "maria@example.com", "name": "Maria", "status": "attending"}]
# ```
# 
# You want to transform this list of dictionaries to a single dictionary like this:
# 
# ```
# {"alex@example.com": "attending",
# "brian@example.com": "declined",
# "carol@example.com": "pending",
# "david@example.com": "attending",
# "maria@example.com": "attending"}
# ```
# 
# Here, the reduce function can help. You just have to write an adequate function (maybe using a lambda function won't work here) and pass it to the reduce function, along with the invitees list and an empty dictionary as the initializer.
# 
# Give it a try!

# In[14]:


from functools import reduce


# In[15]:


def transform_invitees_data(invitees):
    def transform_data(acc, invitee):
        acc[invitee["email"]] = invitee["status"]
        return acc
    results = reduce(transform_data, invitees, {})
    return results


# In[16]:


invitees = [{"email": "alex@example.com", "name": "Alex", "status": "attending"},
{"email": "brian@example.com", "name": "Brian", "status": "declined"},
{"email": "carol@example.com", "name": "Carol", "status": "pending"},
{"email": "david@example.com", "name": "David", "status": "attending"},
{"email": "maria@example.com", "name": "Maria", "status": "attending"}]


# In[17]:


transform_invitees_data(invitees)


# In[ ]:




