import turtle

def draw_circle(x, y, radius, turtle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)

def sierpinski_circle(x, y, radius, depth, turtle):
    if depth == 0:
        draw_circle(x, y, radius, turtle)
    else:
        sierpinski_circle(x, y, radius/2, depth-1, turtle)
        sierpinski_circle(x+radius/2, y, radius/2, depth-1, turtle)
        sierpinski_circle(x, y+radius/2, radius/2, depth-1, turtle)

def main():
    myturtle = turtle.Turtle()
    myturtle.speed(0)
    myWin = myturtle.Screen()
    sierpinski_circle(0, 0, 200, 4, myturtle)
    myturtle.hideturtle()
    myWin.exitonclick()

main()
