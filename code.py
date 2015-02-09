#!/usr/bin/env python


import web
import random


DEFAULT_COUNT = 4
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
            words = [x for x in wordlist if x[0].islower()]

        if maxlength > 0:
            words = [x for x in wordlist if len(x) <= maxlength]

        possible = len(words) ** count
        base, exponent = '{:.2e}'.format(possible).split('e+', 1)
        exponent = int(exponent)
        if exponent >= len(EXPONENT_NAMES):
            magnitude = 'an absurdly large number'
        else:
            magnitude = EXPONENT_NAMES[exponent]

        sample = random.sample(words, count)
        return render.index(
                sample,
                len(words),
                base,
                exponent,
                magnitude,
                count,
                inputs.propers,
                maxlength,
                )


app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()


if __name__ == '__main__':
    app.run()
