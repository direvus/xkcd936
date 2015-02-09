#!/usr/bin/env python


import web
import random


DEFAULT_COUNT = 4
WORDSFILE = '/usr/share/dict/words'
TEMPLATE_DIR = 'templates/'


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
        except TypeError:
            count = DEFAULT_COUNT
        try:
            maxlength = int(inputs.maxlength)
        except TypeError:
            maxlength = None

        if maxlength <= 0:
            maxlength = None

        if inputs.propers != 'true':
            words = [x for x in wordlist if x[0].islower()]

        if maxlength > 0:
            words = [x for x in wordlist if len(x) <= maxlength]

        sample = random.sample(words, count)
        return render.index(
                sample,
                len(words),
                count,
                inputs.propers,
                maxlength,
                )


app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()


if __name__ == '__main__':
    app.run()
