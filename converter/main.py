import json
import sys
from typing import cast

from classes import JsonNode
from render import *

parsed_data = cast(JsonNode, json.load(sys.stdin))
markdown = render(parsed_data)
print(json.dumps(parsed_data, indent=2))
print(markdown, end='')
