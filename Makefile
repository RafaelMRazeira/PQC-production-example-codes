install:
	python -m venv venv; \
	. venv/bin/activate; \
	pip install --upgrade pip; \
	pip install pre-commit; \
	pip install -e .[dev]; \
	pre-commit install; \
	git config --bool flake8.strict true; \

build:
	docker build -t pqc-server .

build_client:
	docker build -t pqc-client .

run:
	python main.py

c_run:
	docker run --rm -it -v .:/shared -p 5001:5001 pqc-server /bin/bash

c_run_client:
	docker run --network=host --rm -it -v .:/shared -p 5001:5001 pqc-client /bin/bash 