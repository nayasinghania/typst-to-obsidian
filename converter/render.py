from classes import JsonNode


def render_heading(node: JsonNode) -> str:
  marker = ''
  content = ''

  for child in node.get('children', []):
    if child['kind'] == 'HeadingMarker':
      marker = child.get('text', '')

    elif child['kind'] == 'Markup':
      content = render(child)

  level = len(marker)
  return f'{"#" * level} {content}'


def render_strong(node: JsonNode) -> str:
  content = ''
  for child in node.get('children', []):
    if child['kind'] == 'Star':
      continue
    elif child['kind'] == 'Markup':
      content = render(child)
  return f'{"**"}{content}{"**"}'


def render(node: JsonNode) -> str:
  if node['kind'] == 'Heading':
    return render_heading(node)

  if node['kind'] == 'Strong':
    return render_strong(node)

  if 'children' in node:
    return ''.join(render(child) for child in node['children'])

  return node.get('text', '')
