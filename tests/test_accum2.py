import pytest
from stuff.accum import Accumulator

@pytest.fixture
def accum():
    return Accumulator()

 # --------------------------------------------------------------------------------
# A most basic test function
# --------------------------------------------------------------------------------

def test_accumlator_add_one(accum):
    accum.add(4)
    assert accum.count==4
def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
     accum.count = 10