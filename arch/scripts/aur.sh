#!/usr/bin/env bash

if ! command -v paru >/dev/null; then
    rm -rf /tmp/paru
    git clone https://aur.archlinux.org/paru.git /tmp/paru
    cd /tmp/paru || return
    makepkg -si --noconfirm
fi

mapfile -t packages < <(
    grep -vE '^\s*#|^\s*$' packages/aur.txt
)

if [ ${#packages[@]} -gt 0 ]; then
    paru -S --needed "${packages[@]}"
fi
