#!/bin/bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
WORK_DIR="${SCRIPT_DIR}/.."
SERVICE_NAME="216server"

# stop the server
docker-compose \
    -f "${WORK_DIR}"/base.dc.yml \
    -f "${WORK_DIR}"/"${SERVICE_NAME}".dc.yml \
    down
