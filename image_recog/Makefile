DOCKER_BUILD_CMD?=docker build
DOCKER_NAME?=img_recog
DOCKER_IMAGE?=img_recog
DOCKER_FILE?=./Dockerfile
DOCKER_WS=./

all .DEFAULT:
	$(DOCKER_BUILD_CMD)  -f $(DOCKER_FILE) -t $(DOCKER_IMAGE)  $(DOCKER_WS)

clean:
	docker rmi $(DOCKER_IMAGE)

run:
	docker run -d -p 5059:5059 $(DOCKER_NAME)

.PHONY: $(DEFAULT_TARGETS)
