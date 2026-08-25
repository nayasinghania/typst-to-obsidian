from dataclasses import dataclass


class Node:
  pass


@dataclass
class EmptyLine(Node):
  pass


@dataclass
class Heading(Node):
  level: int
  text: str


@dataclass
class TextLine(Node):
  text: str


@dataclass
class BulletedListItem(Node):
  text: str


@dataclass
class NumberedListItem(Node):
  text: str
