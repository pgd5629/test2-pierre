import numpy as np

from test2_pierre.my_module import typed_function


def test_typed_function():
    assert not typed_function(np.zeros(10), "")
jga = 3