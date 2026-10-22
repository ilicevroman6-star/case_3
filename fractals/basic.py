import turtle as t


def branch(depth: int, angle: int, distance=80):
    if depth == 0:
        t.left(90)
        t.fd(distance)
        t.home()
        return

    t.left(angle)
    t.fd(distance // (2 * depth))
    t.right(angle)
    branch(depth - 1, angle, distance)
    pass


if __name__ == '__main__':
    branch(12, 90)
    t.done()