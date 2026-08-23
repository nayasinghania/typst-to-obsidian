import sys

from lib.convert import parse_line

try:
  filename = sys.argv[1]

  with open(filename, encoding='utf-8') as file:
    source = file.read()

  nodes = [parse_line(line) for line in source.splitlines() if line.strip()]

  for node in nodes:
    print(node)
except IndexError:
  print('Please provide a Typst filename to convert')
except FileNotFoundError:
  print('This Typst file does not exist')
