# -*- coding: utf-8 -*-

import sys
from lettuce import step, world
from flying.equipment import FlyingTractor

@step(u'Given a Flying Tractor')
def given_a_flying_tractor(step):
    world.flying_tractor = FlyingTractor()

@step(u'When I operate at the minimum forward speed')
def when_i_operate_at_the_minimum_forward_speed(step):
    world.flying_tractor.setSpeed(FlyingTractor.MIN_SAFE_SPEED)

@step(u'Then the Flying Tractor will rise to the minimum safe altitude')
def then_the_flying_tractor_will_rise_to_the_minimum_safe_distance(step):
    assert world.flying_tractor.getAltitude() == FlyingTractor.MIN_SAFE_ALTITUDE, "your tractor is operating dangerously"
