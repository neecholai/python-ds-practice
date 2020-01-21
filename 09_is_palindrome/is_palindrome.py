def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    new_phrase = ''.join([letter for letter in phrase if letter is not " "])
    new_phrase_lower = new_phrase.lower()

    return new_phrase_lower == new_phrase_lower[::-1]

print('should be True', is_palindrome('taco cat'))
print('should be False', is_palindrome('robert'))
