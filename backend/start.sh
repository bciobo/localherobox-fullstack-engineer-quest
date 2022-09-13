#! /usr/bin/env sh
set -e

# Wait for DB to start
#python -m app.cmd.backend_pre_start

# Import csv data into db
python -m app.cmd.csv_importer

# Start Uvicorn
exec uvicorn app.main:app --host 0.0.0.0 --port 8000