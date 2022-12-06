def day3_1():
    score = 0
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for line in lines:
            middle = len(line) // 2
            firstpart, secondpart = line[:middle], line[middle:]
            find = list(set(firstpart).intersection(secondpart))[0]
            if find.isupper():
                score += int(ord(find) - 38)
            else:
                score += int(ord(find) - 96)
    return score


def day3_2():
    score = 0
    with open("input.txt", "r") as f:
        while True:
            lines = []
            for _ in range(3):
                try:
                    lines.append(
                        next(f).rstrip("\r\n")
                    )  # f.next() returns next line in file
                except StopIteration:  # this will happen if you reach end of file before finding 4 more lines.
                    # decide what you want to do here
                    return score

            find = list(set(lines[0]).intersection(lines[1]).intersection(lines[2]))[0]
            if find.isupper():
                score += int(ord(find) - 38)
            else:
                score += int(ord(find) - 96)


if __name__ == "__main__":
    print(day3_1())
    print(day3_2())
