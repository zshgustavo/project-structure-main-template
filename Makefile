.PHONY: setup lint test build up down deploy-staging

setup:
	./scripts/setup/install.sh

lint:
	./scripts/ci/lint.sh

test:
	./scripts/ci/test.sh

build:
	./scripts/ci/build.sh

up:
	docker compose up -d

down:
	docker compose down

deploy-staging:
	./scripts/deploy/staging.sh