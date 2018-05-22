
# coding: utf-8

# In[223]:


#Derek Lee A11234954
#begin documentation and discussion of the problem:
#basic algorithm: use numpy to create 2d arrays and random for random values inbetween ranges that fit into the array
#                 the 2d array consists of 0s and 1s where 1 is covered. use random to find a tower locations(top right
#                 of a coverage rectangle) and then random again to find a x and y range of the tower(length and width)
#                 Continue to do so until an overlap occurs. Use a helper array to carry a tower coverage with the overlap
#                 removed. Then from that array calculate the area/largest rectangle possible. Then put that rectangle into
#                 the actual coverage map. Then continue putting down towers up to the num_towers specified.
#
#Problems I was unable to complete the largest rectangle in the trimmed coverage. I was unable to find the trimmed 
#          area and the area of the largest rectangle. But was unable to convert it into an array style to fit
#          back into the main coverage. I attempted both brute force and histogram method but was unable to come to an answer.
#          Even after coming to the correct area of the largest rectangle I was unsure as to how I could get the actual
#          rectangle. 
#trade-offs: Because of the way I made the towers, the top left corner is the start of the rectangle, it could be somewhat
#            slower to fill the space because of the allowable range in random. Also Brute forcing the largest rectangle,
#            has significant speed decreases over finding the rectangle through the histogram method.(where the largest)
#            histogram made from a row contains the largest possible rectangle.
#Limitations: This notebook does not complete the computational requirements, but hopefully meets code quality and 
#             documentation standards. I have left the notebook in a state where you can see the trimmed coverages that 
#             just need to be converted into the largest rectangle. Each loop does one trimmed tower, and eventually 
#             fills the trimmed 2d array.
#analysis: My program is at least O(n^3) because of the three nested forloops, however, if the brute forcing section was
#          uncommented it would be higher than that. Brute forcing was more difficult for me because it was nested within
#          a for loop that writes out the trimmed array per loop cycle. So getting the information via j[0] would give an
#          error because not all of the trimmed arrays(up to the number of towers) has been written.

import random #for uniform dist
import numpy as np #for easy matrix

def adhoc_network(x, y, num_towers):
    assert isinstance(x,int)
    assert x > 0 #Assuming that the coverage range cannot be nothing or negative
    assert y > 0
    assert isinstance(y,int)
    assert isinstance(num_towers, int)

    trimItr = 0
    
    temp_coverage = np.zeros(shape=(x,y)) # temp coverage for testing and visualization (coverage with overlap)
    coverage = np.zeros(shape=(x,y)) # actual coverage
    overlap = [[] for i in range(num_towers)] # coordinates of overlap for each tower
    trimmed = [[] for i in range(num_towers)] #coordinates of a rectangle but with overlaps missing
    nptrimmed = np.zeros(shape=(x,y)) # np array for visualization of trimmed
    
    #NOTE: x refers to the number of rows, y refers to the number of columns
    
    #for loop for the number of towers available to be placed
    for i in range(num_towers):
        xtower = random.randint(0,x-1) #x coordinate of a tower, randomly generated (this is the top left of a rectangle)
        ytower = random.randint(0,y-1) #y coordinate of said tower, randomly generated(y cood of the top left of a rectangle)
        #because this coordinate is the top left of a rectangle, the random int range wont include the very right side column
        
        xtrange = random.randint(1,x - xtower) #make sure the range is at least 1. x will always be bigger than xtower by 1
        ytrange = random.randint(1,y - ytower) #y range version of above
        
        #add footprint to coverage map
        print("xtower:%s ytower:%s xrange:%s yrange:%s" % (xtower, ytower, xtrange, ytrange))
        
        for j in range(xtrange):
            for k in range(ytrange):
                if temp_coverage[xtower + j][ytower + k] != 1: #if it isnt already covered
                    temp_coverage[xtower + j][ytower + k] = 1 # add it to the coverage

                    trimmed[i].append([xtower+j,ytower+k]) #also add this to the trimmed 2d list so we can calculate max-area
                else:
                    overlap[i].append((xtower+j,ytower+k)) #not really necessary, but good way to cross-check
                    #this is just a 2d list that has the initial overlap of each tower.

        for j in trimmed: #loop through trimmed, a list of lists of list(x,y)
            for k in j:
                nptrimmed[k[0]][k[1]] = 1
                #botright = j[-1-bruteItr]
                #topright = j[0]
                #if block == 0:
                #    nptrimmed[k[0]][k[1]] = 1
                #    for z in range(botright[0],topright[0]-1,-1):
                #        for w in range(botright[1], topright[1] - 1,-1):
                #            print(z,w)
                #            print("valus")
                #            if nptrimmed[z][w] == 1:
                #                print("path")
                #                recttrimmed[z][w] = 1
                #            else:
                #                recttrimmed.fill(0)
                #    block = 1
                #    print("recttrimmed:")
                #    print(recttrimmed)
                
                #bruteItr = bruteItr + 1
            #bruteItr = 0 
            print("Trimmed Tower #: {} Trimmed Range: {}".format(trimItr, j))
            print(nptrimmed)
            
            #find the maximum area for each trimmed tower/range
            
            
            trimItr += 1
            nptrimmed.fill(0)
            
        trimItr = 0        
                    
        print("overlap: %s" % overlap)
        #print("trimmed: %s" % trimmed)
        #print("cov:")
        #print(temp_coverage)
        #print("trimmed cov: ")
        #print(nptrimmed)
    return temp_coverage
        #find overlaps and trim
        
#this is for finding maximum rectangle, this method finds the maximum histogram given a row of an array
#where each value in the array is the height of a bar in the histogram
#n is a row of an array
def max_histogram(n, arr):
    i = 0 #loop iterator
    area = 0 # final area
    temp = 0 # for checking if newly calculated area is larger
    stack = [] #using list as stack for algorithm
    ay = ()
    
    while i < n.size:
        if not stack:
            stack.append(i) #append iterator if stack is empty
            i = i + 1
        else:
            if n[i] >= n[stack[-1]]: #if array value is larger or equal to the top of the stack(end of list) append
                stack.append(i)
                i = i + 1
            else:
                val = stack.pop() # if array value is less pop the value and calculate an area
                if not stack:
                    temp = n[val] * i
                    
                else:
                    temp = n[val] * (i - stack[-1] - 1)
                    print(i,temp)
        if temp > area: # for seeing if area is actually larger
            area = temp
            
    while len(stack) > 0: #after reaching the end of the array, pop the rest of the values and calculate each area
        val = stack.pop()
        if len(stack) == 0:
            temp = n[val] * i 
        else:
            temp = n[val] * (i - stack[-1] - 1)
        if temp > area:
            area = temp
            
    return area

#uses above max_histogram to find maximum area of 1s in a 2d array
#n is the 2d array
def max_rectangle(n):
    temp = 0
    area = 0
    i = 1
    topleft = ()
    botright = ()
    
    row = n[0,:]
    area = max_histogram(row) #use above method to find area of a histogram for this row
    
    while i < n.shape[0]:
        for j in range(n.shape[1]):
            if(n[i][j] == 1):
                n[i][j] = n[i][j] + n[i-1][j] #create the added array
        temp = max_histogram(n[i,:]) # loop and calculate area
        if temp > area:
            area = temp
            
        i = i + 1
        
    return area

adhoc_network(5,5,10)
        

