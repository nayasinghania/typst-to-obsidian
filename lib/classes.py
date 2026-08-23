from dataclasses import dataclass


@dataclass
class Heading:
  level: int
  text: str


@dataclass
class Text:
  text: str


@dataclass
class Bullet:
  text: str
