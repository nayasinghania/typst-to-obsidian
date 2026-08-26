echo 'Formatting and linting Python code'
ruff check converter/ --fix && ruff format converter/

echo ''

echo 'Formatting and linting Rust code'
cargo fmt --manifest-path parser/Cargo.toml
cargo clippy --manifest-path parser/Cargo.toml
