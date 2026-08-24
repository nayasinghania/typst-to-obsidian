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
class Text(Node):
  text: str


@dataclass
class BulletedList(Node):
  text: str


@dataclass
class NumberedList(Node):
  text: str
