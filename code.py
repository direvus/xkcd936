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
        inputs = web.input(count=DEFAULT_COUNT, propers='false')
        try:
            count = int(inputs.count)
        except ValueError:
            count = DEFAULT_COUNT
        if inputs.propers != 'true':
            words = [x for x in wordlist if x[0].islower()]
        sample = random.sample(words, count)
        return render.index(sample, len(words), count, inputs.propers)


app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()


if __name__ == '__main__':
    app.run()
