
watch:
	find . | entr -d make test

run:
	docker run --rm --env PYTHONUNBUFFERED=1 -v $$(pwd):/app python:3.9.18 python /app/$(SCRIPT) /app/$(INPUT)

test:
	$(MAKE) run SCRIPT=least-heat-loss.py INPUT=test-input


task1:
	$(MAKE) run SCRIPT=least-heat-loss.py INPUT=input
