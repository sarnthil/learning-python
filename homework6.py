'''OOP 2: Trees

Write a class Tree that implements syntax trees.
Each node has a label and knows whether it's a leaf or not.
.leaf should be a property, but one that is automatically
determined based on the number of children (look up the property
function/decorator or ask me). Tree should have a classmethod/staticmethod
'from_string', which takes a string like '(S (NP (N Peter)) (VP (VI sleeps)))'
and can build a tree from it. repr() of a tree should return that
kind of string (wrapped in a Tree.from_string call), while str()
should return something nicer (details up to you).
Other properties that should be defined on a (sub)tree are:
    .size (amount of nodes below that node including itself)
    .depth (depth, leafs have depth 1)
Methods:
    .walk() (iterate over all nodes in the subtree)
    .walk_leaves() (iterate over all leafs in the subtree)
    .attach(other) (to attach the 'other' tree as a child to the tree)
    .delete() (to delete the subtree)
'''
class Tree(object):
    def __init__(self, label):
        self.label = label
        self.children = []
    @property
    def size(self):
        return 1 + sum(child.size for child in self.children)
    @property
    def depth(self):
        return 1 + max(child.depth for child in self.children)
    @property
    def leaf(self):
        return len(self.children) == 0
    @staticmethod
    def from_string(string):
        '''Takes something like "(S (NP Peter))" and returns a tree'''
        pass
    def __str__(self):
        pass
    def __repr__(self):
        '''Returns something like "Tree.from_string('(S (NP Peter))')"
        '''
        pass
    def walk(self):
        pass
    def walk_leaves(self):
        pass
    def attach(self, other):
        pass
    def delete(self):
        pass
