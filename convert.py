from dataclasses import dataclass


@dataclass
class Heading:
  level: int
  text: str


@dataclass
class Text:
  text: str


def parse_line(line: str) -> Heading | Text:
  parts = line.split(maxsplit=1)

  if len(parts) == 2:
    marks, text = parts

    if set(marks) == {"="}:
      return Heading(level=len(marks), text=text)

  return Text(text=line)


with open("example.typst", encoding="utf-8") as file:
  source = file.read()

nodes = [parse_line(line) for line in source.splitlines() if line.strip()]

for node in nodes:
  print(node)
