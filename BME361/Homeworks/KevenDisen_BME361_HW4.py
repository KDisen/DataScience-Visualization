#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Keven Disen
#111433335
#BME 361
#Homework 4

import re

#Finding file and reading it
file = open("Email1.txt")
text = file.read()

#Finds all the emails inside the text file
emails = re.findall('\S+@\S+', text)
# "\S+" is non-whitespace characters  
# so it captures the name of the user before the @ and after 
     
reduce()
print("First text file:\n", emails)


#Finding email file 2
file = open("Email2.txt")
text = file.read()

emails = re.findall('\S+@\S+', text)
reduce()
print("\nSecond text file:\n", emails)

#Finding email file 3
file = open("Email3.txt")
text = file.read()

emails = re.findall('\S+@\S+', text)
reduce()
print("\nThird text file:\n", emails)


#reduce amount of emails
def reduce():
    for i in range(len(emails)):
        for j in range(1, len(emails)):
            if i == j:
                emails.pop(j)
            j=j+1
        


# In[21]:





# In[ ]:




