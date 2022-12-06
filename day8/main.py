import collections


def is_max(tree, list_tree):
    return True if len(list_tree) == 0 or tree > max(list_tree) else False


def day8_1():
    sum_tree_visible = 0
    with open("input.txt") as f:
        lines = f.read().splitlines()
        groupdict = collections.defaultdict(list)
        cols = len(lines)
        for line in lines:
            group = line[:cols]
            groupdict[group] = list(line)
        result = list(groupdict.values())
        for i in range(0, cols):
            for j in range(0, cols):
                current_row = result[i]
                pos_tree = result[i][j]
                current_colums = [result[c][j] for c in range(cols)]
                max_left_row = is_max(pos_tree, current_row[j + 1 :])
                max_right_row = is_max(pos_tree, current_row[:j][::-1])
                max_top_colums = is_max(pos_tree, current_colums[:i][::-1])
                max_down_colums = is_max(pos_tree, current_colums[i + 1 :])
                if (
                    sum([max_left_row, max_right_row, max_top_colums, max_down_colums])
                    > 0
                ):
                    sum_tree_visible += 1
        return sum_tree_visible


def count_tree_visible(tree, list_trees):
    count = 0
    for i in range(0, len(list_trees)):
        count += 1
        if int(tree) <= int(list_trees[i]):
            break
    return count


def day8_2():
    sum_tree_visible = 0
    with open("input.txt") as f:
        lines = f.read().splitlines()
        groupdict = collections.defaultdict(list)
        cols = len(lines)
        for line in lines:
            group = line[:cols]
            groupdict[group] = list(line)
        result = list(groupdict.values())
        for i in range(0, cols):
            for j in range(0, cols):
                current_row = result[i]
                pos_tree = result[i][j]
                current_colums = [result[c][j] for c in range(cols)]
                count_left_row = count_tree_visible(pos_tree,  current_row[j + 1 :])
                count_right_row = count_tree_visible(pos_tree,  current_row[:j][::-1])
                count_top_colums = count_tree_visible(pos_tree, current_colums[i + 1 :])
                count_down_colums = count_tree_visible(pos_tree, current_colums[:i][::-1])
                total = (
                    count_left_row
                    * count_right_row
                    * count_top_colums
                    * count_down_colums
                )
                if total > sum_tree_visible:
                    sum_tree_visible = total
        return sum_tree_visible


if __name__ == "__main__":
    print(day8_1())
    print(day8_2())
