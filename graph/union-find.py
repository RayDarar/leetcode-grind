class UnionQuickFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]

    def find(self, x: int):
        return self.root[x]

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootX:
                    self.root[i] = rootX

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


class QuickUnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]

    def find(self, x: int):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.root[rootX] = rootY

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


class UnionByRank:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x: int):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)
