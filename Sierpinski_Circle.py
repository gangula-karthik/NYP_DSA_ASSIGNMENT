import turtle 


def drawCircle(myRadius, myTurtle):
    """This function is used to actually draw each circle"""
    myTurtle.circle(myRadius) # Draw a circle with the given radius
    

def draw_circles(myRadius, degree, myTurtle):
    """This function is used to perform recursion"""
    
    if degree > 0:
        newRadius = (myRadius * (2 ** 0.5)) / (1 + (2 ** 0.5))
        for i in range(3):
            drawCircle(newRadius, myTurtle)
        draw_circles(newRadius, degree - 1, myTurtle) # Call the draw_circles function again
        

def main(): 
    """This function is used to call the draw_circles function and do initialization"""
    myWindow = turtle.Screen # Create a screen
    turtle.screensize(500, 500) # Set the screen size
    myTurtle = turtle.Turtle() # Create a turtle 
    myTurtle.home() # set the coordinates of the turtle to origin
    myTurtle.speed(6) # Set the speed of the turtle to 0
    # do something over here
    drawCircle(150, myTurtle) # Call the drawCircle function
    draw_circles(150, 2, myTurtle) # Call the draw_circles function


if __name__ == "__main__": 
    main()