def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    new_phrase = [(letter.swapcase() if letter.lower() == to_swap.lower() else letter) for letter in phrase]
    return ''.join(new_phrase)

print('should be aAAAhhh', flip_case('Aaaahhh', 'a'))
