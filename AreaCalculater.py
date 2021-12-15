'''
A function to calculate the area of a piece of land in acres given its length and width
'''
def calculate_area_in_acres(length, width):    
    area = (length * width)/43560
    return area