class Node: 
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if (node):
            grandparent = node.parent
            if (grandparent):
                grandparent.remove_child(node)
            self._parent = node
            node.add_child(self)

    def add_child(self, node):
        if (node):
            if (not node in self._children):
                node.parent = self
            self._children.append(node)

    def remove_child(self, child):
        if (child):
            self._children.remove(child)
            child.parent = None


node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2

print(node1.children)
print(node2.children)

    # @value.setter

