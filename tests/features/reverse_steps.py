#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
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
    world.assert_equal(world.result, group1)

@step('I reverse these strings:')
def when_i_reverse_these_strings(step):
    outputs = list()
    for input in step.hashes:
        outputs.append(world.reverser.reverse(input['input']))
    outputs.reverse()
    world.outputs = outputs

@step('the results are:')
def then_the_results_are(step):
    for expected in step.hashes:
        world.assert_equal(world.outputs.pop(), expected['output'])
