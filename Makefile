.PHONY: build
build:
	docker-compose run --rm -T dev python main.py
