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

