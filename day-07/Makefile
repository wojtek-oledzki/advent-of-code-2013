
watch:
	find . | entr -d make test

run:
	docker run --rm  -v $$(pwd):/app golang:alpine3.17 go run /app/$(SCRIPT) --input /app/$(INPUT)

test:
	$(MAKE) run SCRIPT=camelCards.go INPUT=test-input
	$(MAKE) run SCRIPT=camelCardsWithJoker.go INPUT=test-input

task1:
	$(MAKE) run SCRIPT=camelCards.go INPUT=input

task2:
	$(MAKE) run SCRIPT=camelCardsWithJoker.go INPUT=input
