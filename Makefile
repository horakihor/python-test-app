.PHONY: build test

NAME = web
VERSION = latest
REGISTRY = test
AWS_REPO_REGION = eu-west-2

build:
	$(call blue, "Build Docker Image...")
	docker build -t ${NAME}:${VERSION} .

test:
	$(call blue, "Run unit tests...")
	docker run --rm -it ${NAME}:${VERSION} sh -c "cd /app && .venv/bin/python manage.py test"

run:
	$(call blue, "Start Application...")
	docker-compose up --build

release: build test
	$(call blue, "Release Docker Image...")
	docker tag ${NAME}:latest ${NAME}:${VERSION}

login:
	aws ecr get-login --no-include-email --region ${AWS_REPO_REGION}

publish:
	$(call blue, "Publishing Docker Image to Registry...")
	docker tag ${NAME}:${VERSION} ${REGISTRY}/${NAME}:${VERSION}
	docker push ${REGISTRY}/${NAME}:${VERSION}

boot_debug:
	$(call blue, "Prepare debug environment...")
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

run_debug: boot_debug
	$(call blue, "Run application in debug mode localy...")
	.venv/bin/python manage.py run

test_debug: boot_debug
	$(call blue, "Run unit tests localy...")
	.venv/bin/python manage.py test

define blue
	@tput setaf 6
	@echo $1
	@tput sgr0
endef
