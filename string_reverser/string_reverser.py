#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

class Reverser(object):
    def __init__(self):
        pass

    def reverse(self,input):
        words = string.split(input)
        words.reverse()
        return string.join(words, " ")
