import turtle as t
import tkinter as tk
from fractals.basic import draw_binary_tree, draw_branch
from fractals.complex import draw_ice_fractal_1, draw_ice_fractal_2, draw_levy
from fractals.koch import draw_koch, draw_koch_snowflake, draw_minkowski

def show_menu() -> None:
    print("=== ФРАКТАЛЬНАЯ МАСТЕРСКАЯ ===")
    print("1. Двоичное дерево")
    print("2. Фрактал 'Ветка'")
    print("3. Кривая Коха")
    print("4. Снежинка Коха")
    print("5. Кривая Минковского")
    print("6. Ледяной фрактал №1")
    print("7. Ледяной фрактал №2")
    print("8. Кривая Леви")
    print("9. Дракон Хартера-Хейтуэя")
    print("10. Выход")

def prepare() -> None:
    t.reset()
    t.speed(0)
    t.penup()
    t.goto(-400, -200)
    t.pendown()

def main() -> None:
    t.speed(100000000)

    try:
        while True:
            show_menu()
            choice = input('Выберите пункт меню: ')

            if choice == '10':
                break

            if choice == '9':
                print('Дракон сегодня заболел')

            try:
                prepare()

                if choice == '1':
                    t.setheading(90)
                    depth = int(input('Глубина рекурсии: '))
                    size = float(input('Длина стороны: '))
                    angle = float(input('Угол: '))
                    draw_binary_tree(depth, size, angle)

                if choice == '2':
                    t.setheading(90)
                    depth = int(input("Глубина рекурсии: "))
                    size = float(input("Длина стороны: "))
                    draw_branch(depth, size)

                elif choice == "3":
                    t.setheading(0)
                    order = int(input("Глубина рекурсии: "))
                    size = float(input("Длина стороны: "))
                    draw_koch(order, size)

                elif choice == "4":
                    t.setheading(0)
                    order = int(input("Глубина рекурсии: "))
                    size = float(input("Длина стороны: "))
                    draw_koch_snowflake(order, size)

                elif choice == "5":
                    t.setheading(0)
                    depth = int(input("Глубина рекурсии: "))
                    size = float(input("Длина стороны: "))
                    draw_minkowski(depth, size)

                elif choice == "6":
                    t.setheading(0)
                    order = int(input("Глубина рекурсии: "))
                    size = float(input("Длина стороны: "))
                    draw_ice_fractal_1(order, size)

                elif choice == "7":
                    t.setheading(0)
                    order = int(input("Глубина рекурсии: "))
                    size = float(input("Длина стороны: "))
                    draw_ice_fractal_2(order, size)

                elif choice == "8":
                    t.setheading(0)
                    depth = int(input("Глубина рекурсии: "))
                    size = float(input("Длина стороны: "))
                    draw_levy(depth, size)

                else:
                    print("Попробуйте снова.")

            except ValueError:
                print('Ошибка. Введите число')

    except KeyboardInterrupt:
        print("Программа остановлена пользователем.")
        return
    # Попытка работать с окном Turtle после того, как оно было закрыто
    except (t.Terminator, tk.TclError):
        print("Окно закрыто пользователем")
        return

    t.done()

if __name__ == '__main__':
    main()