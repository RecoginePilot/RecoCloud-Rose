#!/bin/bash

set -e

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
WORK_DIR="${SCRIPT_DIR}"
# go into current dir to make sure everything work as per intended
cd "$WORK_DIR"

EC2_IP="$(head -n1 aws-ec2.txt)"
PROJ_RPATH=$(realpath -s --relative-to="$HOME" "$(pwd)")/
KEY_LOC="$(tail -n1 aws-ec2.txt)"

echo "PROJ_RPATH: $PROJ_RPATH"

# step1
echo "Sync aws stuff"
./aws-sync.sh

# step2
echo "Deploy AWS Stuff..."
ssh -i "${KEY_LOC}" "${EC2_IP}" "cd ~/${PROJ_RPATH};./script/app-deploy.sh"

echo "Job dones!"
