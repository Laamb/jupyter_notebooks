#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib
import numpy


# In[2]:


values = 1, 2, 3, 4, 5 

a, b, *rest = values

a, b

rest
# In[3]:


rest


# In[4]:


a = (1, 2, 2, 2, 2, 3, 4)
a.count(4)


# In[5]:


a.count(2)


# In[4]:


a_list = [2, 3, 7, None]

tup = ('foo', 'bar', 'baz')

b_list = list(tup)


# In[8]:


b_list


# In[5]:


b_list[1] = 'boo'


# In[10]:


b_list


# In[8]:


gen = range(10)

gen


# In[2]:


list(gen)


# In[7]:


b_list.append('dwarf')
b_list


# In[6]:


b_list


# In[9]:


b_list


# In[10]:


b_list.remove('foo')


# In[11]:


b_list


# In[16]:


x = [4, None, 'foo']

x.extend([7, 8 (2, 3)])
x


# In[18]:


a = [7, 2, 6, 0, 3, 5]

a.sort()


# In[19]:


a


# In[20]:


mapping = {}
for key, value in zip(key_list, value_list):
    mapping[key] = value
    
mapping = dict(zip(range(5), reversed(range(5))))

mapping


# In[1]:


# April 4, 2020; Built in Data Structures
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}

# Unions are all of the distint (unique) elements occuring
# in either data set
a.union(b)
a | b


# In[2]:


# Intersections contain the elements occuring in BOTH sets
a.intersection(b)
a & b


# In[3]:


# Logical set operations have things which let you replace
# or update the opposing side with the result
c = a.copy()

c |= b

c


# In[4]:


d = a.copy()

d &= b
d


# In[5]:


# List / Set / Dict Comprehension is one of Py's best ft.
# List:
# [expr for val in collection if condition] *Better*
# == *Equivalent to as a for loop as*:
# result = [] 
# for val in collection:
#     if condition:
#       result.append(expr)


# In[6]:


strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
[x.upper() for x in strings if len(x) > 2]


# In[7]:


# dictionary comprehension
dict_comp = {key-expr : value-expr for value in collection
            if condition}

#set comprehension
set_comp = {expr for value in collection if condition}

# these are mostly conveniences, but also make code easier
# to read and write


# In[8]:


# Consider the set
unique_lengths = {len(x) for x in strings}

unique_lengths


# In[9]:


# we can also express this as a function with map
set(map(len, strings))


# In[10]:


# as a dict comprehension, we ake a map of the strings to
# their locations in the list:
loc_mapping = {val : index for index, val in enumerate(strings)}

loc_mapping


# In[ ]:


# FUNCTIONS 

