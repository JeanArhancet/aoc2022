import collections

f = lambda x: ord(x) if x not in "SE" else ord("a") if x == "S" else ord("z")


def bfs(grid, start, end):
    width, height = len(grid), len(grid[0])
    queue = collections.deque([[start]])
    goal = grid[end[0]][end[1]]
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[x][y] == goal:
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (
                0 <= x2 < width
                and 0 <= y2 < height
                and (f(grid[x2][y2]) - f(grid[x][y])) < 2
                and (x2, y2) not in seen
            ):
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return None


def day12_1():
    with open("input.txt") as f:
        grid = [list(row) for row in f.read().splitlines()]
        start, end = (0, 0), (0, 0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "S":
                    start = (i, j)
                if grid[i][j] == "E":
                    end = (i, j)
        return len(bfs(grid, start, end)) - 1


def day12_2():
    with open("input.txt") as f:
        grid = [list(row) for row in f.read().splitlines()]
        end = (0, 0)
        starts = []
        res = []
        start, end = (0, 0), (0, 0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "S":
                    starts.append((i, j))
                if grid[i][j] == "a":
                    starts.append((i, j))
                if grid[i][j] == "E":
                    end = (i, j)
        for start in starts:
            path = bfs(grid, start, end)
            if path:
                res.append(len(path))
        return min(res) - 1


if __name__ == "__main__":
    print(day12_1())
    print(day12_2())
