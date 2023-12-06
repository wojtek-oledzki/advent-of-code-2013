
watch:
	find . | entr -d make test

test:
	docker run --rm  -v $$(pwd):/app python:3.9.18 python /app/seed-location.py test-input
	docker run --rm  -v $$(pwd):/app python:3.9.18 python /app/seed-range-location.py test-input

task1:
	docker run --rm  -v $$(pwd):/app python:3.9.18 python /app/seed-location.py input

task2:
	docker run --rm  -v $$(pwd):/app python:3.9.18 python /app/seed-range-location.py input
