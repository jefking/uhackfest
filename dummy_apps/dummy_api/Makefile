TAG := 1.0.0
IMAGE := uhackfest-dummy-api:$(TAG)

.PHONY: image

image:
	docker build -t ${IMAGE} .

dev: image
	docker run --rm -it -p 8000:8000 \
	$(IMAGE) /bin/sh

run: image
	docker run --rm -it -p 8000:8000 \
	$(IMAGE)
