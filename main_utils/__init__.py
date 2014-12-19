# python
import random
import string
import time


def random_string(length=32, chars=string.ascii_letters+string.digits):
    return ''.join([random.choice(chars) for i in xrange(length)])


def timestamp_random_string(length=32, chars=string.ascii_letters+string.digits):
    timestamp = int(time.time())
    return '%s-%s' % (timestamp, random_string(length-len(str(timestamp))-1, chars))