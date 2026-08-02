#!/usr/bin/env bash

sudo pacman -S --needed --noconfirm \
    linux-firmware \
    mesa \
    vulkan-icd-loader

if grep -q "GenuineIntel" /proc/cpuinfo; then
    sudo pacman -S --needed --noconfirm intel-ucode
elif grep -q "AuthenticAMD" /proc/cpuinfo; then
    sudo pacman -S --needed --noconfirm amd-ucode
fi

if lspci | grep -qi "nvidia"; then
    sudo pacman -S --needed --noconfirm \
        nvidia \
        nvidia-utils
fi

if lspci | grep -qi "amd\|ati"; then
    sudo pacman -S --needed --noconfirm \
        vulkan-radeon
fi

if lspci | grep -qi "intel"; then
    sudo pacman -S --needed --noconfirm \
        vulkan-intel
fi
