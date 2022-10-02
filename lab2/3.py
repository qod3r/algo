import turtle
import random


def tree(branchLen, t):
    if branchLen > 5:
        # 1
        t.pensize(branchLen/8)
        
        # 3
        angle = random.randint(15, 45)
        
        # 4
        length = random.randint(8, 22)
        
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen - length, t)
        t.left(angle * 2)
        tree(branchLen - length, t)
        t.right(angle)
        t.backward(branchLen)
        
        # 2
        t.color("brown")
    else:
        t.color("green")


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75, t)
    myWin.exitonclick()

if __name__ == "__main__":
    main()
