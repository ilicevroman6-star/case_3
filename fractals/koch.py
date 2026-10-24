import turtle as t


def minkowski(depth: int, length: float) -> None:
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
    minkowski(depth - 1, 0.25 * length)
    t.left(90)
    minkowski(depth - 1, 0.25 * length)
    t.right(90)
    minkowski(depth - 1, 0.25 * length)
    t.right(90)
    minkowski(depth - 1, 0.25 * length)
    minkowski(depth - 1, 0.25 * length)
    t.left(90)
    minkowski(depth - 1, 0.25 * length)
    t.left(90)
    minkowski(depth - 1, 0.25 * length)
    t.right(90)
    minkowski(depth - 1, 0.25 * length)


if __name__ == "__main__":
    t.tracer(0, 0)
    # t.speed(0)
    minkowski(4, 400)
    t.update()
    t.done()