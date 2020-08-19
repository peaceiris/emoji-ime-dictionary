#!/usr/bin/env bash

# Fail on unset variables and command errors
set -ue -o pipefail


TAG_NAME="$1"
RELEASE_ASSETS_DIR="build"
RELEASE_NOTES="release_notes.md"


\rm -rf "${RELEASE_ASSETS_DIR}" || true
mkdir "${RELEASE_ASSETS_DIR}"
cat $(echo ./tsv/*.tsv) > "./${RELEASE_ASSETS_DIR}/emoji.txt"
(
  cd "${RELEASE_ASSETS_DIR}"

  zip ./emoji.zip ./emoji.txt

  # Microsoft IME (Windows)
  nkf -w16L -Lw ./emoji.txt > ./emoji.windows.txt
  zip ./emoji.windows.zip ./emoji.windows.txt

  # ATOK for Windows
  sed -e 's/記号/顔文字*/g' ./emoji.windows.txt > ./emoji.atok-windows.txt
  zip ./emoji.atok-windows.zip ./emoji.atok-windows.txt

  # ATOK for Mac (macOS)
  sed -e 's/記号/顔文字*/g' ./emoji.txt > ./emoji.atok-macos.txt
  nkf --overwrite -w16L ./emoji.atok-macos.txt
  zip ./emoji.atok-macos.zip ./emoji.atok-macos.txt

  rm ./*.txt
)

sed -i "1i日本語 IME 絵文字拡張辞書 ${TAG_NAME}\n" "./${RELEASE_NOTES}"

(
  cd "${RELEASE_ASSETS_DIR}"
  hub release edit \
    --file "../${RELEASE_NOTES}" \
    $(for i in $(echo *); do echo -n "--attach ${i}#${i} "; done) \
    "${TAG_NAME}"
)
