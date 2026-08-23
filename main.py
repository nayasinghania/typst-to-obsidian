from lib.convert import parse_line

with open("example.typst", encoding="utf-8") as file:
  source = file.read()

nodes = [parse_line(line) for line in source.splitlines() if line.strip()]

for node in nodes:
  print(node)
