import turtle


def sierpinski(length, depth):
    if depth == 0:
        for _ in range(0, 3):
            t.forward(length)
            t.left(120)
    else:
        sierpinski(length / 2, depth - 1)
        t.forward(length / 2)
        sierpinski(length / 2, depth - 1)
        t.backward(length / 2)
        
        t.left(60)
        t.forward(length / 2)
        t.right(60)
        sierpinski(length / 2, depth - 1)
        
        t.left(60)
        t.backward(length / 2)
        t.right(60)


window = turtle.Screen()
window.setworldcoordinates(-1, -1, window.window_width() - 1, window.window_height() - 1)
t = turtle.Turtle()
sierpinski(800, 4)
window.exitonclick()