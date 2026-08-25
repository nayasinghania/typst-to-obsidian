from .classes import *


def parse_line(line: str) -> Node:
  if not line.strip():
    return EmptyLine()

  parts = line.split(maxsplit=1)

  if len(parts) == 2:
    marks, text = parts

    if set(marks) == {'='}:
      return Heading(level=len(marks), text=text)

    if set(marks) == {'-'}:
      return BulletedListItem(text=text)

    if set(marks) == {'+'}:
      return NumberedListItem(text=text)

  return TextLine(text=line)
