host = wesley
dest = /usr/local/flask-apps/xkcd936
rsync_opts = -urv --exclude='.*' --exclude='*.pyc'


install:
	rsync $(rsync_opts) *.py *.wsgi templates $(host):$(dest)
