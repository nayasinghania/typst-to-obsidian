#!/bin/sh

filename=$1
echo "Converting $filename"
cargo run --manifest-path parser/Cargo.toml -- "$filename" | python converter/main.py
