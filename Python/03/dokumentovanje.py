def ping(something):
    """ Funkcija koja vraca ono sto dobije"""
    return something

class Klasa:
    """
    Klasa koja nista ne radi
    """
    pass

print(ping.__doc__)  # specifican atribut koji sadrzi docstring
print(Klasa.__doc__)

# google style
def square_root(n):
    """Calculate the square root of a number.

    Args:
        n: the number to get the square root of.
    Returns:
        the square root of n.
    Raises:
        TypeError: if n is not a number.
        ValueError: if n is negative.

    """
    pass

#reST stil
def rest_stil(param1, param2):
    """
    This is a reST style.

    :param param1: this is a first param
    :param param2: this is a second param
    :returns: this is a description of what is returned
    :raises keyError: raises an exception
    """
    pass