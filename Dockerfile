FROM docker.io/opensuse/leap:15.6

LABEL org.opencontainers.image.authors="nikolaj@majorov.biz"

COPY udp_server.py /usr/local/bin/udp_server
COPY udp_client.py /usr/local/bin/udp_client
RUN zypper --non-interactive in  -l -y python3 iproute2 curl vim && \
    alternatives --install  /usr/bin/python python /usr/bin/python3 1 && \
    chmod 775 /usr/local/bin/udp_* && \
    useradd -s /bin/bash suse

USER suse
# Make port available to the world outside this container
EXPOSE 9090

CMD ["udp_server"]
