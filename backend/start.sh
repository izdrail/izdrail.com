#!/bin/bash
echo "Starting osint spider foot backend"
cd /home/osint/spiderfoot || exit 1
nohup python3 sf.py -l 0.0.0.0:5001 &

echo "Starting osint spider foot web"

cd /home/osint/app || exit 2
uvicorn main:app --host 0.0.0.0 --port 8003 --reload