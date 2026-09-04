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
  return f'**{content}**'


def render_emphasis(node: JsonNode) -> str:
  content = ''
  for child in node.get('children', []):
    if child['kind'] == 'Underscore':
      continue
    elif child['kind'] == 'Markup':
      content = render(child)
  return f'*{content}*'


def render_function(node: JsonNode) -> str:
  content = ''
  fname = ''
  selected = ''
  options = {'highlight': '=='}
  skips = ['Ident', 'LeftBracket', 'RightBracket']
  for child in node.get('children', []):
    if child['kind'] in skips:
      fname = child.get('text')
      if fname is not None:
        selected = options[fname]
      continue
    elif child['kind'] == 'Args' or child['kind'] == 'Markup':
      content = render(child)
  return selected + content[1:-1] + selected


def render(node: JsonNode) -> str:
  if node['kind'] == 'Heading':
    return render_heading(node)

  if node['kind'] == 'Strong':
    return render_strong(node)

  if node['kind'] == 'Emph':
    return render_emphasis(node)

  if node['kind'] == 'Hash':
    return ''

  if node['kind'] == 'FuncCall':
    return render_function(node)

  if 'children' in node:
    return ''.join(render(child) for child in node['children'])

  return node.get('text', '')
