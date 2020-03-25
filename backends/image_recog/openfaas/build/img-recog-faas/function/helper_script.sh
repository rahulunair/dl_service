#! /usr/bin/env bash

# Clone dl_service and move img recognition into `.`
git clone https://github.com/rahulunair/dl_service.git \
  && cp -r dl_service/backends/image_recog/* . \

