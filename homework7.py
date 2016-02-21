'''Implement a CYK parser'''
import sys
from toolib import Tree
from collections import defaultdict

rules = {
        'S' :{('NP','VP')},
        'NP' : {('Det', 'N'), ('NP', 'PP')},
        'VP' : {('V', 'NP'), ('VP', 'PP')},
        'PP' : {('P', 'NP')},
        }
r = defaultdict(set)
for key, value in rules.items():
    for element in value:
        r[element].add(key)
rules = r

lexicon = {
            'N': {'cat','man','woman','telescope','hill'},
            'Det' : {'the','a'},
            'P' : {'with','on','above','under','by'},
            'V' : {'fucked','saw'},
            }

lexicon = {element:key for key,value in lexicon.items() for element in value}
chart = defaultdict(list)

def cyk(sentence):
    """Given a sentence return a list of possible tree parses."""
    sentence = sentence.split()
    for index, word in enumerate(sentence):
        chart[(index,index)].append(Tree.from_string("({} {})".format(lexicon[word], word)))
    length = len(sentence)
    for i in range(1, length):
        for j in range(length-i):
            for k in range(i):
                # print((j, j+k), (j+k+1, j+i))
                for left in chart[(j,j+k)]:
                    for right in chart[(j+k+1,j+i)]:
                        for head in rules[left.label,right.label]:
                            tree = Tree(head)
                            tree.children = [left, right]
                            chart[(j,j+i)].append(tree)
    return chart[(0,length-1)]


if __name__ == '__main__':
    trees = cyk('the woman fucked the man with the telescope')
    for tree in trees:
        print(tree)
