

watch:
	find . | entr -d make test

test:
	docker run --rm  -v $$(pwd):/app python:3.9.18 python /app/boat-race.py test-input
	docker run --rm  -v $$(pwd):/app python:3.9.18 python /app/boat-race.py test-input2

task1:
	docker run --rm  -v $$(pwd):/app python:3.9.18 python /app/boat-race.py input

task2:
	docker run --rm  -v $$(pwd):/app python:3.9.18 python /app/boat-race.py input2
