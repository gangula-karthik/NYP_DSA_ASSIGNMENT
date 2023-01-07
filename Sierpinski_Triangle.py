# NAME: GANGULA KARTHIK 
# ADMISSION_NO: 223715Y
# TUTORIAL_GROUP: BA2202
############################################################################################################

import turtle
import random 
import colorsys

def drawTriangle(points, myTurtle):
    myTurtle.up() # Pen up
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down() # Pen down
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])

def initialize_color_list():
    """
    Generates a list of 7 random colors in hexadecimal format, and ensures that the color is not repeated.

    Returns:
    list[str]: A list of 7 strings representing the hexadecimal values of the colors.
    """
    color_list = []
    for i in range(7):
        # Generate random HSL values
        h, s, l = (random.random() for _ in range(3))
        # Convert HSL to RGB values
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        # Convert RGB values to hexadecimal format
        color = '#%02x%02x%02x' % (int(r*255), int(g*255), int(b*255))
        # Add the colors to the list
        if color not in color_list:
            color_list.append(color)
    return color_list

def getMid(p1, p2):
    return ( (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, myTurtle, color_list):
    # Set the color of the turtle based on the degree of recursion
    myTurtle.fillcolor(color_list[degree % len(color_list)])
    myTurtle.begin_fill() # Begin filling the triangle with the color
    # Draw a triangle based on the 3 points given
    drawTriangle(points, myTurtle)
    myTurtle.end_fill() # End filling the triangle with the color
    
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                   degree-1, myTurtle, color_list)
        sierpinski([points[1],
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                   degree-1, myTurtle, color_list)
        sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                   degree-1, myTurtle, color_list)

def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(10) # adjust the drawing speed here
    myWin = turtle.Screen()
    # getting the colors for the triangles
    color_list = initialize_color_list()
    # 3 points of the first triangle based on [x,y] coordinates
    myPoints = [[-200, -50], [0, 200], [200, -50]]
    degree = 5 # Vary the degree of complexity here
    # first call of the recursive function
    sierpinski(myPoints, degree, myTurtle, color_list)
    myTurtle.hideturtle() # hide the turtle cursor after drawing is completed
    myWin.exitonclick() # Exit program when user click on window

main()