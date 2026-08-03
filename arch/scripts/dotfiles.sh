#!/usr/bin/env bash

REPO="$(cd "$(dirname "$0")/.." && pwd)"

rsync -a "$REPO/home/" "$HOME/"
