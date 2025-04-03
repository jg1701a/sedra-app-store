FROM debian:bullseye

RUN dpkg --add-architecture i386 && \
    apt update && \
    apt install -y wine64 wine32 python3

WORKDIR /app
COPY sedrad.exe .
COPY scripts/start.sh .
COPY log_server.py .
COPY public/ public/

RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]
