FROM alpine:latest
  
RUN apk add --update --no-cache \
        bash \
        tcpdump \
        iperf \
        busybox-extras \
        iproute2 \
        iputils

COPY . /scripts/

RUN  sh /scripts/script.sh

CMD /bin/bash