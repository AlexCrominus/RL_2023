FROM ubuntu:trusty
        
RUN apt-get clean
RUN apt-get update \
    && apt-get install -y --no-install-recommends apt-utils \
    supervisor \
    apt-utils \
    net-tools \
    build-essential \
    systemd \
    ansible \
    curl \
    iptables \
    iputils-ping \
    sudo \ 
    vsftpd \
    openssh-server \
    systemd \
    bash \
    tcpdump \
    iperf \
    iproute2 \
    ftp \
    vsftpd 

COPY ./configs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./configs/vsftpd.conf /etc/vsftpd.conf
COPY . /scripts/

RUN useradd -ms /bin/bash stupid

ENTRYPOINT [ "/sbin/init" ]
CMD /bin/bash