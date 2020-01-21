def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if len(lst) < 1:
        return

    return lst[-1]

print("should be 3", last_element([1,2,3]))
print("should be None", last_element([]))
