import pytest
from pkg.mod1 import *

def test_do_something():
    res = deco_str('CONT', 'LEFT[', ']RIGHT')
    assert res, 'LEFT[CONT]RIGHT'