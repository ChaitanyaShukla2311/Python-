#!/usr/bin/env python
# coding: utf-8

# package with function 
# 1.reverse string
# 2.vowels in string
# 3.length of string
# 4.string is palinndrom
# 5.convert to lower case
# 6.convert to upper case
# 7.show words in string
# 8.convert to ascii values 

# In[2]:


def rev(string):
    print(string[::-1])


# In[16]:


def vowel_in(string):
    s=set()
    for ch in string:
        if ch in 'aeiouAEIOU':
            s.add(ch)
    return s


# In[1]:


def len_of(string):
    count=0
    for i in string:
        count+=1
    return count


# In[11]:


def is_palindrome(string):
    if string==string[::-1]:
        return True
    return False



# In[12]:


def to_lower(string):
    return string.lower()



# In[13]:


def to_upper(string):
    return string.upper()




# In[14]:


def word_in(string):
    return string.split()



# In[15]:


def to_ascii(string):
    return (ord(ch) for ch in string)



# In[ ]:




