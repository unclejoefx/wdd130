"""The previous lesson’s prove milestone required you to write a program named tire_volume.py
 that computes the approximate volume of air inside a tire. Add code near the end of that program 
 that does the following:
Gets the current date from the computer’s operating system.
Opens a text file named volumes.txt for appending.
Appends to the end of the volumes.txt file one line of text that contains the following five values:
current date width of the tire aspect ratio of the tire diameter of the wheel volume of the tire"""

#previous lesson on milestone

#Import math to call the built-in functions for the maths to be done
#Also, Import the datetime class from the datetime
import math 
from datetime import datetime 
#defining variables using input function
print() #for spacing
width = int(input("Enter the width of the tire in mm: "))
aspect_ratio = int(input("Enter the aspect ratio of the tire: "))
diameter = int(input("Enter the diameter of the wheel in inches: "))


#carry out the arithemetric
pi = math.pi
volume = (pi * width**2 * aspect_ratio)
second_half =((width * aspect_ratio) + 2540  * diameter)
final_result = (volume*second_half/10000000000)
print()
print(f"The approximate volume is {final_result:.2f} liters" ) #round my final_result to 2dp by applying :.2f
#End of previous lesson on milestone


#Prove 02 starts here inorder to complete the milestone lesson

# Call the now() method to get the current
# date and time as a datetime from my OS
current_date_and_time = datetime.now()
print(current_date_and_time)
#Open text file named volumes.txt for appending and print it out.
with open("volumes.txt", mode='at') as tire_volume:
    print(file=tire_volume) 
    #use .format() to  my final_result formatted and print everything out.
    print(f"{current_date_and_time}, {width}, {aspect_ratio}, {diameter}, {'{:.2f}'.format(final_result)}", file=tire_volume)
    