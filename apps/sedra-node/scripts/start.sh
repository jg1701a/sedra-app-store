#!/bin/bash

mkdir -p /data
cd /data

# Run sedrad.exe and capture logs
wine /app/sedrad.exe --utxoindex > /data/sedra.log 2>&1 &
sleep 2

# Start log viewer HTTP server
python3 /app/log_server.py
