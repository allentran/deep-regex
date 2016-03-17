import random
import string

SUFFIXES = ['*','+', '?']
#^ (e.g) [^0-9]
RANGES = ['A-Z','a-z','0-9']

# single tokens in outside group, (a|b), {number}, {number, number}, ^ start, %
def random_ascii():
    return random.choice(string.printable)

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

