# cs362 - in class activity 04
# casey nord
# spring 2021


import pytest
from palindrome import *
from wordcount import *


# palindrome unit tests
def test_one():
    assert palindrome("racecar") == True

def test_two():
    assert palindrome("tacocat") == True

def test_three():
    assert palindrome("level") == True

def test_four():
    assert palindrome("banana") == False

def test_five():
    assert palindrome(42) == -1

def test_six():
    assert palindrome(26.4) == -1

def test_seven():
    assert palindrome(False) == -1


# wordcount unit tests
def test_eight():
    assert wordcount("racecar") == 1

def test_nine():
    assert wordcount("this exercise in painful") == 4

def test_ten():
    assert wordcount("thisisjustonebigword") == 1

def test_eleven():
    assert wordcount("r e a l l y j u s t a b u n c h o f c h a r s") == 23

def test_twelve():
    assert wordcount(46) == 1

def test_thirteen():
    assert wordcount(True) == 1
