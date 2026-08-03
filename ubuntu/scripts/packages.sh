#!/usr/bin/env bash

set -e

OS_DIR="$(cd "$(dirname "$0")/.." && pwd)"

sudo apt update
sudo apt upgrade -y

for file in "$OS_DIR"/packages/*.txt; do
    packages=()

    while read -r package; do
        [[ -z "$package" ]] && continue
        [[ "$package" =~ ^# ]] && continue
        packages+=("$package")
    done < "$file"

    if [ "${#packages[@]}" -gt 0 ]; then
        sudo apt install -y "${packages[@]}"
    fi
done
