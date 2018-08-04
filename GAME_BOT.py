
# coding: utf-8

# In[100]:


from PIL import ImageGrab,ImageOps


# In[101]:


import pyautogui 
import time
from numpy import *


# In[ ]:


class cordinates():
    replay=(338,326)
    dinosaur=(75,332)
    up=(75,323)
    
def restartgame():
    pyautogui.click(cordinates.replay)
    
    

    
def pressspace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    
    pyautogui.keyUp('space')
    
def imagegrab():
    box=(cordinates.dinosaur[0]+40,cordinates.dinosaur[1],cordinates.dinosaur[0]+90,cordinates.dinosaur[1]+30)
    image=ImageGrab.grab(box)
    grayImage=ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    return(a.sum())

def main():                 
    restartgame()
    
    while True:
        if(imagegrab()!=1747):
            pressspace()
            time.sleep(0.01)
            
            
main()
    
        
            
            

