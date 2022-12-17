def day15():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for line in lines:
            print(line)
    return "Hello World"


if __name__ == "__main__":
    print(day15())
