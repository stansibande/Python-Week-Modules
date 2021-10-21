'''This Module containes functions that compute the areas of different shapes'''
# module name area
# disc - functions that compute areas of shapes

# square= a to the power 2
# circle +pie r square
# triangle =half base x height
# trapezium=half(a+b)h
# rectangle=length X width

def square(side):
    '''This Function Computes the area of a Square given the side Value'''
    area=side*side
    print ("The area of the square is ",area,"meters squared")
    
def circle(radius):
    '''This Function Computes the area Of A Circle Given The radius'''
    area=3.14*(radius*radius)
    print ("The area of the Circle is",area,"meters squared")

def triangle(base,height):
    '''This Function Computes area of a Triangle Given Base and Height'''
    area=0.5*(base*height)
    print ("The area of the Triangle is ", area,"meters squared")

def trapezium(abase,base,height):
    '''This Function Computes area of a Trapezium Given Top base, Bottom Base and Height'''
    area=0.5*((abase+base)*height)
    print ("The area of the Trapezium is ", area,"meters squared")
    
def rectangle(length,width):
     '''This Function Computes area of a Rectangle Given Length and Width'''
     area=length*width
     print("The area of the Rectangle is ",area,"meters squared")
    
    