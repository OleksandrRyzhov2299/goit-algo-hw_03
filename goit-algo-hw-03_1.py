import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            size /= 3
            koch_snowflake(t, order - 1, size)
            t.left(60)
            koch_snowflake(t, order - 1, size)
            t.right(120)
            koch_snowflake(t, order - 1, size)
            t.left(60)
            koch_snowflake(t, order - 1, size)
            t.left(angle)

def main():
    screen = turtle.Screen()
    screen.title("Сніжинка Коха")
    t = turtle.Turtle()
    t.speed(0)
    
    size = 300
    # Створення сніжинки Коха
    for _ in range(3):
        order = int(input("Введіть рівень рекурсії: "))
        koch_snowflake(t, order, size)
        t.right(120)
    screen.mainloop()

if __name__ == "__main__":
    main()