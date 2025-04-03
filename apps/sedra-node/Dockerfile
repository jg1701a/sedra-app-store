FROM debian:bullseye

RUN dpkg --add-architecture i386 && \
    apt update && \
    apt install -y wine64 wine32

WORKDIR /app
COPY sedrad.exe .
COPY scripts/start.sh .
COPY log_server.py .

RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]
