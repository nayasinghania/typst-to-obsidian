from .classes import Heading, Text, Bullet


def parse_line(line: str) -> Heading | Bullet | Text:
  parts = line.split(maxsplit=1)

  if len(parts) == 2:
    marks, text = parts

    if set(marks) == {'='}:
      return Heading(level=len(marks), text=text)

    if set(marks) == {'-'}:
      return Bullet(text=text)

  return Text(text=line)
