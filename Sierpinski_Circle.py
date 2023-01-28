import math 
import time
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


def draw_circle(x, y, r, colour, turtle):
    """
    Draws a filled circle with the given radius, color and position using turtle

    Args:
    x (int): the x-coordinate of the center of the circle
    y (int): the y-coordinate of the center of the circle
    r (int): the radius of the circle
    colour (str): the color of the circle in hexadecimal format
    turtle (turtle.Turtle): the turtle object used to draw the circle
    """
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.fillcolor(colour)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def sierpinski_circle(turtle, big_r, degree, point, pattern, colors):
    """
    Draws the Sierpinski Circle fractal using turtle library

    Args:
    turtle (turtle.Turtle): the turtle object used to draw the fractal
    big_r (int): the radius of the big circle
    degree (int): the degree of recursion for the fractal
    point (list): the x, y coordinates of the center of the big circle
    pattern (dict): a dictionary containing the pattern of the fractal
    colors (list): a list of colors in hexadecimal format to fill the circles
    """
    draw_circle(point[0], point[1], big_r, colors[degree % len(colors)], turtle)
    small_r = big_r / (1 + math.sqrt(2))
    if degree > 0:
        quadrants = get_quadrants(point, small_r, big_r, pattern[degree])
        for quadrant in quadrants.values():
            draw_circle(quadrant[0], quadrant[1], small_r, colors[degree % len(colors)], turtle)
            sierpinski_circle(turtle, small_r, degree - 1, quadrant, pattern, colors)



def get_quadrants(point, small_r, big_r, pattern): 
    """
    Generates a dictionary of quadrants coordinates to be used in the Sierpinski Circle fractal

    Args:
    point (list): the x, y coordinates of the center of the big circle
    small_r (int): the radius of the small circles
    big_r (int): the radius of the big circle
    pattern (list): a list of integers representing the pattern of the fractal

    Returns:
    dict: A dictionary of quadrants coordinates {quadrant: (x,y)}
    """
    x, y = point
    quadrants = {
        "I": (x + small_r, y + big_r),
        "II": (x + small_r, y + big_r - (2 * small_r)), 
        "III": (x - small_r, y + big_r - (2 * small_r)), 
        "IV": (x - small_r, y + big_r)
    }
    quadrants = {quadrant: coordinates for quadrant, coordinates in quadrants.items() if pattern[list("I II III IV".split()).index(quadrant)] == 1}
    return quadrants



def pattern_gen(degree, pattern):
    """
    Generates the pattern for the Sierpinski Circle fractal
    Args:
    degree (int): the degree of recursion for the fractal
    pattern (List[int]): a list of integers representing the pattern of the fractal

    Returns:
    dict: A dictionary of patterns {degree: pattern}
    """
    patterns = {degree: pattern}
    for i in range(degree - 1, 0, -1):
        pos_init = lambda lst: lst.insert(0, lst.pop()) or lst
        patterns[i] = pos_init(patterns[i + 1].copy())
    return patterns





def main():
    st = time.time()
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.setup(width=1000, height=1000)
    myTurtle.speed(0)

    degree = 5
    big_R = 300
    point = [0, -250]
    myQueue = [1, 1, 0, 1]
    color_list = initialize_color_list()

    circlePattern = pattern_gen(degree, myQueue)

    sierpinski_circle(myTurtle, big_R, degree, point, circlePattern, color_list)
    et = time.time()

    print("elapsed time", et - st)
    myTurtle.hideturtle()
    myWin.exitonclick()
  

main()