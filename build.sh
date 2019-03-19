#!/usr/bin/env bash

# Fail on unset variables and command errors
set -eu -o pipefail # -x: is for debugging

uniq emoji.txt > emoji.tsv
cp emoji.tsv emoji.txt
