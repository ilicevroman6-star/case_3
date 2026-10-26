import turtle as t


def draw_binary_tree(depth: int, size: float, angle: float) -> None:
    """
    Рисует двоичное дерево.
    :param depth: Глубина рекурсии.
    :param size: Длина отрезка.
    :param angle: Угол.
    :return: None.
    """
    if depth == 0:
        return
    else:
        t.fd(size)
        t.right(angle)
        draw_binary_tree(depth - 1, size / 2, angle)
        t.left(2 * angle)
        draw_binary_tree(depth - 1, size / 2, angle)
        t.right(angle)
        t.backward(size)


def draw_branch(depth: int, length: float) -> None:
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
    draw_branch(depth - 1, 0.5 * length)
    t.right(45)

    t.right(45)
    draw_branch(depth - 1, 0.5 * length)
    t.left(45)

    draw_branch(depth - 1, 0.7 * length)
    t.bk(length)


if __name__ == '__main__':
    t.tracer(0, 0)
    t.left(90)
    # t.speed(0)
    draw_binary_tree(6, 100, 45)
    draw_branch(7, 100)
    t.update()
    t.done()
