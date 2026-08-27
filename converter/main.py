import json
import sys
from typing import cast

from classes import JsonNode
from render import *

parsed_data = cast(JsonNode, json.load(sys.stdin))
markdown = render(parsed_data)

print("--------------------")
print("Parsed Typst source:")
print("--------------------\n")
print(json.dumps(parsed_data, indent=2))
print("\n----------------------------")
print("Converted Obsidian Markdown:")
print("----------------------------\n")
print(markdown, end='')
