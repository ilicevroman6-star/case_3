import turtle as t


def draw_koch(order: int, size: float) -> None:
    """
    Рисует кривую "Коха".
    :param order: Глубина рекурсии.
    :param size: Длина отрезка.
    :return: None.
    """
    if order == 0:
        t.fd(size)
    else:
        draw_koch(order - 1, size / 3)
        t.left(60)
        draw_koch(order - 1, size / 3)
        t.right(120)
        draw_koch(order - 1, size / 3)
        t.left(60)
        draw_koch(order - 1, size / 3)


def draw_koch_snowflake(order: int, size: float) -> None:
    """
    Рисует "Снежинку Коха".
    :param order: Глубина рекурсии.
    :param size: Длина рекурсии.
    :return: None.
    """
    for _ in range(3):
        draw_koch(order, size)
        t.right(120)


def draw_minkowski(depth: int, length: float) -> None:
    """
    Рисует фрактал "Кривая Минковского".
    :param depth: Глубина рекурсии.
    :param length: Длина отрезка.
    :return: None.
    """
    if depth == 0:
        t.fd(length)
        return
    # Отрезок делим на 4 части. Длина одного отрезка - 1/4.
    # При снижении глубины рекурсии на 1 длина сокращается в 1/4 раза.
    draw_minkowski(depth - 1, 0.25 * length)
    t.left(90)
    draw_minkowski(depth - 1, 0.25 * length)
    t.right(90)
    draw_minkowski(depth - 1, 0.25 * length)
    t.right(90)
    draw_minkowski(depth - 1, 0.25 * length)
    draw_minkowski(depth - 1, 0.25 * length)
    t.left(90)
    draw_minkowski(depth - 1, 0.25 * length)
    t.left(90)
    draw_minkowski(depth - 1, 0.25 * length)
    t.right(90)
    draw_minkowski(depth - 1, 0.25 * length)


if __name__ == "__main__":
    t.tracer(0, 0)
    # t.speed(0)
    draw_koch(2, 100)
    draw_koch_snowflake(2, 100)
    draw_minkowski(4, 400)
    t.update()
    t.done()
