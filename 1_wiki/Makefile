#Makefile default shell is /bin/sh which does not implement 'source'
SHELL := /bin/zsh
dev_env_setup:
	echo ${SHELL}
	#creating virtual environment:
	python -m venv .venv
	#activating virtual env:
	. .venv/bin/activate
	#installing dependencies from req file:
	python -m pip install -r requirements.txt