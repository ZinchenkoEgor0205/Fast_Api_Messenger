FROM ubuntu:latest
LABEL authors="zinch"

ENTRYPOINT ["top", "-b"]