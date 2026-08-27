#!/bin/sh

filename=$1
echo "--------------------"
echo "Converting $filename"
echo "--------------------"
echo ""
cargo run --quiet --manifest-path parser/Cargo.toml -- "$filename" | python converter/main.py
