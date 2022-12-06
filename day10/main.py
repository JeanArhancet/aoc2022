def day10_1():
    with open("input.txt") as f:
        input = f.read().split("\n")
        value = 1
        cycles = [1]
        for op in input:
            match op.split():
                case ["noop"]:
                    cycles.append(value)
                case ["addx", v]:
                    cycles.append(value)
                    value += int(v)
                    cycles.append(value)
        return(sum([i * cycles[i-1] for i in [20, 60, 100, 140, 180, 220]]))

def day10_2():
    with open("input.txt") as f:
        input = f.read().split("\n")
        value = 1
        cycles = [1]
        line = 40
        res = []
        for op in input:
            match op.split():
                case ["noop"]:
                    cycles.append(value)
                case ["addx", v]:
                    cycles.append(value)
                    value += int(v)
                    cycles.append(value)
        crt = ['#'  if abs(pos - (i % line)) <= 1 else '.' for i, pos in enumerate(cycles)]
        for i in range(0, len(cycles) // line):
            res.append(''.join(crt[i * line:(i + 1) * line]))
        return res
        


if __name__ == "__main__":
    print(day10_1())
    lines = day10_2()
    for line in lines:
        print(line)
   