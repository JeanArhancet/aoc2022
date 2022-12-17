start = (500, 0)


def create_matrix():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        matrix = {}
        min_y = 0
        for line in lines:
            coord = [tuple(map(int, point.split(","))) for point in line.split("->")]
            for i in range(len(coord) - 1):
                x1, y1, x2, y2 = *coord[i], *coord[i + 1]
                min_y = max(y1, y2, min_y)
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        matrix[x, y] = "#"
        return matrix, min_y


def day14():
    matrix, min_y = create_matrix()
    amount = 0
    part1 = 0
    floor = min_y + 2
    sand = None
    while sand != start:
        sand = start
        while True:
            y = sand[1] + 1
            for dx in 0, -1, 1:
                x = sand[0] + dx
                if y < floor and matrix.get((x, y), "") == "":
                    sand = x, y
                    break
            else:
                if not part1 and sand[1] > min_y:
                    part1 = amount
                matrix[sand] = "o"
                break
        amount += 1
    return part1, amount


if __name__ == "__main__":
    print(day14())
