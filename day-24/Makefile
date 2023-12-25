watch:
	find . | entr -d make test


run:
	docker compose run --rm python python /app/$(SCRIPT) /app/$(INPUT)


test:
	$(MAKE) run SCRIPT=2d-hail-collision-detector.py INPUT="test-input 7 27"


task1:
	$(MAKE) run SCRIPT=2d-hail-collision-detector.py INPUT="input 200000000000000 400000000000000"

task2:
	$(MAKE) run SCRIPT=module-analyser-with-stop.py INPUT="input rx"
