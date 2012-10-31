#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from lettuce import *

def isDebug():
    rval = False
    try:
        if (os.environ['DEBUG']):
            rval = True
    except KeyError:
        pass
    return rval

def report(message):
    if (isDebug()):
        print message

@world.absorb
def assert_equal(string1, string2):
    assert string1 == string2, "\n'%s'\nis not equal to\n'%s'" % (string1, string2)

@before.all
def before_all():
    report("About to do all")
    
@after.all
def after_all(all):
    report("Have done all %s" % (all))
    world.spew('assert_equals')  #remove the assert_equals from world
    
@before.each_feature
def before_each_feature(feature):
    report("About to do a feature %s" % (feature))

@after.each_feature
def after_each_feature(feature):
    report("Have done a feature %s" % (feature))

@before.each_scenario
def before_each_scenario(scenario):
    report("About to do a scenario %s" % (scenario))

@after.each_scenario
def after_each_scenario(scenario):
    report("Have done a scenario %s" % (scenario))

@before.each_step
def before_each_step(step):
    report("About to do a step %s\n" % (step))
    
@after.each_step
def after_each_step(step):
    report("\nHave done a step %s" % (step))
