#!/bin/bash

set -e

EC2_IP="$(head -n1 aws-ec2.txt)"
PROJ_RPATH=$(realpath -s --relative-to="$HOME" "$(pwd)")/
KEY_LOC="$(tail -n1 aws-ec2.txt)"

ssh -i "${KEY_LOC}" "${EC2_IP}"
