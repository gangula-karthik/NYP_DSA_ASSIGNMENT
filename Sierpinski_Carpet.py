# NAME: GANGULA KARTHIK 
# ADMISSION_NO: 223715Y
# TUTORIAL_GROUP: BA2202
############################################################################################################

import turtle
import random 
import colorsys

def drawSquare(points, myTurtle):
    """
    Draws a square on the turtle's canvas.

    Parameters:
    points (list): A list of 2 lists, each containing an x,y coordinate. The first list represents the top-left corner of the square, and the second list represents the bottom-right corner of the square.
    myTurtle (turtle.Turtle): The turtle object used to draw the square.

    Returns:
    None
    """
    myTurtle.up() # Pen up
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down() # Pen down
    for i in range(4):
        myTurtle.forward(points[1][0] - points[0][0])
        myTurtle.left(90)

def initialize_color_list():
    """
    Generates a list of 7 random colors in hexadecimal format, and ensures that the color is not repeated.

    Returns:
    list[str]: A list of 7 strings representing the hexadecimal values of the colors.
    """
    color_list = set()
    for i in range(7):
        # Generate random HSL values
        h, s, l = (random.random() for _ in range(3))
        # Convert HSL to RGB values
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        # Convert RGB values to hexadecimal format
        color = '#%02x%02x%02x' % (int(r*255), int(g*255), int(b*255))
        # Add the colors to the list
        if color not in color_list:
            color_list.add(color)
    return list(color_list)

def getMid(p1, p2):
    """
    Calculates the midpoint between two points.

    Parameters:
    p1 (tuple): A tuple containing the x,y coordinates of the first point.
    p2 (tuple): A tuple containing the x,y coordinates of the second point.

    Returns:
    tuple: A tuple containing the x,y coordinates of the midpoint between p1 and p2.
    """
    return ( (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def draw_squares(points, degree, myTurtle, color_list):
    """
    Recursively draws a 3x3 grid of squares on the turtle's canvas, with the middle square left blank.

    Parameters:
    points (list): A list of 2 lists, each containing an x,y coordinate. The first list represents the top-left corner of the outermost square, and the second list represents the bottom-right corner of the outermost square.
    degree (int): The degree of recursion, or the number of times the squares will be divided.
    myTurtle (turtle.Turtle): The turtle object used to draw the squares.
    color_list (list[str]): A list of strings representing the hexadecimal values of the colors used to fill the squares.

    Returns:
    None
    """
    # Set the color of the turtle based on the degree of recursion
    myTurtle.fillcolor(color_list[degree % len(color_list)])
    myTurtle.begin_fill() # Begin filling the square with the color
    # Draw a square based on the 2 points given
    drawSquare(points, myTurtle)
    myTurtle.end_fill() # End filling the square with the color
    
    if degree > 0:
        # Divide the square into 9 smaller squares and draw them recursively
        size = points[1][0] - points[0][0]
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    # Skip the middle square
                    continue
                draw_squares([[points[0][0] + i*size/3, points[0][1] + j*size/3],
                              [points[0][0] + (i+1)*size/3, points[0][1] + (j+1)*size/3]],
                             degree-1, myTurtle, color_list)

def main():
    """
    Draws a 3x3 grid of squares using recursive functions and turtle graphics, with the middle square left blank. The squares are filled with random colors. The program exits when the user clicks on the window.

    Parameters:
    None

    Returns:
    None
    """
    myTurtle = turtle.Turtle()
    myTurtle.speed(0)
    myWin = turtle.Screen()
    myTurtle.speed(0)
    # getting the colors for the squares
    color_list = initialize_color_list()
    # 2 points of the first square based on [x,y] coordinates
    myPoints = [[-200, -200], [200, 200]]
    degree = 2 # Vary the degree of complexity here
    # first call of the recursive function
    draw_squares(myPoints, degree, myTurtle, color_list)
    myTurtle.hideturtle() # hide the turtle cursor after drawing is completed
    myWin.exitonclick() # Exit program when user click on window

main()