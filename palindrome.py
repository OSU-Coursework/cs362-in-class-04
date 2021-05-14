def palindrome(_str):
    try:
        return _str == _str[::-1]
    except TypeError:
        print("Passed value was not a string... aborted!")
        return -1
