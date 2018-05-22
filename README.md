# ECE-143-Individual-Project
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
