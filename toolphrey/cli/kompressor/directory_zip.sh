#!/usr/bin/bash

set -e

for d in */ ; do
    DIR=$(echo "$d" | sed 's/\/*$//g')
    python -m kompressor --dir "$DIR"
done

