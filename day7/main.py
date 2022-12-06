from __future__ import annotations

class Tree(object):
    def __init__(self, name: str, parents: Tree | None):
        self.name = name
        self.parents = parents or self
        self.files = {}
        self.children = {}

    def size(self):
        return sum(c.size() for c in self.children.values()) + sum(self.files.values())

    def recursive_children(self):
        return {self}.union(*(child.recursive_children() for child in self.children.values()))

def tree():
    with open("input.txt") as f:
        lines = f.readlines()
        cwd = root = Tree("/", None)
        for line in lines:
            match line.split():
                case ["$", "cd", ".."]:
                    cwd = cwd.parents
                case ["$", "cd", child]:
                    cwd = cwd.children.setdefault(child, Tree(child,cwd))
                    cwd.children[child] = Tree(child, cwd)
                case [size, name] if size.isdecimal():
                    cwd.files[name] = int(size)
        return root

if __name__ == "__main__":
    root = tree()
    day7_1 = sum(r.size() for r in root.recursive_children() if r.size() <= 100000)
    print(day7_1)
    day7_2 = root.size()
    size_treshold = 30000000 - 70000000 + day7_2
    for r in root.recursive_children():
        day7_2 = min(day7_2, r.size()) if r.size() >= size_treshold else day7_2 
    print(day7_2)
