.PHONY: build
build:
	COMPOSE_DOCKER_CLI_BUILD=1 docker-compose run --rm -T dev python main.py

.PHONY: test
test:
	docker-compose run --rm -T dev python main_test.py

.PHONY: all
all:
	$(MAKE) test
	$(MAKE) build

.PHONY: run
run:
	docker-compose run --rm dev bash
