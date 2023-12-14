
watch:
	find . | entr -d make test

run:
	docker run --rm --env PYTHONUNBUFFERED=1 -v $$(pwd):/app python:3.9.18 python /app/$(SCRIPT) /app/$(INPUT)

test:
	$(MAKE) run SCRIPT=rounded-rocks-load.py INPUT=test-input
	$(MAKE) run SCRIPT=rounded-rocks-cycles.py INPUT=test-input

task1:
	$(MAKE) run SCRIPT=rounded-rocks-load.py INPUT=input

task2:
	$(MAKE) run SCRIPT=rounded-rocks-cycles.py INPUT=input
