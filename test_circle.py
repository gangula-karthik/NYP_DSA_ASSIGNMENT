import turtle
import mpmath as mp
import math

def drawCircle(points, myTurtle, color, radius):
    myTurtle.penup()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.pendown()
    myTurtle.color(color)
    myTurtle.begin_fill()
    myTurtle.circle(radius)
    myTurtle.end_fill()

def seirpinski(points, degree, myTurtle, diameter, number):
    list_of_colours = ['blue', 'red', 'green', 'cyan', 'yellow', 'pink', 'white', 'black']
    pi = 3.14159265

    small_radius = (diameter/2*(mp.csc(math.pi/4))) / (1 + mp.csc(math.pi/4))
    positoning = (2 ** (1 / 2)) * small_radius / 2
    r = diameter / 2
    new_diameter = small_radius + 2

    drawCircle(points, myTurtle, list_of_colours[degree], r)

    if degree > 0:
        if number == 1 or (number - 1) % 4 == 0:
            seirpinski([
                [-(small_radius + points[1][0]) / 2, points[1][1]],
                [(small_radius + points[1][0]), points[1][1] + small_radius / 2],

            ],
                degree - 1, myTurtle, new_diameter, number + 1

            )
            seirpinski([
                [(small_radius - points[1][0]) / 2, points[1][1]],
                [-(small_radius - points[1][0]), points[1][1] + small_radius / 2],
            ],
                degree - 1, myTurtle, new_diameter, number + 1

            )
            seirpinski([
                [points[1][0], points[1][1] + small_radius],
            ],
                degree - 1, myTurtle, new_diameter, number + 1

            )
        elif number == 2 or (number - 2) % 4 == 0:
            seirpinski([
                [-(small_radius + points[1][0]) / 2, points[1][1]],
                [(small_radius + points[1][0]), points[1][1] - small_radius / 2],

            ],
                degree - 1, myTurtle, new_diameter, number + 1

            )
            seirpinski([
                [(small_radius - points[1][0]) / 2, points[1][1]],
                [-(small_radius - points[1][0]), points[1][1] - small_radius / 2],
            ],
                degree - 1, myTurtle, new_diameter, number + 1
            )
        elif number == 3 or (number-4)%3 ==0:
            seirpinski([
                [-(small_radius+points[1][0])/2,points[1][1]],
                [(small_radius+points[1][0]),points[1][1]+small_radius/2],

            ],
                       degree-1, myTurtle,new_diameter,number+1
            )
            seirpinski([
                [-(small_radius + points[1][0]) / 2, points[1][1]-small_radius],
                [-(small_radius - points[1][0]), points[1][1]-small_radius/2],

            ],
                degree - 1, myTurtle, new_diameter,number+1
            )
            seirpinski([
                [(small_radius-points[1][0])/2, points[1][1]-small_radius],
                [-(small_radius-points[1][0]), points[1][1]-small_radius/2 ],
            ],
                degree - 1, myTurtle, new_diameter,number+1

            )
        elif number == 4 or (number/2)%2 == 0:
            seirpinski([
                [-(small_radius+points[1][0])/2,points[1][1]],
                [(small_radius+points[1][0]),points[1][1]+small_radius/2],

            ],
                       degree-1, myTurtle,new_diameter,number+1

            )
            seirpinski([
                [(small_radius-points[1][0])/2, points[1][1]],
                [-(small_radius-points[1][0]), points[1][1]+small_radius/2],
            ],
                degree - 1, myTurtle, new_diameter,number+1

            )
            seirpinski([
                [-(small_radius + points[1][0]) / 2, points[1][1]],
                [-(small_radius - points[1][0]), points[1][1]-small_radius/2],

            ],
                degree - 1, myTurtle, new_diameter,number+1
            )
        

def main():
    myTurtle = turtle.Turtle
    myWin = turtle.Screen()
    myTurtle.penup()
    myTurtle.setpos(0, 0)
    myTurtle.pendown()
    radius = 150
    degree = 0
    seirpinski([[0, 0], [0, 0]], degree, myTurtle, radius, 1)


if __name__ == '__main__':
    drawCircle([[0, 0], [0, 0]], turtle.Turtle(), 'red', 100)