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
    cd ${DICT_DIR}
    local BUNDLE="emoji.all.txt"
    local ZIP_FILE="emoji.zip"
    touch ${BUNDLE}
    for i in ${ORG_DICT}; do
        cat ${i}.txt >> emoji.all.txt
    done
    zip ${ZIP_FILE} ${BUNDLE}
    mv ${ZIP_FILE} ../${DIST_DIR}/
    rm ${BUNDLE}
    # zip file for macOS and Linux
    # zip file for Windows
}

function help() {
    cat << EOF
usage: ./task.sh [OPTION]
    add   (-a, --add)  : run after emoji addition
    build (-b, --build): build release
    help               : show this help
EOF
}


# main
case $1 in
    "add" | "-a" | "--add")
        (add)
        ;;
    "build" | "-b" | "--build")
        (build)
        ;;
    *)
        help
        ;;
esac
