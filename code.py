#!/usr/bin/env python


import web
import random
from math import log, floor
from decimal import Decimal


DEFAULT_COUNT = 4
GUESSES = 1000
SYMBOLS = 94

MIN_SECS = 60
HOUR_SECS = MIN_SECS * 60
DAY_SECS = HOUR_SECS * 24
YEAR_SECS = Decimal(DAY_SECS * 365.25)

WORDSFILE = '/usr/share/dict/words'
TEMPLATE_DIR = 'templates/'
EXPONENT_NAMES = (
        'several',
        'tens',
        'hundreds',
        'thousands',
        'tens of thousands',
        'hundreds of thousands',
        'millions',
        'tens of millions',
        'hundreds of millions',
        'billions',
        'tens of billions',
        'hundreds of billions',
        'trillions',
        'tens of trillions',
        'hundreds of trillions',
        'quadrillions',
        'tens of quadrillions',
        'hundreds of quadrillions',
        'quintillions',
        'tens of quintillions',
        'hundreds of quintillions',
        'sextillions',
        'tens of sextillions',
        'hundreds of sextillions',
        'septillions',
        'tens of septillions',
        'hundreds of septillions',
        'octillions',
        'tens of octillions',
        'hundreds of octillions',
        'nonillions',
        'tens of nonillions',
        'hundreds of nonillions',
        'decillions',
        'tens of decillions',
        'hundreds of decillions',
        'undecillions',
        'tens of undecillions',
        'hundreds of undecillions',
        'duodecillions',
        'tens of duodecillions',
        'hundreds of duodecillions',
        'tredecillions',
        'tens of tredecillions',
        'hundreds of tredecillions',
        'quattuorillions',
        'tens of quattuorillions',
        'hundreds of quattuorillions',
        'quindecillions',
        'tens of quindecillions',
        'hundreds of quindecillions',
        'sexdecillions',
        'tens of sexdecillions',
        'hundreds of sexdecillions',
        'septendecillions',
        'tens of septendecillions',
        'hundreds of septendecillions',
        'octodecillions',
        'tens of octodecillions',
        'hundreds of octodecillions',
        'novemdecillions',
        'tens of novemdecillions',
        'hundreds of novemdecillions',
        )


with open(WORDSFILE, 'r') as fp:
    wordlist = [line.strip() for line in fp]


prefix = '/xkcd936'
urls = (
        '/', 'index',
        prefix, 'index',
        prefix + '/', 'index',
        )

render = web.template.render(TEMPLATE_DIR)


def describe_magnitude(exponent):
    if exponent >= len(EXPONENT_NAMES):
        return 'an absurdly large number'
    else:
        return EXPONENT_NAMES[exponent]


def describe_count(number, unit):
    number = int(round(number))
    if number > 1:
        unit = unit + 's'
    return '{} {}'.format(number, unit)

def describe_time(seconds):
    seconds = Decimal(seconds)
    if seconds >= YEAR_SECS:
        years = seconds / YEAR_SECS
        if years > 1000:
            return '{} of years'.format(describe_magnitude(years.adjusted()))
        else:
            return describe_count(seconds / YEAR_SECS, 'year')
    if seconds >= DAY_SECS:
        return describe_count(seconds / DAY_SECS, 'day')
    if seconds >= HOUR_SECS:
        return describe_count(seconds / HOUR_SECS, 'hour')
    if seconds >= MIN_SECS:
        return describe_count(seconds / MIN_SECS, 'minute')
    return describe_count(seconds, 'second')


def entropy_bits(total_entropy):
    return int(floor(log(total_entropy, 2)))


class index(object):
    def GET(self):
        words = wordlist
        inputs = web.input(
                count=DEFAULT_COUNT,
                propers='false',
                maxlength=None,
                )
        try:
            count = int(inputs.count)
        except:
            count = DEFAULT_COUNT
        try:
            maxlength = int(inputs.maxlength)
        except:
            maxlength = None

        if maxlength <= 0:
            maxlength = None

        if inputs.propers != 'true':
            words = [x for x in words if x[0].islower()]

        if maxlength > 0:
            words = [x for x in words if len(x) <= maxlength]

        space = len(words)
        possible = space ** count
        base, exponent = '{:.2e}'.format(possible).split('e+', 1)
        exponent = int(exponent)
        magnitude = describe_magnitude(exponent)

        sample = random.sample(words, count)

        attacks = []
        algentropy = possible
        algguess = describe_time(algentropy / GUESSES)
        attacks.append((
            'Known algorithm',
            space,
            count,
            entropy_bits(algentropy),
            algguess,
            '1',
            'Assumes the attacker knows the exact algorithm used to '
            'generate the password, including the wordlist and the number of '
            'words used.',
            ))

        symlen = sum([len(x) for x in sample]) + (len(sample) - 1)
        symentropy = SYMBOLS ** symlen
        symguess = describe_time(symentropy / GUESSES)
        attacks.append((
            'All symbols',
            SYMBOLS,
            symlen,
            entropy_bits(symentropy),
            symguess,
            '2',
            'Assumes the attacker knows nothing about the password, and is '
            'trying all combinations of letters, numbers and symbols.'
            ))

        return render.index(
                sample,
                space,
                base,
                exponent,
                magnitude,
                count,
                attacks,
                inputs.propers,
                maxlength,
                )


app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()


if __name__ == '__main__':
    app.run()
