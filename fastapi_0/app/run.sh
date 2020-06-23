#!/bin/bash

set -eu

GU=${GU:-"G"}
HOST=${HOST:-"0.0.0.0"}
PORT=${PORT:-8888}
WORKERS=${WORKER:-4}
UVICORN_WORKER=${UVICORN_WORKER:-"uvicorn.workers.UvicornWorker"}
LOGLEVEL=${LOGLEVEL:-"debug"}
LOGCONFIG=${LOGCONFIG:-"./logging.conf"}


if [ ${GU} = "G" ]; then
    gunicorn app:app \
        -b ${HOST}:${PORT} \
        -w ${WORKERS} \
        -k ${UVICORN_WORKER}  \
        --log-level ${LOGLEVEL} \
        --log-config ${LOGCONFIG}

else
    uvicorn app:app \
        --host ${HOST} \
        --port ${PORT} \
        --workers ${WORKERS} \
        --log-level ${LOGLEVEL} \
        --log-config ${LOGCONFIG}
fi