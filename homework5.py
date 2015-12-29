'''Today's topic: OOP!

15.5/16'''

class Animal(object):
    '''Write a generic animal class that keeps track of how many animals there
    are overall.

    3.5/4 points #Hacky "An"/"A" thing :(( DON'T DO THAT!!!
    '''
    count = 0
    def __init__(self, name):
        '''Set name of that animal.'''
        self.name = name
        Animal.count += 1
        if type(self) != Animal:
            type(self).count += 1
    def __str__(self):
        '''Return a human-readable version of the animal: "An animal called <name>."'''
        classname = type(self).__name__.lower()
        n = 'n' if classname[0] in "aeiou" else ''
        return "A{} {} called {}.".format(n, classname, self.name)
    def __repr__(self):
        '''Return a string that would create an equivalent object when given to
        Python.'''
        classname = type(self).__name__
        return "{}('{}')".format(classname, self.name)

'''Write two other classes "Fox" and "Goat" that inherit from Animal. Foxes have
an additional method .teach(who, what), which take as arguments a goat, and a
topic. The goat should remember what she knows already, and therefore the .teach
method of a fox should either print "Taught the goat named <name> the topic
<topic> successfully", or throw a GoatKnowsAlready exception, which you should
also define.

4/4 points
'''
class Goat(Animal):
    count = 0
    def __init__(self, name):
        super().__init__(name)
        self.knowledge = []
class Fox(Animal):
    count = 0
    def teach(self, who, what):
        if type(who) != Goat:
            raise TypeError('You are trying to teach a nongoat pythonic creature')
        if what in who.knowledge:
            raise GoatKnowsAlready('Goat knows all')
        who.knowledge.append(what)
        print("Taught the goat named {} the topic {} successfully".format(who.name, what))

class GoatKnowsAlready(Exception):
    pass
'''
Both classes should also keep track of how many goats/foxes there are in total,
while not destroying the Animal class' counting abilities.
You should either override the __str__ and __repr__ methods in Fox and Goat, or
code it in Animal in such a way that it will e.g. print "A fox called <name>",
if it is not a generic Animal, but a fox.

4/4 points
'''
