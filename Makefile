install:
	docker-compose build dope

run:
	docker-compose run --no-deps --rm dope sh -c 'python dope.py'

test:
	docker-compose run --no-deps --rm dope sh -c 'py.test --failed-first'
