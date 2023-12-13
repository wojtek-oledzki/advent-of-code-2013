
watch:
	find . | entr -d make test

run:
	docker run --rm  -v $$(pwd):/app php:cli-alpine3.18 php /app/$(SCRIPT) /app/$(INPUT)

test:
	# $(MAKE) run SCRIPT=a2z.php INPUT=test-input
	# $(MAKE) run SCRIPT=a2z.php INPUT=test-input2
	$(MAKE) run SCRIPT=a2z-ghost.php INPUT=test-input3

task1:
	$(MAKE) run SCRIPT=a2z.php INPUT=input

task2:
	$(MAKE) run SCRIPT=a2z-ghost.php INPUT=input
