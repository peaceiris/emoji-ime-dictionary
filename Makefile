.PHONY: build
build:
	docker-compose run --rm -T dev python main.py

.PHONY: test
test:
	docker-compose run --rm -T dev python main_test.py

.PHONY: all
all:
	$(MAKE) test
	$(MAKE) build
