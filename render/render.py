from classes import JsonNode
from lorem_gen.generator import LoremGenerator

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
  options = {
    'highlight': '==',
    'lorem': '',
    'lower': '',
    'strike': '~~'
  }
  for child in node.get('children', []):
    if child['kind'] == 'Ident':
      fname = child.get('text', '')
      selected = options[fname]
    elif child['kind'] == 'Args':
      content = render(child)
  if fname == 'lorem':
    length = int(content[1:-1])
    generator = LoremGenerator(words=length)
    return generator.generate()

  return selected + content[1:-1].strip('"').lower() + selected


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

  if node['kind'] == 'Linebreak':
    return '<br/>'

  if 'children' in node:
    return ''.join(render(child) for child in node['children'])

  return node.get('text', '')


# --- Text Types ---
# Highlight (done)
# Line Break (done)
# Lorem (done)
# Lowercase (done)
# Overline
# Raw Text / Code
# Small Capitals
# Smartquote
# Strikethrough (done)
# Subscript
# Superscript
# Text (done)
# Underline
# Uppercase
