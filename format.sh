echo 'Formatting and linting Python code'
ruff check render/ --fix && ruff format render/

echo ''

echo 'Formatting and linting Rust code'
cargo fmt --manifest-path parser/Cargo.toml
cargo clippy --manifest-path parser/Cargo.toml
