import math
import turtle
import random
import colorsys


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


def drawCircle(points, myTurtle, colour, r):
    """
    Draws a filled circle on the screen using the turtle module.
    Parameters:
    - points (list): A list of two-element tuples representing the (x, y) coordinates of the center of the circle.
    - myTurtle (Turtle): A turtle object to draw the circle.
    - colour (str): The color to fill the circle with.
    - r (float): The radius of the circle.
    Returns:
    None
    """
    myTurtle.fillcolor(colour)
    myTurtle.up() # Pen up
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down() # Pen down
    myTurtle.begin_fill()
    myTurtle.circle(r)
    myTurtle.end_fill()


def sierpinski(points,degree,myTurtle,radius,number, color_list):

    small_radius = ( radius / (1 + math.sqrt(2)) )

    drawCircle(points,myTurtle,color_list[degree % len(color_list)],radius/2)

    if degree>0:
        if number == 1 or (number-1)%4 == 0 :
            sierpinski([
                [-(small_radius+points[1][0])/2,points[1][1]],
                [(small_radius+points[1][0]),points[1][1]+small_radius/2]
            ],
                       degree-1, myTurtle,small_radius,number+1, color_list

            )
            sierpinski([
                [(small_radius-points[1][0])/2, points[1][1]],
                [-(small_radius-points[1][0]), points[1][1]+small_radius/2]
            ],
                degree - 1, myTurtle, small_radius,number+1, color_list

            )
            sierpinski([
                [(small_radius-points[1][0])/2, points[1][1]-small_radius],
                [-(small_radius-points[1][0]), points[1][1]-small_radius/2 ]
            ],
                degree - 1, myTurtle, small_radius,number+1, color_list

            )

        elif number == 2 or (number%4!=0 and number%2 ==0):
            sierpinski([
                [(small_radius-points[1][0])/2, points[1][1]],
                [-(small_radius-points[1][0]), points[1][1]+small_radius/2]
            ],
                degree - 1, myTurtle, small_radius,number+1, color_list

            )
            sierpinski([
                [(small_radius-points[1][0])/2, points[1][1]-small_radius],
                [-(small_radius-points[1][0]), points[1][1]-small_radius/2 ]
            ],
                degree - 1, myTurtle, small_radius,number+1, color_list

            )
            sierpinski([
                [-(small_radius+points[1][0])/2,points[1][1]-small_radius],
                [(small_radius+points[1][0]), points[1][1]-small_radius/2 ]

            ],
                       degree-1, myTurtle,small_radius,number+1, color_list
            )
        elif number == 3 or ((number-4)%3 ==0 and number %3==0):
            sierpinski([
                [-(small_radius+points[1][0])/2,points[1][1]],
                [(small_radius+points[1][0]),points[1][1]+small_radius/2]

            ],
                       degree-1, myTurtle,small_radius,number+1, color_list
            )
            sierpinski([
                [-(small_radius + points[1][0]) / 2, points[1][1]-small_radius],
                [(small_radius+points[1][0]),points[1][1]-small_radius/2]

            ],
                degree - 1, myTurtle, small_radius,number+1, color_list
            )
            sierpinski([
                [(small_radius-points[1][0])/2, points[1][1]-small_radius],
                [-(small_radius-points[1][0]), points[1][1]-small_radius/2 ]
            ],
                degree - 1, myTurtle, small_radius,number+1, color_list

            )

        elif number == 4 or (number/2)%2 == 0:

            sierpinski([
                [-(small_radius + points[1][0]) / 2, points[1][1]],
                [(small_radius+points[1][0]), points[1][1]+small_radius/2]

            ],
                degree - 1, myTurtle, small_radius,number+1, color_list
            )
            sierpinski([
                [-(small_radius + points[1][0]) / 2, points[1][1]-small_radius],
                [(small_radius+points[1][0]),points[1][1]-small_radius/2]
            ],
                degree - 1, myTurtle, small_radius, number + 1, color_list
            )
            sierpinski([
                [(small_radius - points[1][0]) / 2, points[1][1]],
                [-(small_radius - points[1][0]), points[1][1] + small_radius / 2]
            ],
                degree - 1, myTurtle, small_radius, number + 1,   color_list
            )



def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(0) 
    myWin = turtle.Screen()
    radius = 350
    color_list = initialize_color_list()
    myPoints = [[0,0],[0,radius/2]]
    degree = 3 # Vary the degree of complexity here
    number = 1
    # first call of the recursive function
    sierpinski(myPoints,degree,myTurtle,radius,number, color_list)
    myTurtle.hideturtle()
    myWin.exitonclick()


main()