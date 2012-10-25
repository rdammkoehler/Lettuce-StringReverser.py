#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lettuce import step, world
from string_reverser.string_reverser import Reverser 

@step(u'Given a String Reverser')
def given_a_string_reverser(step):
    world.reverser = Reverser()

@step(u'When I reverse the string "([^"]*)"')
def when_i_reverse_the_string_group1(step, group1):
    world.result = world.reverser.reverse(group1)

@step(u'Then the result is "([^"]*)"')
def then_the_result_is_group1(step, group1):
    assert world.result == group1
