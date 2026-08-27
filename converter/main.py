import json
import sys
from typing import cast

from classes import JsonNode

parsed_data = cast(JsonNode, json.load(sys.stdin))
print(json.dumps(parsed_data, indent=2, ensure_ascii=False))
