class Node:
  def __init__(self,chars,freq,left=None,right=None):
    self.chars=chars
    self.freq=freq
    self.left=left
    self.right=right

def find_min(nodes):
  min=0
  for i in range(len(nodes)):
    if nodes[i].freq<nodes[min].freq:
      min=i
  return min

def huffman(chars,freq):
  nodes=[]
  for i in range(len(chars)):
    nodes.append(Node(chars[i],freq[i]))
  while len(nodes)>1:
    m1=find_min(nodes)
    n1=nodes.pop(m1)
    m2=find_min(nodes)
    n2=nodes.pop(m2)
    new_node=Node(n1.chars+n2.chars,n1.freq+n2.freq,n1,n2)
    nodes.append(new_node)
  return nodes[0]

def print_code(node,code=""):
  if node.left is None and node.right is None:
    print(node.chars,":",code)
    return 
  print_code(node.left,code+"0")
  print_code(node.right,code+"1")

chars=['A','B','C','D','E']
freq=[12,15,7,13,9]
result=huffman(chars,freq)
print("\nHuffman Code:")
print_code(result)
  
