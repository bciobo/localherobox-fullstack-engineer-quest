#! /usr/bin/env sh
set -e

# Import csv data into db
python -m backend.src.cmd.csv_importer

# Start Uvicorn
exec uvicorn backend.src.main:app --host 0.0.0.0 --port 8000
