from .classes import *


def parse_line(line: str) -> Node:
  parts = line.split(maxsplit=1)

  if len(parts) == 2:
    marks, text = parts

    if set(marks) == {'='}:
      return Heading(level=len(marks), text=text)

    if set(marks) == {'-'}:
      return BulletedList(text=text)

    if set(marks) == {'+'}:
      return NumberedList(text=text)

  return Text(text=line)
