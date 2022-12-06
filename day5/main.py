import re

from collections import deque

board = []


def read_line_board(line):
    lines_board = line.split(" ")
    count_escape = 0
    index = 0

    for line_board in lines_board:
        if line_board.isdigit():
            break

        if index >= len(board):
            board.append(deque())

        if line_board == "":
            count_escape += 1
        else:
            board[index].append(line_board)
            index += 1

        if count_escape == 4:
            count_escape = 0
            index += 1


def read_line_move(move, reverse=False):
    parts = re.findall(r"\d+", move)
    length = int(parts[0])
    origin = int(parts[1]) - 1
    dest = int(parts[2]) - 1
    tmp_array = [0] * length
    for i in range(length):
        if board[origin]:
            tmp = board[origin].popleft()
            tmp_array[i] = tmp
    if reverse:
        tmp_array.reverse()
    for i in range(length):
        board[dest].appendleft(tmp_array[i])


def day5_1():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for line in lines:
            if "move" in line:
                read_line_move(line, False)
            else:
                read_line_board(line)
        res = [re.match(r"[^[]*\[([^]]*)\]", x.popleft()).groups()[0] for x in board]
        return "".join(res)


def day5_2():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for line in lines:
            if "move" in line:
                read_line_move(line, True)
            else:
                read_line_board(line)
        res = [re.match(r"[^[]*\[([^]]*)\]", x.popleft()).groups()[0] for x in board]
        return "".join(res)


if __name__ == "__main__":
    print(day5_1())
    board = []
    print(day5_2())
