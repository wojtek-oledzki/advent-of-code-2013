
watch:
	find . | entr -d make test

run:
	docker run --rm --env PYTHONUNBUFFERED=1 -v $$(pwd):/app python:3.9.18 python /app/$(SCRIPT) /app/$(INPUT)

test:
	$(MAKE) run SCRIPT=energizing.py INPUT=test-input
	$(MAKE) run SCRIPT=max-energizing.py INPUT=test-input


task1:
	$(MAKE) run SCRIPT=energizing.py INPUT=input

task2:
	$(MAKE) run SCRIPT=max-energizing.py INPUT=input
