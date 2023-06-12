import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __len__(self):
        return self.get_height(self.root)

    def __iter__(self):
        return self.traverse(self.root)

    def __getitem__(self, value):
        return self.search(self.root, value)

    def __contains__(self, value):
        return self.__getitem__(value) is not None

    def __str__(self):
        return self.draw_tree(self.root)

    def __setitem__(self, value):
        self.insert(value)

    def __lshift__(self, value):
        self.insert(value)

    def __pow__(self, exponent):
        new_tree = Tree()
        new_tree.root = self.copy_tree(self.root)

        while self.count(new_tree.root) != self.count(self.root) ** exponent:
            new_tree.insert(random.randint(1, 100))

        return new_tree

    def get_height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def count(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count(node.left) + self.count(node.right)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, node, value):
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self.search(node.left, value)
        else:
            return self.search(node.right, value)

    def traverse(self, node):
        if node is not None:
            yield from self.traverse(node.left)
            yield node.value
            yield from self.traverse(node.right)

    def copy_tree(self, node):
        if node is None:
            return None
        else:
            new_node = Node(node.value)
            new_node.left = self.copy_tree(node.left)
            new_node.right = self.copy_tree(node.right)
            return new_node

    def draw_tree(self, node, level=0):
        tree_str = ""

        if node is not None:
            tree_str += self.draw_tree(node.right, level + 1)
            tree_str += "  " * level + str(node.value) + "\n"
            tree_str += self.draw_tree(node.left, level + 1)

        return tree_str

t = Tree()

t.insert(5)
t.insert(3)
t.insert(7)
t.insert(2)
t.insert(4)
t.insert(6)
t.insert(8)

print("Wysokość drzewa:", len(t))

print("Liczba wierzchołków:", t.count(t.root))

print("Przeglądanie wierzchołków:")
for value in t:
    print(value)

print("Czy 4 jest w drzewie?", 4 in t)
print("Czy 10 jest w drzewie?", 10 in t)

t2 = t ** 2
print("Nowe drzewo:")
print(t2)

t[9] = None
print("Dodano element 9:")
print(t)

print("Rysowanie drzewa:")
print(t)
