from .classes import Heading, Text


def parse_line(line: str) -> Heading | Text:
  parts = line.split(maxsplit=1)

  if len(parts) == 2:
    marks, text = parts

    if set(marks) == {"="}:
      return Heading(level=len(marks), text=text)

  return Text(text=line)
