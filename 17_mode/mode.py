def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    num_count = {}
    for num in nums:
        num_count[num] = num_count[num] + 1 if (num in num_count) else 1

    max = 0
    for (num, count) in num_count.items():
        if count > max:
            max = count
            highest_frequency = num

    return highest_frequency

print('should be 2', mode([2, 2, 3, 3, 2]))