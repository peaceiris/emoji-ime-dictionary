#!/usr/bin/env bash

# Fail on unset variables and command errors
set -e -o pipefail # -x: is for debugging


# values
DICT_DIR="./dict"
DIST_DIR="./dist"
ORG_DICT="emoji emoji_additional"


# functions
function add() {
    cd ${DICT_DIR}
    for i in ${ORG_DICT}; do
        uniq ${i}.txt > ${i}.tsv
        cp ${i}.tsv ${i}.txt
    done
}

function build() {
    echo "build"
    # zip file for macOS and Linux
    # zip file for Windows
}

function help() {
    echo "help"
}


# main
case $1 in
    "add" | "-a")
        add
        ;;
    "build" | "-b")
        build
        ;;
    *)
        help
        ;;
esac
