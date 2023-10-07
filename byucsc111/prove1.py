import math
width = 185
aspect_ratio = 50
diametre = 14
pii = math.pi
result = pii * width**2 * aspect_ratio
second_half = (width * aspect_ratio) + 2540  * diametre 
final = round(result*second_half/10000000000,2)
print(final)

#get current time

# open a txt file with writing privilages
# put the required info in one string f{}
#append the new variab,e to the txt file
"""v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches."""