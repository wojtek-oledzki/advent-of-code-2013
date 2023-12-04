
watch:
	find . | entr -d make test

test:
	docker run --rm  -v $$(pwd):/app php:cli-alpine3.18 php /app/read-engine-schema.php test-input

task1:
	docker run --rm  -v $$(pwd):/app php:cli-alpine3.18 php /app/read-engine-schema.php input
