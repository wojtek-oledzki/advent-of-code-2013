
watch:
	find . | entr -d make test

run:
	docker run --rm --env PYTHONUNBUFFERED=1 -v $$(pwd):/app python:3.9.18 python /app/$(SCRIPT) /app/$(INPUT)

test:
	$(MAKE) run SCRIPT=module-analyser.py INPUT=test-input-01
	$(MAKE) run SCRIPT=module-analyser.py INPUT=test-input-02


task1:
	$(MAKE) run SCRIPT=module-analyser.py INPUT=input

task2:
	$(MAKE) run SCRIPT=polygon-hex-area.py INPUT=input
