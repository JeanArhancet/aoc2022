def day6_1():
    res = []
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for line in lines:
            tmp = 0
            for i in range(len(line)):
                marker = list(set(line[i : i + 4]))
                if len(marker) == 4:
                    tmp = i + 4
                    break
            res.append(tmp)
        return res


def day6_2():
    res = []
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for line in lines:
            tmp = 0
            for i in range(len(line)):
                marker = list(set(line[i : i + 14]))
                if len(marker) == 14:
                    tmp = i + 14
                    break
            res.append(tmp)
        return res


if __name__ == "__main__":
    print(day6_1())
    print(day6_2())
