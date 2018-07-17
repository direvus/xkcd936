# xkcd936
A small Flask webapp to generate passwords in the style of xkcd 936 ("correct horse battery staple")

xkcd936 uses [Flask](http://flask.pocoo.org/) and the "words" dictionary from
[GNU miscfiles](http://savannah.gnu.org/projects/miscfiles/) to create a
very simple single-page webapp to generate passwords of the kind suggested
by [xkcd 936](http://xkcd.com/936).

The app allows you to choose:
 * the number of words to generate,
 * whether to include proper nouns,
 * and the maximum length of words to select from.
 
In addition to generating a password, the app also provides some information
about the difficulty of cracking such a password.

## Installation

`pip install Flask`, and then run the app locally with `FLASK_APP=code.py flask
run`, or deploy onto a webserver however you like.

The page uses [Bootstrap](http://getbootstrap.com/) for its UI, but you don't
need to install anything, it links to the Bootstrap CDN.

I have been running it on Python 2.7, but it ought to be Python 3
compatible, or close to.

## Demo

There is an instance of this app available for general use at
https://swords.id.au/xkcd936/

## License

xkcd936 is licensed under the "MIT License".
