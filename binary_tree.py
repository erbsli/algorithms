def create_tree(l):
    root = Node(l[0], None, None)

    for i in range(1, len(l)):
        root.insert(l[i])

    return root



class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, v):
        if v == self.value:
            return False
        elif v < self.value:
            if self.left is None:
                self.left = Node(v, None, None)
                return True
            else:
                self.left.insert(v)
        else:
            if self.right is None:
                self.right = Node(v, None, None)
                return True
            else:
                self.right.insert(v)

    def find(self, v):
        if v == self.value:
            return True
        elif v < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(v)
        else:
            if self.right is None:
                return False
            return self.right.find(v)

    def path(self, v, p):
        if v == self.value:
            return p + "1"
        elif v < self.value:
            if self.left is None:
                return p + "0"
            else:
                return self.left.path(v, p + 'L')
        else:
            if self.right is None:
                return False
            return self.right.path(v, p + 'R')
