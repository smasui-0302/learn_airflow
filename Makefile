.PHONY: run build up init

run:
	$(MAKE) build && $(MAKE) up

build:
	docker compose build

up:
	docker compose up -d

init:
	docker compose up airflow-init

down:
	docker compose down