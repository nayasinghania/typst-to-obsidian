from typing import NotRequired, TypedDict


class JsonNode(TypedDict):
  kind: str
  text: NotRequired[str]
  children: NotRequired[list['JsonNode']]
