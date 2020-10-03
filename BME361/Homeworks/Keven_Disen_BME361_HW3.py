#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Keven Disen
#111433335
#BME 361
#2/26/20

import math, random

# Create list of powerball numbers
powerball = []
redBall = random.randint(1,26)

print("Your red ball is", redBall)
print()

#Getting random white ball numbers
for i in range(5):
    whiteBall = random.randint(1,69)
    powerball.insert(i, whiteBall)

#Adding red ball to the end
powerball.append(redBall)

#Checking if the white balls are equal, excluding the red ball
for i in range(len(powerball) - 1):
    for j in range(i+1, len(powerball)-2):
        if powerball[i] == powerball[j]:
            powerball[j] = random.randint(1,69)
            j=j+1
        else:
            break;
    
        
print ("These are your lottery numbers \n", powerball)
print()

#Checking probability for each number that is drawn



probability = int((math.factorial(69) * 26) / (math.factorial(69-5) * math.factorial(5)))
    
probmsg = f'You have 1 in {probability} chances to win the powerball'
print(probmsg)
    
    


# # 

# In[ ]:




