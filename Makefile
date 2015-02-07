host = wesley
dest = /usr/local/webpy-apps/xkcd936
rsync_opts = -urv --exclude='.*'


install:
	rsync $(rsync_opts) code.py templates $(host):$(dest)
