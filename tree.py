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
        if (self.parent == node):
            return
        if (node):
            prevParent = self.parent
            self._parent = node
            # print('GRANDPARENT', prevParent)
            if (prevParent):
                # print('inside the conditional')
                prevParent.remove_child(self)
            if (not node.children.count(self)):
                node.add_child(self)
        else:
            self._parent = None

    def add_child(self, node):
        if (node):
            print('NODE', node)
            print('SELF_CHILDREN', self.children)
            print('Conditional', not self.children.count(node))
            if (not self.children.count(node)):
                self._children.append(node)
                node.parent = self

    def remove_child(self, child):
        if (child):
            self._children.remove(child)
            child.parent = None


node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

# node3.parent = node1
# node3.parent = node2

node1.add_child(node2)
node1.add_child(node2)

# print(node1.children)
# print(node2.children)

    # @value.setter

