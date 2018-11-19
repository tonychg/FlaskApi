FROM python:3-alpine

WORKDIR /app

ADD . .

RUN set -ex \
    && pip install -q -e . \
    && mkdir /build \
    && tar --exclude=.git --exclude=.vagrant -cz -f /build/flaskapi-$(cat version.txt).tar.gz .

ENTRYPOINT ["/bin/sh"]
