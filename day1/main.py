def day1_1():
    elfs = []
    elf = 0
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line == "":
                elfs.append(elf)
                elf = 0
            else:
                elf += int(line)
        return max(elfs)


def day1_2():
    elfs = []
    elf = 0
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line == "":
                elfs.append(elf)
                elf = 0
            else:
                elf += int(line)
        elfs.sort(reverse=True)
        return sum(elfs[:3])


if __name__ == "__main__":
    print(day1_1())
    print(day1_2())
