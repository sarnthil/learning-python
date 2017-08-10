class LinkedList:
    def __init__(self, from_what):
        from_what = iter(from_what)
        self.val = next(from_what)
        try:
            self.link = LinkedList(from_what)
        except StopIteration:
            self.link = None

    def __repr__(self):
        if  self.link is None:
            return repr(self.val)
        else:
            return repr(self.val) + ", " + repr(self.link)

    def __getitem__(self, n):
        if n == 0:
            return self.val
        elif len(self) - 1:
            return self.link[n-1]
        else:
            raise IndexError

    def __len__(self):
        if self.link is None:
            return 1
        else:
            return len(self.link) + 1

    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            return False
        elif self.link is None and other.link is None:
            return self.val == other.val
        else:
            return (self.val == other.val and
                    self.link == other.link)

    def insert(self, n, e):
        if n == 0:
            old = self.link
            self.link = LinkedList([e])
            self.link.link = old
        elif len(self) - 1:
            self.link.insert(n-1, e)
        else:
            raise IndexError

    def delete(self, i):
        if i == 0:
            self.link = self.link.link
        elif len(self) - 1:
            self.link.delete(i-1)
        else:
            raise IndexError

    # Linked list is the worst ds if you want to check for 
    # a palindrome, but we do this for fun.

    def fst(self):
        return self.val

    def lst(self):
        if self.link is None:
            return self.val
        else:
            return self.link.lst()

    def rev(self):
        return LinkedList(reversed(self))

    def ispal(self):
        return self == rev(self)

    
