
watch:
	find . | entr -d make test

test:
	docker run --rm  -v $$(pwd):/app php:cli-alpine3.18 php /app/check-cards.php test-input
	docker run --rm  -v $$(pwd):/app php:cli-alpine3.18 php /app/cards-copies.php test-input

task1:
	docker run --rm  -v $$(pwd):/app php:cli-alpine3.18 php /app/check-cards.php input

task2:
		docker run --rm  -v $$(pwd):/app php:cli-alpine3.18 php -d memory_limit=256M /app/cards-copies.php input
