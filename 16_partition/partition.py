def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

    true_values = [val for val in lst if fn(val)]
    false_values = [val for val in lst if not fn(val)]

    return [true_values, false_values]

def is_even(num):
    return num % 2 == 0

print("should be [[2, 4], [1, 3]]", partition([1, 2, 3, 4], is_even))

def is_string(el):
    return isinstance(el, str)

print("should be [['hi', 'bye'], [None, 6]]", partition(["hi", None, 6, "bye"], is_string))