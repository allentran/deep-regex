import random
import string

import numpy as np

SUFFIXES = ['*','+', '?']
#^ (e.g) [^0-9]
RANGES = ['A-Z','a-z','0-9']

# single tokens in outside group, (a|b), {number}, {number, number}, ^ start, %
def random_ascii():
    return random.choice(string.printable)

def random_number():
    return random.choice(string.digits)

class DeterminateToken(object):

    def __init__(self, token):
        self.token = token

    def __call__(self, *args, **kwargs):
        return self.token

class RandomToken(object):

    def __init__(self, token_template, n_args, random_generator, sorted_args=False):
        self.token_template = token_template
        self.n_args = n_args
        self.random_generator = random_generator
        self.sorted_args = sorted_args

    def __call__(self, *args, **kwargs):
        random_args = [self.random_generator() for _ in self.n_args]
        if self.sorted_args:
            random_args = sorted(random_args)
        return self.token_template % random_args

class Modifier(object):

    pre_modifiers = [(DeterminateToken('^'), 1)]
    post_modifiers = [
        (DeterminateToken('?'), 0.3),
        (DeterminateToken('*'), 0.3),
        (DeterminateToken('+'), 0.3),
        (RandomToken('{%s}', 1, random_number), 0.3)
    ]

    def _modify(self, pos, modify_token, s):
        if pos == 0:
            return '%s%s' % (modify_token, s)
        return '%s%s' %(s, modify_token)

class RegexToken(object):

    def generate(self):
        return NotImplementedError

    def modify(self, s):
        pass

    def __call__(self, *args, **kwargs):
        return self.modify(self.generate())

class RegexGroup(RegexToken):

    def generate(self):
        pass


    def modify(self, s):
        # add group modifiers
        return '[%s]'


class SingleCharInGroup(RegexToken):
    def generate(self):
        return '[%s]'



class RegexGenerator(object):
    pass



