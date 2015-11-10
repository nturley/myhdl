"""
Even the best fall down sometimes
Even the wrong words seem to rhyme
Out of the doubt that fills your mind
You finally find, you and I collide
"""
from __future__ import absolute_import
#!/usr/bin/python2.7-32
# -*- coding: utf-8 -*-

from myhdl import *
from myhdl.conversion import analyze 

import pytest

class Bus:
    def __init__(self):
      self.a = Signal(bool(False))

def invert(i, bar):
    @always_comb
    def foo():
        bar.next = not i
    return foo

def underscore_collision(busin, you_and_i):
    """ Using underscores as delimiters can collide"""
    you_and = invert(busin.a, you_and_i)
    return you_and

def keyword_collide(std_logic, assign):
    """ using VHDL or Verilog keywords can collide """
    @always_comb
    def foo():
        std_logic.next = not assign
    return foo

def invalid_char(_private, _signals):
    """ leading underscores are invalid in VHDL"""
    @always_comb
    def foo():
        _private.next = not _signals
    return foo

def case_insensitive(lifetime, lifeTime):
    """ VHDL is case insensitive """
    @always_comb
    def foo():
        lifetime.next = not lifeTime
    return foo

#@pytest.mark.xfail
def test_collision_underscore():
    assert analyze(underscore_collision, Bus(),Signal(bool(False))) == 0
@pytest.mark.xfail
def test_collision_keyword():
    assert analyze(keyword_collide, Signal(bool(False)), Signal(bool(False))) == 0
@pytest.mark.xfail
def test_collision_invalid_char():
    assert analyze(invalid_char, Signal(bool(False)), Signal(bool(False))) == 0
@pytest.mark.xfail
def test_collision_case_insensitive():
    assert analyze(case_insensitive, Signal(bool(False)), Signal(bool(False))) == 0