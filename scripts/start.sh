#!/bin/bash
echo "🚀 Starting Timelytics System..."
python backend/main.py &
python background/worker.py &
wait