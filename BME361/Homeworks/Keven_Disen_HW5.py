#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Keven Disen 111433335
#April 8, 2020
#BME 361
#Homework 5

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests
import numpy as np


# In[2]:


#received the website
webHtml = requests.get("https://www.sbnation.com/college-basketball/2020/3/24/21186863/college-basketball-players-ranking-obi-toppin-duke-kansas-kentucky").text
soup = BeautifulSoup(str(webHtml), "html.parser")


# In[3]:


#gets all of the id's needed in the h2 tag that contains the different information of the players
test = [r['id'] for r in soup.find_all(name="h2", attrs={"id":True})]


# In[4]:


#The id's with 6 characters are the ones that carry the different information of the players
id = []
for x in range(len(test)):
    if len(test[x]) == 6:
        id.append(test[x])


# In[5]:


#gets the information of each player and added into a list
eachPlayer = []
for x in range(len(id)):
    eachPlayer.append(soup.findAll("h2", {"id": id[x]}))


# In[6]:


#Tries getting ranks by searching the elements of the list
names = []
ranks = []
position = []
college = []
link = []

for x in range(len(eachPlayer)):
    ranks.append( re.findall(">(\d{1,2})", str(eachPlayer[x])))
    names.append(re.findall("\>([A-Za-z].*)(?=<\/a)", str(eachPlayer[x])))
    position.append(re.findall("([A-Z]{1,2})(?=,)", str(eachPlayer[x])))
    college.append(re.findall("(?<=[A-Z],)[-\s](.*)(?=\<)<\/h", str(eachPlayer[x])))
    link.append(re.findall("(?<=<a href=\")(.*)(?=\")", str(eachPlayer[x])))

Table = pd.DataFrame({'Rank': ranks, 
                      'Name': names, 
                      'Position': position, 
                      'College': college,
                     'Link': link})

#Sort in who's highest ranked
Table = Table.sort_index(ascending = False)


# In[7]:


#I had to manually input these because the html format wasnt the same as the others
Table.at[49, 'Name'] = "Obi Toppin"
Table.at[48, 'Name'] = "Udoka Azuibuike"
Table.at[46, 'Name'] = "Markus Howard"
Table.at[43, 'Name'] = "Luka Garza"
Table.at[38, 'Name'] = "Onyeka Okongwu"
Table.at[29, 'Name'] = "Immanuel Quickley"
Table.at[23, 'Name'] = "Filip Petrušev"
Table.at[10, 'Name'] = "Kira Lewis"

Table


# In[ ]:





# In[ ]:





# In[ ]:




