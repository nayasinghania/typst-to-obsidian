use serde::Serialize;
use std::{env, fs};
use typst_syntax::{SyntaxNode, parse};

#[derive(Serialize)]
struct JsonNode<'a> {
    kind: String,
    #[serde(skip_serializing_if = "str::is_empty")]
    text: &'a str,
    #[serde(skip_serializing_if = "Vec::is_empty")]
    children: Vec<JsonNode<'a>>,
}

impl<'a> From<&'a SyntaxNode> for JsonNode<'a> {
    fn from(node: &'a SyntaxNode) -> Self {
        Self {
            kind: format!("{:?}", node.kind()),
            text: node.leaf_text(),
            children: node.children().map(JsonNode::from).collect(),
        }
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = args.get(1).expect("usage: parser <filename>");
    let source = fs::read_to_string(filename).expect("failed to read input file");
    let parsed = parse(&source);
    let json = JsonNode::from(&parsed);
    serde_json::to_writer(std::io::stdout(), &json).expect("failed to serialize syntax tree");
}
