install:
	# install commands
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	# format code
	black *.py 
lint:
	# flake8 or pylint
	pylint --disable=R,C *.py
run:
	# Run app
	uvicorn blog.main:app --host 0.0.0.0 --port 8080 --reload
all: install format lint