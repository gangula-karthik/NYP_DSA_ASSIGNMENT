# NAME: GANGULA KARTHIK 
# ADMISSION_NO: 223715Y
# TUTORIAL_GROUP: BA2202
############################################################################################################

import turtle
import random 
import colorsys


def drawCircle(center_x, center_y, radius, myTurtle):
    myTurtle.up()
    myTurtle.goto(center_x, center_y)
    myTurtle.down()
    myTurtle.circle(radius)


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


def sierpinski_circles(center_x, center_y, radius, degree, myTurtle, color_list):
    # Set the color of the turtle based on the degree of recursion
    myTurtle.fillcolor(color_list[degree % len(color_list)])
    myTurtle.begin_fill() # Begin filling the circle with the color
    # Draw the big circle
    drawCircle(center_x, center_y, radius, myTurtle)
    myTurtle.end_fill() # End filling the circle with the color
    if degree > 0:
        # Draw 3 smaller circles with the same center and radius * 0.5
        sierpinski_circles(center_x + radius / 2, center_y, radius * 0.5, degree-1, myTurtle, color_list)
        sierpinski_circles(center_x - radius / 2, center_y, radius * 0.5, degree-1, myTurtle, color_list)
        sierpinski_circles(center_x, center_y + radius / 2, radius * 0.5, degree-1, myTurtle, color_list)


def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.screensize(700,500)
    color_list = initialize_color_list()
    myTurtle.pencolor(color_list[0])
    myTurtle.penup()
    myTurtle.setpos(0,0)
    myTurtle.pendown()
    radius = 150
    degree = 0
    sierpinski_circles(0, 0, radius, degree, myTurtle, color_list)
    myTurtle.hideturtle()
    myWin.exitonclick()


main()


# def sierpinski(points,degree,myTurtle,diameter,number):
#     list_of_colours=['blue','red','green','cyan','yellow','pink','white','black']
#     pi = 3.14159265

#     small_radius=(diameter/(1+2**(1/2)))
#     positoning = (2 ** (1 / 2)) * small_radius / 2
#     r = diameter/2
#     new_diameter=small_radius+2


#     drawCircle(points,myTurtle,list_of_colours[degree],r)

#     if degree>0:
#         if number == 1 or (number-1)%4 == 0 :
#             sierpinski([
#                 [-(small_radius+points[1][0])/2,points[1][1]],
#                 [(small_radius+points[1][0]),points[1][1]+small_radius/2],

#             ],
#                        degree-1, myTurtle,new_diameter,number+1

#             )
#             sierpinski([
#                 [(small_radius-points[1][0])/2, points[1][1]],
#                 [-(small_radius-points[1][0]), points[1][1]+small_radius/2],
#             ],
#                 degree - 1, myTurtle, new_diameter,number+1

#             )
#             sierpinski([
#                 [(small_radius-points[1][0])/2, points[1][1]-small_radius],
#                 [-(small_radius-points[1][0]), points[1][1]-small_radius/2 ],
#             ],
#                 degree - 1, myTurtle, new_diameter,number+1

#             ) 
#         elif number == 2 or number%4!=0:



#             sierpinski([
#                 [(small_radius-points[1][0])/2, points[1][1]],
#                 [-(small_radius-points[1][0]), points[1][1]+small_radius/2],
#             ],
#                 degree - 1, myTurtle, new_diameter,number+1

#             )
#             sierpinski([
#                 [(small_radius-points[1][0])/2, points[1][1]-small_radius],
#                 [-(small_radius-points[1][0]), points[1][1]-small_radius/2 ],
#             ],
#                 degree - 1, myTurtle, new_diameter,number+1

#             )
#             sierpinski([
#                 [-(small_radius+points[1][0])/2,points[1][1]-small_radius],
#                 [(small_radius+points[1][0]), points[1][1]-small_radius/2 ],

#             ],
#                        degree-1, myTurtle,new_diameter,number+1
#             )
#         elif number == 3 or (number-4)%3 ==0:
#             sierpinski([
#                 [-(small_radius+points[1][0])/2,points[1][1]],
#                 [(small_radius+points[1][0]),points[1][1]+small_radius/2],

#             ],
#                        degree-1, myTurtle,new_diameter,number+1
#             )
#             sierpinski([
#                 [-(small_radius + points[1][0]) / 2, points[1][1]-small_radius],
#                 [-(small_radius - points[1][0]), points[1][1]-small_radius/2],

#             ],
#                 degree - 1, myTurtle, new_diameter,number+1
#             )
#             sierpinski([
#                 [(small_radius-points[1][0])/2, points[1][1]-small_radius],
#                 [-(small_radius-points[1][0]), points[1][1]-small_radius/2 ],
#             ],
#                 degree - 1, myTurtle, new_diameter,number+1

#             )
#         elif number == 4 or (number/2)%2 == 0:
#             sierpinski([
#                 [-(small_radius+points[1][0])/2,points[1][1]],
#                 [(small_radius+points[1][0]),points[1][1]+small_radius/2],

#             ],
#                        degree-1, myTurtle,new_diameter,number+1

#             )
#             sierpinski([
#                 [(small_radius-points[1][0])/2, points[1][1]],
#                 [-(small_radius-points[1][0]), points[1][1]+small_radius/2],
#             ],
#                 degree - 1, myTurtle, new_diameter,number+1

#             )
#             sierpinski([
#                 [-(small_radius + points[1][0]) / 2, points[1][1]],
#                 [-(small_radius - points[1][0]), points[1][1]-small_radius/2],

#             ],
#                 degree - 1, myTurtle, new_diameter,number+1
#             )