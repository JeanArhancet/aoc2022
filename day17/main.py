# Found on reddit

import collections

shapes = [
    [[1, 1, 1, 1]],
    [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
    [[0, 0, 1], [0, 0, 1], [1, 1, 1]],
    [[1], [1], [1], [1]],
    [[1, 1], [1, 1]],
]

LEFT_DISTANCE = 2
HEIGHT_DISTANCE = 3
WIDTH = 7
MAX_ROCK_1 = 2022
MAX_ROCK_2 = 1000000000000


def collision(matrix, shape, x, y):
    for y2 in range(len(shape)):
        for x2 in range(len(shape[y2])):
            if shape[y2][x2] == 1 and matrix[y + y2][x + x2] == 1:
                return True
    return False


def drop(matrix):
    while all(cell == 0 for cell in matrix[0]):
        matrix.popleft()


def plot(matrix, shape, x, y):
    for y2 in range(len(shape)):
        for x2 in range(len(shape[y2])):
            if shape[y2][x2] == 1:
                matrix[y + y2][x + x2] = 1


def day17_1():
    with open("input.txt") as f:
        jets = f.read().splitlines()[0]
        matrix = collections.deque()
        matrix.append([1] * WIDTH)
        counter = 0
        shape = 0
        jet = 0
        seen = collections.defaultdict(list)
        while counter < min(MAX_ROCK_1, 10000):
            curr = shapes[shape]
            for _ in range(HEIGHT_DISTANCE + len(curr)):
                matrix.appendleft([0] * WIDTH)
            x = LEFT_DISTANCE
            y = 0
            while True:
                match jets[jet]:
                    case ">":
                        if x + len(curr[0]) < WIDTH:
                            if not collision(matrix, curr, x + 1, y):
                                x += 1
                    case "<":
                        if x > 0:
                            if not collision(matrix, curr, x - 1, y):
                                x -= 1
                jet = (jet + 1) % len(jets)
                if collision(matrix, curr, x, y + 1):
                    break
                y += 1

            plot(matrix, curr, x, y)
            counter += 1
            shape = (shape + 1) % len(shapes)
            drop(matrix)

            if len(matrix) > 20:
                matrix_top = tuple(
                    int("".join(map(str, matrix[i])), 2) for i in range(20)
                )
                key = (matrix_top, jet, shape)
                seen[key].append((counter, len(matrix) - 1))
                if len(seen[key]) > 1:
                    r1, h1 = seen[key][-2]
                    r2, h2 = seen[key][-1]
                    if (MAX_ROCK_1 - r1) % (r2 - r1) == 0:
                        result = (MAX_ROCK_1 - r1) // (r2 - r1) * (h2 - h1) + h1
                        return result
    return len(matrix) - 1


def day17_2():
    with open("input.txt") as f:
        jets = f.read().splitlines()[0]
        matrix = collections.deque()
        matrix.append([1] * WIDTH)
        counter = 0
        shape = 0
        jet = 0
        seen = collections.defaultdict(list)
        while counter < min(MAX_ROCK_2, 10000):
            curr = shapes[shape]
            for _ in range(HEIGHT_DISTANCE + len(curr)):
                matrix.appendleft([0] * WIDTH)
            x = LEFT_DISTANCE
            y = 0
            while True:
                match jets[jet]:
                    case ">":
                        if x + len(curr[0]) < WIDTH:
                            if not collision(matrix, curr, x + 1, y):
                                x += 1
                    case "<":
                        if x > 0:
                            if not collision(matrix, curr, x - 1, y):
                                x -= 1
                jet = (jet + 1) % len(jets)
                if collision(matrix, curr, x, y + 1):
                    break
                y += 1

            plot(matrix, curr, x, y)
            counter += 1
            shape = (shape + 1) % len(shapes)
            drop(matrix)

            if len(matrix) > 20:
                matrix_top = tuple(
                    int("".join(map(str, matrix[i])), 2) for i in range(20)
                )
                key = (matrix_top, jet, shape)
                seen[key].append((counter, len(matrix) - 1))
                if len(seen[key]) > 1:
                    r1, h1 = seen[key][-2]
                    r2, h2 = seen[key][-1]
                    if (MAX_ROCK_2 - r1) % (r2 - r1) == 0:
                        result = (MAX_ROCK_2 - r1) // (r2 - r1) * (h2 - h1) + h1
                        return result
    return len(matrix) - 1


if __name__ == "__main__":
    print(day17_1())
    print(day17_2())
