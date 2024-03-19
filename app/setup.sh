#!/bin/bash

set -e

echo "[Development-env] Running initial setup..."

venv=venv
python3 -m venv "${venv}"
source "${venv}"/bin/activate

pip3 install --upgrade pip
pip3 install -r requirements.txt

echo
echo "Finished setting up the venv, begin by entering command in terminal: source venv/bin/activate"
