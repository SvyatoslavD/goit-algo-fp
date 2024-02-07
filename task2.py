import turtle


def draw_pifagor_tree(t, branch_length, level):
    if level == 0:
        return

    t.forward(branch_length * level)
    t.right(45)
    draw_pifagor_tree(t, branch_length, level-1)
    t.left(90)
    draw_pifagor_tree(t, branch_length, level-1)
    t.right(45)
    t.backward(branch_length * level)


if __name__ == "__main__":
    level = int(input("Рівень рекурсії: "))

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.left(90)
    draw_pifagor_tree(t, 10, level)

    screen.mainloop()
