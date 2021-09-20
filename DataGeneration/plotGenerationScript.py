#!/usr/bin/env python
# coding: utf-8

# In[17]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random
import os
from tqdm import tqdm
#from csv import writer

#def append_list_as_row(file_name, list_of_elem):
    #with open(file_name, 'a+', newline='') as write_obj:
        #csv_writer = writer(write_obj)
        #csv_writer.writerow(list_of_elem)
    



#array to store degree values
#degree = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
#array to store coefficient values
coeff = np.array([0, 1, 1, 1, 1, 1, 1, 1, 1])

#start for loop to create data
for i in tqdm(range(100), desc="Generating..."):
    
    x = np.linspace(-5, 5, 1000)

    fig, ax = plt.subplots()

    #for loop to randomize coefficients
    for j in range(1, 9):
        #sets each coefficient from 1 to 8 between -5 and 5
        coeff[j] = random.randint(-5,5)

    
    #for loop to determine highest degree
    #highestDegree = 0
    #for k in coeff:
        #if coeff[k] != 0:
            #highestDegree = k
            #break
    
    #pick a random background image
    backgroundNum = random.randint(0,15)
    backgroundPath = 'E:\\GitHub\\poly-curve-detector\\DataGeneration\\backgroundImages\\background'+ str(backgroundNum) + '.jpg'
    img = plt.imread(backgroundPath)
    
    
    #create plot
    ax.plot(x, (coeff[8]*x**8)+(coeff[7]*x**7)+(coeff[6]*x**6)
            +(coeff[5]*x**5)+(coeff[4]*x**4)+(coeff[3]*x**3)
            +(coeff[2]*x**2)+(coeff[1]*x**1)+(coeff[0]),
            color='#000000')
    
    ax.imshow(img, extent=[-5, 5, -5+coeff[0], 5+coeff[0]]) #image bounds
    ax.set_xlim(-5, 5) #plot x axis bounds
    ax.set_ylim(-5+coeff[0], 5+coeff[0]) #plot y axis bounds
    ax.tick_params(left = False, labelleft = False,
                   bottom =  False, labelbottom = False) #remove labels
    ax.grid(1)
    #plt.show()


    #create file name
    fileName = ''
    for l in range(1, 9):
        if coeff[l] >= 0:
            fileName = 'p' + str(coeff[l]) + fileName
        else:
            fileName = 'n' + str(abs(coeff[l])) + fileName
        
        
    #finish file name and create path
    fileIteration = 0
    fileName = fileName + '_' +str(fileIteration) + '.png'
    folderPath = 'E:\\GitHub\\poly-curve-detector\\DataGeneration\\plotData\\'
    filePath = folderPath + fileName


    #check if file name already exists
    isFile = os.path.isfile(filePath)
    while(isFile):
        fileIteration = fileIteration + 1
        fileName = fileName[:17] + str(fileIteration) + fileName[18:]
        filePath = folderPath + fileName
        isFile = os.path.isfile(filePath)
    

    #save file to specified path
    fig.savefig(filePath, bbox_inches = ('tight'), dpi = (30))
    plt.close('all')


    #end for loop


# In[ ]:





# In[ ]:




