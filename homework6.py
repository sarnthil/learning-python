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
    .empty() (to empty the subtree, turning the node into a leaf)
'''
import re

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
    def tokenize(string):
        pattern = r'\(|\)|[^ ()]+'
        return re.findall(pattern, string)
    @staticmethod
    def from_string(string):
        '''Takes something like "(S (NP Peter))" and returns a tree'''
        tokenslist = Tree.tokenize(string)
        return Tree.tree(tokenslist)
    @staticmethod
    def tree(tokenslist):
        t = tokenslist.pop(0)
        if t == '(':
            foo = Tree(tokenslist.pop(0))
            for subtree in Tree.trees(tokenslist):
                foo.children.append(subtree)
            return foo
        else:
            return Tree(t)
    @staticmethod
    def trees(tokens):
        while True:
            if tokens[0] == ')':
                tokens.pop(0)
                raise StopIteration
            yield Tree.tree(tokens)
    def __str__(self):
        return "Here is a string representation of the tree: \n {}\n {}".format(self._wrap(),' '.join(tree.label for tree in self.walk_leaves()))
    def _wrap(self):
        '''Returns something like "Tree.from_string('(S (NP Peter))')"
        '''
        if self.leaf:
            return self.label
        return '({} {})'.format(self.label, ' '.join(child._wrap() for child in self.children))
    def __repr__(self):
        return "Tree.from_string('{}')".format(self._wrap())
    def walk(self):
        yield self
        for child in self.children:
            yield from child.walk()
    def walk_leaves(self):
        if self.leaf:
            yield self
        for child in self.children:
            yield from child.walk_leaves()
    def attach(self, other):
        self.children.append(other)
    def empty(self):
        self.children = []
