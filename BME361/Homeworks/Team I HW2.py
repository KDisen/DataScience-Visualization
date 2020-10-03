#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Joewin James, 111709919
#Niti Punn, 111523470
#Brandon Paradiso, 111430356
#Keven Disen, 111433335



def drawRectangle():
    rectangleHeight = int(input("Enter rectangle height: "))
    rectangleWidth = int(input("Enter rectangle width: "))
    width = []
    height = []

    for i in range(rectangleWidth):
            width.append("*")

    for i in range(rectangleWidth):
        if i == 0 or i == rectangleWidth-1:
            height.append("*")
        else:
            height.append(" ")

    for i in range(rectangleHeight):
        if i == 0 or i == rectangleHeight-1:
            print(''.join(width))
        else:
            print(''.join(height))

    stop = input("Press enter to return to menu")

def drawDoublePyramid():
    pyramidHeight = int(input("Enter length of pyramid"))
    
    #putting stars in order
    leftSpaces = 2*pyramidHeight
    
    for i in range(0, pyramidHeight):
        for j in range(0, leftSpaces):
            print(end = " ")
       
    #substracts 1 to create pyramid
        leftSpaces= leftSpaces -1
        
    #adds an extra star everytime
        for j in range(0, i+1):
            print("* ", end = " ")
        
        print("\n") 
    #As the spaces are subtracting, the stars are adding to put the stars in line for a pyramid
    
   
    #Reverse Pyramid under 
    leftSpaces = leftSpaces + 1
    for i in range(pyramidHeight, 0, -1):
        for j in range(leftSpaces, 0, -1):
            print(end = " ")
       
    #substracts 1 to create pyramid
        leftSpaces= leftSpaces +1 
        
    #adds an extra star everytime
        for j in range(0, i):
            print("* ", end = " ")
        
        print("\n")
        
    stop = input("Press enter to return to menu")
    
while True:
    answer = str(input("r for rectangle, p for pyramid, q to quit: "))
    if answer == "r":
        drawRectangle()
    elif answer == "p":
        drawDoublePyramid()
    elif answer == "q":
        break
    else:
        print("Invalid")
        
        


# ### 
