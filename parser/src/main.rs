use std::{env, fs};
use typst_syntax::parse;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = args.get(1).expect("usage: parser <filename>");
    let source = fs::read_to_string(filename).expect("failed to read input file");
    let parsed = parse(&source);

    println!("{parsed:#?}");
}
