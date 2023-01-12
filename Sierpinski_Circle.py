
import turtle

def drawCircle(points,myTurtle,colour,r):
    myTurtle.fillcolor(colour)
    myTurtle.up() # Pen up
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down() # Pen down
    myTurtle.begin_fill()
    myTurtle.circle(r)
    myTurtle.end_fill()





def sierpinski(points,degree,myTurtle,diameter,number):
    list_of_colours=['blue','red','green','cyan','yellow','pink','white','black']

    small_radius=(diameter/(1+2**(1/2)))
    r = diameter/2
    new_diameter=small_radius+2


    drawCircle(points,myTurtle,list_of_colours[degree],r)

    if degree>0:
        if number == 1 or (number-1)%4 == 0 :
            sierpinski([
                [-(small_radius+points[1][0])/2,points[1][1]],
                [(small_radius+points[1][0]),points[1][1]+small_radius/2],

            ],
                       degree-1, myTurtle,new_diameter,number+1

            )
            sierpinski([
                [(small_radius-points[1][0])/2, points[1][1]],
                [-(small_radius-points[1][0]), points[1][1]+small_radius/2],
            ],
                degree - 1, myTurtle, new_diameter,number+1

            )
            sierpinski([
                [(small_radius-points[1][0])/2, points[1][1]-small_radius],
                [-(small_radius-points[1][0]), points[1][1]-small_radius/2 ],
            ],
                degree - 1, myTurtle, new_diameter,number+1

            )

        elif number == 2 or (number%4!=0 and number%2 ==0):



            sierpinski([
                [(small_radius-points[1][0])/2, points[1][1]],
                [-(small_radius-points[1][0]), points[1][1]+small_radius/2],
            ],
                degree - 1, myTurtle, new_diameter,number+1

            )
            sierpinski([
                [(small_radius-points[1][0])/2, points[1][1]-small_radius],
                [-(small_radius-points[1][0]), points[1][1]-small_radius/2 ],
            ],
                degree - 1, myTurtle, new_diameter,number+1

            )
            sierpinski([
                [-(small_radius+points[1][0])/2,points[1][1]-small_radius],
                [(small_radius+points[1][0]), points[1][1]-small_radius/2 ],

            ],
                       degree-1, myTurtle,new_diameter,number+1
            )
        elif number == 3 or ((number-4)%3 ==0 and number %3==0):
            sierpinski([
                [-(small_radius+points[1][0])/2,points[1][1]],
                [(small_radius+points[1][0]),points[1][1]+small_radius/2],

            ],
                       degree-1, myTurtle,new_diameter,number+1
            )
            sierpinski([
                [-(small_radius + points[1][0]) / 2, points[1][1]-small_radius],
                [(small_radius+points[1][0]),points[1][1]-small_radius/2],

            ],
                degree - 1, myTurtle, new_diameter,number+1
            )
            sierpinski([
                [(small_radius-points[1][0])/2, points[1][1]-small_radius],
                [-(small_radius-points[1][0]), points[1][1]-small_radius/2 ],
            ],
                degree - 1, myTurtle, new_diameter,number+1

            )

        elif number == 4 or (number/2)%2 == 0:

            sierpinski([
                [-(small_radius + points[1][0]) / 2, points[1][1]],
                [(small_radius+points[1][0]), points[1][1]+small_radius/2 ],

            ],
                degree - 1, myTurtle, new_diameter,number+1
            )
            sierpinski([
                [-(small_radius + points[1][0]) / 2, points[1][1]-small_radius],
                [(small_radius+points[1][0]),points[1][1]-small_radius/2],

            ],
                degree - 1, myTurtle, new_diameter, number + 1

            )
            sierpinski([
                [(small_radius - points[1][0]) / 2, points[1][1]],
                [-(small_radius - points[1][0]), points[1][1] + small_radius / 2],
            ],
                degree - 1, myTurtle, new_diameter, number + 1

            )



def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(1000) # adjust the drawing speed here
    myWin = turtle.Screen()
    diameter = 300
    myPoints = [[0,0],[0,diameter/2 ]]
    degree = 3 # Vary the degree of complexity here
    number = 1
# first call of the recursive function
    sierpinski(myPoints,degree,myTurtle,diameter,number)
    myTurtle.hideturtle()# hide the turtle cursor after drawing is
# completed
    myWin.exitonclick() # Exit program when user click on window
main()