import turtle as t


def branch(depth: int, length: float) -> None:
    """
    Рисует фрактал "Ветка".
    :param depth: Глубина рекурсии.
    :param length: Длина "Ствола".
    :return: None.
    """
    # Базовый случай - это "ствол", прямая линия.
    # Когда черепаха идёт задом (t.bk(len)) стрелка не меняет направления!!!
    if depth == 0:
        t.fd(length)
        t.bk(length)
        return

    t.fd(length)

    t.left(45)
    branch(depth - 1, 0.5 * length)
    t.right(45)

    t.right(45)
    branch(depth - 1, 0.5 * length)
    t.left(45)

    branch(depth - 1, 0.7 * length)
    t.bk(length)


if __name__ == '__main__':
    # t.tracer(0, 0)
    t.left(90)
    t.speed(0)
    branch(2, 100)
    # t.update()
    t.done()