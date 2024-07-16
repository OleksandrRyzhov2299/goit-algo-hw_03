import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def main():
    screen = turtle.Screen()
    screen.title("Сніжинка Коха")
    screen.setup(800, 600)
    screen.bgcolor("black")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("white")
    t.penup()
    t.goto(-300, 173)
    t.pendown()
    
    size = 600
    order = int(input("Введіть рівень рекурсії (рекомендовано 0-5): "))
    
    # Створення сніжинки Коха
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
