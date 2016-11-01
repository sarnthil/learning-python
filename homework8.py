from math import ceil
from typing import List

def heapify(ls: List[int]) -> None:
    """ Heapify the given list in-place. """
    for index in range(len(ls)):
        _siftup(ls, index)

def _siftup(ls: List[int], current: int) -> None:
    """ Sift up from a given index. """
    while current != 0:
        parent = ceil((current - 1)/2)
        if ls[parent] > ls[current]:
            ls[parent], ls[current] = ls[current], ls[parent]
            current = parent
        else:
            break

def _siftdown(ls: List[int], current: int) -> None:
    """ Sift down from a given index. """
    while True:
        left = 2 * current + 1
        right = 2 * current + 2
        if left >= len(ls):
            break
        elif right >= len(ls):
            if ls[left] < ls[current]:
                ls[left], ls[current] = ls[current], ls[left]
                break
            else:
                break
        else:
            # if ls[left] <= ls[right]:
            #     if ls[left] < ls[current]:
            #         ls[left], ls[current] = ls[current], ls[left]
            #         current = left
            #     else:
            #         break
            # else:
            #     if ls[right] < ls[current]:
            #         ls[right], ls[current] = ls[current], ls[right]
            #         current = right
            #     else:
            #         break

            smaller = right if ls[right] <= ls[left] else left
            if ls[smaller] < ls[current]:
                ls[smaller], ls[current] = ls[current], ls[smaller]
                current = smaller
            else:
                break


def insert(ls: List[int], element: int) -> None:
    """ Insert a given element into the heap. """
    ls.append(element)
    _siftup(ls, len(ls)-1)

def delete(ls: List[int], index: int = 0) -> int:
    """ Delete the item at the given index, returning it. """
    item = ls[index]
    ls[index] = ls[-1]
    ls.pop()
    _siftdown(ls, index)
    return item

def heap_sort(ls: List[int]) -> None:
    """ Sort a given list using heap sort. """
    heapify(ls)
    for _ in range(len(ls)):
        yield delete(ls)

from random import randint
ls = [randint(1,101) for _ in range(20)]
print(ls)
print(list(heap_sort(ls)))
