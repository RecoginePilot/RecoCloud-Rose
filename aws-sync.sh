#!/bin/bash

set -e

EC2_IP="$(head -n1 aws-ec2.txt)"
PROJ_RPATH=$(realpath -s --relative-to="$HOME" "$(pwd)")/
KEY_LOC="$(tail -n1 aws-ec2.txt)"

echo "PROJ_RPATH: $PROJ_RPATH"

echo "Create folder..."
ssh -i "${KEY_LOC}" "${EC2_IP}" "mkdir -p ~/${PROJ_RPATH}"

echo "Syncing..."
# Rsync ignore gitignore
# https://stackoverflow.com/questions/13713101/rsync-exclude-according-to-gitignore-hgignore-svnignore-like-filter-c
rsync -arvP --update \
    --include='**.gitignore' \
    --filter="dir-merge,- .gitignore" \
    --exclude-from="aws-rsync_exclude.txt" \
    -e "ssh -i ${KEY_LOC}" \
    "${HOME}/${PROJ_RPATH}" \
    "${EC2_IP}":~/"${PROJ_RPATH}"
# --exclude='/.git' \

## Custom include
### LaneGuard

rsync -arvP --update \
    -e "ssh -i ${KEY_LOC}" \
    "${HOME}/${PROJ_RPATH}/app/static/" \
    "${EC2_IP}":~/"${PROJ_RPATH}"/app/static/

echo "Job dones!"
