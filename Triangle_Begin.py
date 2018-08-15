##Python program to determine the classification type of triangle
## by inputting 3 side lengths.
## Aug 2018

#TEST PLAN to run your program to check your code:

#test for first block
#i=0,j=0,k=0 -> if any side = 0 then 4, end program

#test for second block
#i=1,j=1,k=1 -> if all sides are same then 6
#i=1,j=2,k=3 -> if all sides diff then 0    
#i=1,j=1,k=2 -> 1
#i=1,j=2,k=1 -> 2
#i=2,j=1,k=1 -> 3
#i=2,j=2,k=1 -> 3

#test for third block when tri == 0:
#i=5,j=1,k=2 -> TRUE --> 4
#i=2,j=3,k=4 -> FALSE --> 1
#i=3,j=4,k=6 -> FALSE --> 1
#i=7,j=3,k=4 -> TRUE --> 4

#test for fourth block of code
#i=1,j=1,k=1 -> (Tri = 6) = 3
#i=2,j=2,k=3 -> (Tri == 1 and T) = 2
#i=2,j=3,k=2 -> (Tri == 2 and T) = 2
#i=1,j=2,k=2 -> (Tri == 3 and T) = 2
#i=2,j=1,k=1 -> (Tri == 3 and F) = 4


def triangle_classification_algorithm (i,j,k):
##enter code here:
    
    triangle = i + j + k
    return triangle 
     

##MAIN PROGRAM
    
#result table
# 1 --> scalene triangle
# 2 --> isosceles triangle
# 3 --> equilateral triangle
# 4 --> side lengths cannot form a triangle


i= int(input("Enter Lenght 1: "))
j= int(input("Enter Lenght 2: "))
k= int(input("Enter Lenght 3: "))


print (triangle_classification_algorithm (i,j,k))

print("End of script.")
