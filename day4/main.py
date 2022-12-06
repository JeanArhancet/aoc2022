def day4_1():
    subset_count = 0
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for line in lines:
            first, second = line.split(",")
            first_range, second_range = first.split("-"), second.split("-")
            first_list, second_list = list(
                range(int(first_range[0]), int(first_range[1]) + 1)
            ), list(range(int(second_range[0]), int(second_range[1]) + 1))
            if all(item in second_list for item in first_list) or all(
                item in first_list for item in second_list
            ):
                subset_count += 1
    return subset_count


def day4_2():
    subset_count = 0
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for line in lines:
            first, second = line.split(",")
            first_range, second_range = first.split("-"), second.split("-")
            first_list, second_list = list(
                range(int(first_range[0]), int(first_range[1]) + 1)
            ), list(range(int(second_range[0]), int(second_range[1]) + 1))
            if any(item in second_list for item in first_list) or any(
                item in first_list for item in second_list
            ):
                subset_count += 1
    return subset_count


if __name__ == "__main__":
    print(day4_1())
    print(day4_2())
