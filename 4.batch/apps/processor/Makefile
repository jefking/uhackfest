TAG := 1.0.0
IMAGE := uhackfest-dummy-processor:$(TAG)

.PHONY: image

image:
	docker build -t ${IMAGE} .

dev: image
	docker run --rm -it \
	$(IMAGE) /bin/sh

run: image
	docker run --rm -it \
	$(IMAGE) $(SEC)
