#!/bin/bash

set -e

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

dst_dir_fpath="$SCRIPT_DIR"/static/

# create gitignore
mkdir -p "$dst_dir_fpath"
echo "*" >"$dst_dir_fpath"/.gitignore
echo "!.gitignore" >>"$dst_dir_fpath"/.gitignore

# src_dir_fpath=/mnt/misc-imagedb/cloud-product/lane-guard/backend/static/dashboard/
# echo "Downloading model from '$src_dir_fpath' -> '$dst_dir_fpath'"
# rsync -arvP "$src_dir_fpath" "$dst_dir_fpath"
