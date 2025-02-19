import turtle

pen = turtle.Turtle()  # Create the turtle object

def draw_star(size):
    for _ in range(5):  # Loop to draw 5 sides
        pen.forward(size)  # Move forward
        pen.right(144)  # Turn right 144 degrees

if __name__ == '__main__':
    turtle.bgcolor("white")  # Set background color
    pen.pencolor("blue")  # Set pen color
    pen.speed(3)  # Set turtle speed
    draw_star(150)  # Draw a star with size 150
    pen.hideturtle()  # Hide the turtle after drawing
    turtle.done()  # Keep the drawing window open
