FROM alpine

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
    && rm -rf /var/cache/apk/*
RUN pip install --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
VOLUME ["/app/"]
ENTRYPOINT ["/usr/bin/python", "do.py"]
CMD ["--help"]
