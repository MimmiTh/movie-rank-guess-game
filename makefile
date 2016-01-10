.PHONY: bootstrap

bootstrap: _virtualenv
	_virtualenv/bin/pip install -r requirements.txt

_virtualenv:
	virtualenv --no-site-packages _virtualenv
	_virtualenv/bin/pip install --upgrade pip