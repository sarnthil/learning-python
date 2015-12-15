def mysort(some_list):
    '''Implement mysort, which is any sorting algorithm you want.
    Don't remove what's already here, and don't use sorted(), .sort() etc.
    You may sort in-place or inside a new list, the important thing is to return
    a sorted version of the given list.
    You may define any number of additional functions, or just use this one.

    >>> mysort([])
    []
    >>> mysort([1,2,3])
    [1, 2, 3]
    >>> mysort([1,6,2,8,4])
    [1, 2, 4, 6, 8]
    >>> mysort([4,3,2,1,0,-1])
    [-1, 0, 1, 2, 3, 4]
    >>> mysort([1,4,2,1,4])
    [1, 1, 2, 4, 4]
    '''
    for index in range(0, len(some_list)):
        minimum = index
        for other_index in range(index + 1, len(some_list)):
            if some_list[other_index] < some_list[minimum]:
                minimum = other_index
            some_list[index], some_list[minimum] = some_list[minimum], some_list[index]
    return some_list
    '''2/5 point, gives incorrect results.'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()
