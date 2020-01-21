def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    compact_list = [value for value in lst if value]
    return compact_list

print("Should be [1, 2, 'All done']", compact([0, 1, 2, '', [], False, (), None, 'All done']))