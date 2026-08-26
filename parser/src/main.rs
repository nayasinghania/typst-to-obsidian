use typst_syntax::parse;

fn main() {
    let source = include_str!("../../example.typ");
    let parsed = parse(source);

    println!("{parsed:#?}");
}
