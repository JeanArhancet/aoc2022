from itertools import zip_longest


def compare(a, b):
    if a is None:
        return -1
    elif b is None:
        return 1
    elif isinstance(a, int) and isinstance(b, int):
        return -1 if a < b else 1 if b < a else 0
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    else:
        for x, y in zip_longest(a, b):
            if (r := compare(x, y)) == 0:
                continue
            return r
        return 0


def day13_1():
    with open("input.txt") as f:
        pairs = f.read().split("\n\n")
        orders = 0
        for i, pair in enumerate(pairs):
            pair = pair.split()
            left, right = list(eval(pair[0])), list(eval(pair[1]))
            if compare(left, right) < 0:
                orders += i + 1

        return orders


def count_lower(packets, divider):
    return sum(compare(packet, divider) < 0 for packet in packets)


def day13_2():
    with open("input.txt") as f:
        pairs = [map(eval, x.split()) for x in f.read().split("\n\n")]
        packets = [x for y in pairs for x in y]
        decoder = (count_lower(packets, [[2]]) + 1) * (count_lower(packets, [[6]]) + 2)
        return decoder


if __name__ == "__main__":
    print(day13_1())
    print(day13_2())
