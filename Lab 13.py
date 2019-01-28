#!/usr/bin/env python3

# a_list is the ORIGINAL LIST
a_list = [1, 2, 3, 4]
print("The original list. . .")
print(a_list)
print()                                  # This simply prints an empty line (more below)

# Print out the elements in the original list
print("Item 1 in the list is: " , a_list[0])  # Stored at index 0
print("Item 2 in the list is: " , a_list[1])  # Stored at index 1
print("Item 3 in the list is: " , a_list[2])  # Stored at index 2
print("Item 4 in the list is: " , a_list[3])  # Stored at index 3
print()

##############################################################################
# reversed_list is the ORIGINAL LIST, reversed
# . . . It starts at the LAST element of the list, which is indicated by -1
# . . . It steps backward through the list, which is also indicated by -1
# . . . [-1::-1] means start at index -1,  iterate through all items,  but step backward by 1
# . . . [ 1:3:1] would mean start at index 1, end at index 3, step by 1   (This would be 2,3,4)
# . . . [begin:end:step]
#############################################################################
reversed_list = a_list[-1::-1]
print("The reversed list . . .")
print(reversed_list)
print()

print("Now using the FOR loop to maneuver the entire list")
for x in reversed_list:                    # We can name the variable anything we want
   print(x, " ", end="")                   # This will print the reversed list Horizontally
   #print(x)                               # The variable "x" is called in the print statement
#  END of the FOR loop