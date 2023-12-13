
watch:
	find . | entr -d make test

run:
	docker run --rm  -v $$(pwd):/app php:cli-alpine3.18 php /app/$(SCRIPT) /app/$(INPUT)

test:
	$(MAKE) run SCRIPT=oasis.php INPUT=test-input
	$(MAKE) run SCRIPT=oasis-history.php INPUT=test-input

task1:
	$(MAKE) run SCRIPT=oasis.php INPUT=input

task2:
	$(MAKE) run SCRIPT=oasis-history.php INPUT=input
