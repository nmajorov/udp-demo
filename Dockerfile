FROM docker.io/opensuse/leap:15.6

LABEL org.opencontainers.image.authors="nikolaj@majorov.biz"

COPY udp_server.py /usr/local/bin/udp_server
RUN chmod a+x /usr/local/bin/udp_server && \
    useradd -s /bin/bash suse

USER suse
# Make port available to the world outside this container
EXPOSE 9090

CMD ["udp_server"]
