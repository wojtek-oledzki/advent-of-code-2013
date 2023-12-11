
watch:
	find . | entr -d make test

run:
	docker run --rm  -v $$(pwd):/app python:3.9.18 python /app/$(SCRIPT) /app/$(INPUT)

test:
	$(MAKE) run SCRIPT=expand.py INPUT=test-input
	$(MAKE) run SCRIPT=expand-1000000.py INPUT=test-input

task1:
	$(MAKE) run SCRIPT=expand.py INPUT=input

task2:
	$(MAKE) run SCRIPT=expand-1000000.py INPUT=input
