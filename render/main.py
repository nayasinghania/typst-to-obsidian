import json
import sys
from pathlib import Path
from typing import cast

from classes import JsonNode
from render import *

if len(sys.argv) < 2:
  raise SystemExit(f'Usage: {sys.argv[0]} <filename>')

filename = Path(sys.argv[1])

parsed_data = cast(JsonNode, json.load(sys.stdin))
markdown = render(parsed_data)

print(json.dumps(parsed_data, indent=2))

output_filename = filename.with_suffix('.md')
_ = output_filename.write_text(markdown, encoding='utf-8')
