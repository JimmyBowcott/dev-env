#!/usr/bin/env bash

sudo systemctl enable NetworkManager
sudo systemctl enable bluetooth
sudo systemctl enable sddm
sudo systemctl set-default graphical.target
sudo systemctl start sddm

if [[ "$SHELL" != "$(command -v zsh)" ]]; then
    chsh -s "$(command -v zsh)"
fi

mkdir -p "$HOME/bin"
mkdir -p "$HOME/.local/bin"
