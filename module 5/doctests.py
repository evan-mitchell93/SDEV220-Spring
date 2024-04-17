def test_my_func(opt):
    """
    >>> (0 <= test_my_func(0) < 1)
    True
    >>> x = test_my_func(1)
    >>> int(x) == x
    True
    """
    import mymod
    if opt == 0:
        return mymod.my_num()
    else:
        return mymod.my_int()
    
if __name__ == "__main__":
    import doctest
    import mymod
    doctest.testmod()