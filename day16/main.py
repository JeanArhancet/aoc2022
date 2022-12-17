import functools
import re

valves = {}


@functools.cache
def dfs_1(opened, minute, valve):
    if minute <= 0:
        return 0
    rate = 0
    for neighbor in valves[valve]["valves"]:
        rate = max(rate, dfs_1(opened, minute - 1, neighbor))

    if valve not in opened and valves[valve]["rate"] > 0 and minute > 0:
        opened = set(opened)
        opened.add(valve)
        minute -= 1
        res = valves[valve]["rate"] * minute
        for v in valves[valve]["valves"]:
            rate = max(rate, res + dfs_1(frozenset(opened), minute - 1, v))

    return rate


@functools.cache
def dfs_2(opened, minute, valve):
    if minute <= 0:
        return dfs_1(frozenset(opened), 26, "AA")

    rate = 0
    for neighbor in valves[valve]["valves"]:
        rate = max(rate, dfs_2(opened, minute - 1, neighbor))

    if valve not in opened and valves[valve]["rate"] > 0 and minute > 0:
        opened = set(opened)
        opened.add(valve)
        minute -= 1
        res = valves[valve]["rate"] * minute
        for v in valves[valve]["valves"]:
            rate = max(rate, res + dfs_2(frozenset(opened), minute - 1, v))

    return rate


def day16_1():
    with open("input.txt") as f:
        lines = f.read().splitlines()

        opened = frozenset()
        global valves

        for line in lines:
            valves_matcher = re.compile(r"\b[A-Z]{2}\b")
            rate = int(re.findall(r"\d+", line)[0])
            parsing_valves = re.findall(valves_matcher, line)
            valve = parsing_valves.pop(0)
            valves[valve] = {"valves": parsing_valves, "rate": rate}

        return dfs_1(opened, 30, "AA")


def day16_2():
    with open("input.txt") as f:
        lines = f.read().splitlines()

        opened = frozenset()
        global valves

        for line in lines:
            valves_matcher = re.compile(r"\b[A-Z]{2}\b")
            rate = int(re.findall(r"\d+", line)[0])
            parsing_valves = re.findall(valves_matcher, line)
            valve = parsing_valves.pop(0)
            valves[valve] = {"valves": parsing_valves, "rate": rate}

        return dfs_2(opened, 26, "AA")


if __name__ == "__main__":
    print(day16_1())
    print(day16_2())
