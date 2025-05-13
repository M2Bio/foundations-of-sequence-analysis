import sys
import xml.etree.ElementTree as ET

def synopsis_enum(filepath):
  try:
    xml_tree = ET.parse(filepath)
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  xml_tree_root = xml_tree.getroot()
  synopsis = dict()
  stack = [(0,xml_tree_root)]
  while stack:
    level, node = stack.pop()
    if level == 1 or level == 2:
      if not 'name' in node.attrib:
        print(node)
      assert 'name' in node.attrib
      synopsis[node.tag] = node.attrib['name']
    elif level > 2:
      assert node.text
      synopsis[node.tag] = node.text.strip()
      if node.tag == 'dedesc':
        # synopsis always stores the name values and node tag of the
        # entire path to this node
        yield synopsis
    children_of_node = list()
    for child in node:
      children_of_node.append((level+1,child))
    # first collect all children and then push them in reversed order so that 
    # the first child is processed before the second children etc
    for child in reversed(children_of_node):
      stack.append(child)
