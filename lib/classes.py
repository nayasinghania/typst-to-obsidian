from dataclasses import dataclass


@dataclass
class Heading:
  level: int
  text: str


@dataclass
class Text:
  text: str


@dataclass
class BulletedList:
  text: str


@dataclass
class NumberedList:
  text: str


Node = Heading | Text | BulletedList | NumberedList
