import turtle as t


def draw_ice_fractal_1(order: int, size: float) -> None:
    """
    Рисует ледяной фрактал1
    :param order: Глубина рекурсии.
    :param size: Длина отрезка.
    :return: None.
    """
    if order == 0:
        t.forward(size)
        return

    draw_ice_fractal_1(order - 1, size / 2)

    t.left(90)
    draw_ice_fractal_1(order - 1, size / 4)
    t.left(180)
    draw_ice_fractal_1(order - 1, size / 4)

    t.left(90)

    draw_ice_fractal_1(order - 1, size / 2)


def draw_ice_fractal_2(order: int, size: float) -> None:
    """
    Рисует ледяной фрактал.
    :param order: Глубина рекурсии.
    :param size: Длина отрезка.
    :return: None.
    """
    if order == 0:
        t.fd(size)
        return

    draw_ice_fractal_2(order - 1, size)

    t.left(120)
    draw_ice_fractal_2(order - 1, size / 3)
    t.left(180)
    draw_ice_fractal_2(order - 1, size / 3)

    t.left(120)
    draw_ice_fractal_2(order - 1, size / 3)
    t.left(180)
    draw_ice_fractal_2(order - 1, size / 3)



    t.left(120)
    ice_fractal_2(order - 1, size)


def draw_levy(depth: int, length: float) -> None:
    """
    Рисует фрактал "Кривая Леви".
    :param depth: Глубина рекурсии.
    :param length: Длина отрезка.
    :return: None.
    """
    if depth == 0:
        t.fd(length)
        return
    t.left(45)
    draw_levy(depth - 1, 0.5 * length)
    t.right(90)
    draw_levy(depth - 1, 0.5 * length)
    # Нужно добавить left, чтобы компенсировать 1ый left,
    # иначе будет создаваться лишний бугор.
    t.left(45)


if __name__ == "__main__":
    t.tracer(0, 0)
    # t.speed(0)
    draw_ice_fractal_1(2,100)
    draw_ice_fractal_2(2, 100)
    draw_levy(12, 10000)
    t.update()
    t.done()
