def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_count = {}
    for letter in phrase:
        letter_count[letter] = letter_count[letter] + 1 if (letter in letter_count) else 1
    
    return letter_count

print("should be {'Y': 1, 'a': 1, 'y': 1}", multiple_letter_count('Yay'))