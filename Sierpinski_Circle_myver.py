# # # NAME: GANGULA KARTHIK
# # # ADMISSION_NO: 223715Y
# # # TUTORIAL_GROUP: BA2202
# # ############################################################################################################

# # import math
# # import turtle
# # import random
# # import colorsys


# # def initialize_color_list():
# #     """
# #     Generates a list of 7 random colors in hexadecimal format, and ensures that the color is not repeated.

# #     Returns:
# #     list[str]: A list of 7 strings representing the hexadecimal values of the colors.
# #     """
# #     color_list = set()
# #     for i in range(7):
# #         # Generate random HSL values
# #         h, s, l = (random.random() for _ in range(3))
# #         # Convert HSL to RGB values
# #         r, g, b = colorsys.hls_to_rgb(h, l, s)
# #         # Convert RGB values to hexadecimal format
# #         color = '#%02x%02x%02x' % (int(r*255), int(g*255), int(b*255))
# #         # Add the colors to the list
# #         if color not in color_list:
# #             color_list.add(color)
# #     return list(color_list)


# # def drawCircle(points, myTurtle, colour, radius):
# #     """
# #     Draws a filled circle on the screen using the turtle module.

# #     Parameters:
# #     - points (list): A list of two-element tuples representing the (x, y) coordinates of the center of the circle.
# #     - myTurtle (Turtle): A turtle object to draw the circle.
# #     - colour (str): The color to fill the circle with.
# #     - r (float): The radius of the circle.

# #     Returns:
# #     None
# #     """
# #     myTurtle.fillcolor(colour)
# #     myTurtle.up()  # Pen up
# #     myTurtle.goto(points[0][0], points[0][1])
# #     myTurtle.down()  # Pen down
# #     myTurtle.begin_fill()
# #     myTurtle.circle(radius)
# #     myTurtle.end_fill()


# # def sierpinski_circle(points, degree, myTurtle, big_R, turn_level, color_list):
# #     small_R = big_R / (1 + math.sqrt(2))
# #     # split the circle into 4 parts and get the coordinates 
# #     quadrants_coordinates = {
# #         "I": [points[0] + small_R, points[1] + big_R],
# #         "II": [points[0] + small_R, points[1] + big_R - (2 * small_R)], 
# #         "III": [points[0] - small_R, points[1] + big_R - (2 * small_R)], 
# #         "IV": [points[0] - small_R, points[1] + big_R]
# #     }
# #     # generating the drawing pattern using binary shift operation
# # a



# # def main():
# #     myTurtle = turtle.Turtle()
# #     myTurtle.speed(0)
# #     myWin = turtle.Screen()
# #     radius = 150
# #     color_list = initialize_color_list()
# #     myPoints = [0, 0]
# #     degree = 1  # Vary the degree of complexity here
# #     turn_level = 1
# #     # first call of the recursive function
# #     sierpinski_circle(myPoints, degree, myTurtle, radius, turn_level, color_list)
# #     myTurtle.hideturtle()
# #     myWin.exitonclick()


# # main()


# import math
# import turtle


# myPoints = [0, 0]
# big_R = 170

# myTurtle = turtle.Turtle()
# myTurtle.speed(0)
# myWin = turtle.Screen()
# myTurtle.circle(big_R)


# small_R = big_R / (1 + math.sqrt(2))

# quadrants_coordinates = {
#     "I": [myPoints[0] + small_R, myPoints[1] + big_R],
#     "II": [myPoints[0] + small_R, myPoints[1] + big_R - (2 * small_R)], 
#     "III": [myPoints[0] - small_R, myPoints[1] + big_R - (2 * small_R)], 
#     "IV": [myPoints[0] - small_R, myPoints[1] + big_R]
# }



# for i in range(2): 
#     if i == 1: 
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ1["I"][0], quadrants_coordinatesQ1["I"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ1["II"][0], quadrants_coordinatesQ1["II"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ1["III"][0], quadrants_coordinatesQ1["III"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ1["IV"][0], quadrants_coordinatesQ1["IV"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()
#     else:
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinates["I"][0], quadrants_coordinates["I"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)

#     if i == 1: 
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ2["I"][0], quadrants_coordinatesQ2["I"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ2["II"][0], quadrants_coordinatesQ2["II"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ2["III"][0], quadrants_coordinatesQ2["III"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ2["IV"][0], quadrants_coordinatesQ2["IV"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()
#     else:
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinates["II"][0], quadrants_coordinates["II"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)


#     if i == 1:
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ3["I"][0], quadrants_coordinatesQ3["I"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ3["II"][0], quadrants_coordinatesQ3["II"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ3["III"][0], quadrants_coordinatesQ3["III"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ3["IV"][0], quadrants_coordinatesQ3["IV"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()

#     else:
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinates["III"][0], quadrants_coordinates["III"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)


#     if i == 1:
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ4["I"][0], quadrants_coordinatesQ4["I"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ4["II"][0], quadrants_coordinatesQ4["II"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ4["III"][0], quadrants_coordinatesQ4["III"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinatesQ4["IV"][0], quadrants_coordinatesQ4["IV"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)
#     else:
#         myTurtle.penup()
#         myTurtle.setpos(quadrants_coordinates["IV"][0], quadrants_coordinates["IV"][1])
#         myTurtle.pendown()
#         myTurtle.circle(small_R)

#     big_R = small_R
#     small_R = big_R / (1 + math.sqrt(2))

#     if i == 0: 
#         mypointQ1 = [quadrants_coordinates["I"][0], quadrants_coordinates["I"][1]]
#         quadrants_coordinatesQ1 = {
#             "I": [mypointQ1[0] + small_R, mypointQ1[1] + big_R],
#             "II": [mypointQ1[0] + small_R, mypointQ1[1] + big_R - (2 * small_R)], 
#             "III": [mypointQ1[0] - small_R, mypointQ1[1] + big_R - (2 * small_R)], 
#             "IV": [mypointQ1[0] - small_R, mypointQ1[1] + big_R]
#         }

#         mypointQ2 = [quadrants_coordinates["II"][0], quadrants_coordinates["II"][1]]
#         quadrants_coordinatesQ2 = {
#             "I": [mypointQ2[0] + small_R, mypointQ2[1] + big_R],
#             "II": [mypointQ2[0] + small_R, mypointQ2[1] + big_R - (2 * small_R)], 
#             "III": [mypointQ2[0] - small_R, mypointQ2[1] + big_R - (2 * small_R)], 
#             "IV": [mypointQ2[0] - small_R, mypointQ2[1] + big_R]
#         }

#         mypointQ3 = [quadrants_coordinates["III"][0], quadrants_coordinates["III"][1]]
#         quadrants_coordinatesQ3 = {
#             "I": [mypointQ3[0] + small_R, mypointQ3[1] + big_R],
#             "II": [mypointQ3[0] + small_R, mypointQ3[1] + big_R - (2 * small_R)], 
#             "III": [mypointQ3[0] - small_R, mypointQ3[1] + big_R - (2 * small_R)], 
#             "IV": [mypointQ3[0] - small_R, mypointQ3[1] + big_R]
#         }

#         mypointQ4 = [quadrants_coordinates["IV"][0], quadrants_coordinates["IV"][1]]
#         quadrants_coordinatesQ4 = {
#             "I": [mypointQ4[0] + small_R, mypointQ4[1] + big_R],
#             "II": [mypointQ4[0] + small_R, mypointQ4[1] + big_R - (2 * small_R)], 
#             "III": [mypointQ4[0] - small_R, mypointQ4[1] + big_R - (2 * small_R)], 
#             "IV": [mypointQ4[0] - small_R, mypointQ4[1] + big_R]
#         }


import math 
import turtle

def pos_init(arr): 
    temp = arr.pop()
    if temp == 0: 
        arr.insert(0, 0)
    else: 
        arr.insert(0, 1)

    return arr

def drawCircle(x, y, r, myTurtle):
    myTurtle.penup()
    myTurtle.setpos(x, y)
    myTurtle.pendown()
    myTurtle.circle(r)

def sierpinski_circle(myTurtle, big_R, degree, points, myQueue):
    drawCircle(points[0], points[1], big_R, myTurtle)
    small_R = big_R / (1 + math.sqrt(2))
    if degree > 0: 
        quadrant = get_quad(points, small_R, big_R, myQueue)
    else:
        quadrant = {}
    for i in quadrant:
        drawCircle(quadrant[i][0], quadrant[i][1], small_R, myTurtle)
        if degree > 0:
            myQueue = pos_init(myQueue)
            sierpinski_circle(myTurtle, small_R, degree - 1, quadrant[i], myQueue)

def get_quad(points, small_R, big_R, myQueue): 
    x, y = points[0], points[1]
    quadrants_coordinates = {
        "I": [x + small_R, y + big_R],
        "II": [x + small_R, y + big_R - (2 * small_R)], 
        "III": [x - small_R, y + big_R - (2 * small_R)], 
        "IV": [x - small_R, y + big_R]
    }

    quadrants_to_remove = [quadrant for quadrant, value in quadrants_coordinates.items() if myQueue[list("I II III IV".split()).index(quadrant)] == 0]
    for quadrant in quadrants_to_remove:
        del quadrants_coordinates[quadrant]
    return quadrants_coordinates


def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myTurtle.speed(0)

    degree = 4
    big_R = 170
    point = [0, 0]
    myQueue = [1, 1, 0, 1]

    sierpinski_circle(myTurtle, big_R, degree, point, myQueue)

    myTurtle.hideturtle()
    myWin.exitonclick()
  

main()



# myTurtle.hideturtle()
# myWin.exitonclick()