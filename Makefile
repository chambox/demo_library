install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt


test:
	python -m pytest -vv --cov=client test_client.py


format:
	find . -type f -name '*.py' | xargs black


lint:
	find . -type f -name '*.py' | xargs pylint --disable=R,C

all: install test format lint