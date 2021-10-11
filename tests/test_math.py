"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""
# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import pytest
# --------------------------------------------------------------------------------
# A most basic test function
# --------------------------------------------------------------------------------

def test_one_plus_one():
  assert 1 + 1 == 2

# --------------------------------------------------------------------------------
# A test function to show assertion introspection
# --------------------------------------------------------------------------------

def test_one_plus_two():
  a = 1
  b = 2
  c = 3
  assert a + b == c

# --------------------------------------------------------------------------------
# A test function that verifies an exception
# --------------------------------------------------------------------------------

def test_divide_by_zero():
  with pytest.raises(ZeroDivisionError) as e:
    num = 1 / 0
  assert 'division by zero' in str(e.value)

#multiplication test ideas

#two positive integers
#identity:multiplication with one
#zero property
#positive by negative
#neative by negative
#multipying floats


def test_multiply_two_postivie_int():
    assert 2*3==6

def test_multiply_identity():
    assert 1*28==28

def test_multiply_zero():
    assert 0*4==0
#dry principle: don't repeat yourself
#that's why we are going to use parameterized

# --------------------------------------------------------------------------------
# A parametrized test function
# --------------------------------------------------------------------------------

products = [
    (2,3,6),
    (1,22,22),
    (0,28,0),
    (3,-4,-12),
    (-2,-2,4),
    (2.5,6.7,16.75)
]

@pytest.mark.parametrize('a,b,product', products)
def test_multiplication(a,b,product):
    assert a*b==product