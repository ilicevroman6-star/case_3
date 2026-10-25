import turtle as t


def levy(depth: int, length: float) -> None:
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
    levy(depth - 1, 0.5 * length)
    t.right(90)
    levy(depth - 1, 0.5 * length)
    # Нужно добавить left, чтобы компенсировать 1ый left,
    # иначе будет создаваться лишний бугор.
    t.left(45)


if __name__ == "__main__":
    t.tracer(0, 0)
    # t.speed(0)
    levy(12, 10000)
    t.update()
    t.done()