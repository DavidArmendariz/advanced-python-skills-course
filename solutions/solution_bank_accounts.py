#!/usr/bin/env python
# coding: utf-8

# # Bank Accounts
# 
# In this exercise, we will be creating a BankAccount class.
# 
# This class must have a constructor that receives an initial amount and set it to a property called balance. If you don't provide an initial amount, then you should set balance with zero. 
# 
# You should write a setter and a getter for this property.
# 
# The setter should validate if the amount you pass is greater than or equal to zero. If it is negative, the balance should be setted to zero.
# 
# Pretty easy!

# In[1]:


class BankAccount:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            self._balance = 0


# In[2]:


bank_account = BankAccount()


# In[7]:


bank_account.balance = -60


# In[8]:


bank_account.balance


# In[ ]:




