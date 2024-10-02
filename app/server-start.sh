#!/bin/bash

set -e

echo "[Development-env] Running initial setup..."

venv=venv
source "${venv}"/bin/activate

hypercorn main:app --config hypercorn.toml
