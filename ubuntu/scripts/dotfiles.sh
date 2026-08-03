#!/usr/bin/env bash

OS_DIR="$(cd "$(dirname "$0")/.." && pwd)"

rsync -a "$OS_DIR/../shared/home/" "$HOME/"
rsync -a "$OS_DIR/home/" "$HOME/"
