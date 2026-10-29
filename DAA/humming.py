text=input("Text to encode: ")
chars=[]
freq=[]

for ch in text:
  found=False
  for i in range(len(chars)):
    if chars[i]==ch:
      freq[i]+=1
      found=True
      break
  if not found:
    chars.append(ch)
    freq.append(1)

nodes=[]
for i in range(len(chars)):
  nodes.append([chars[i],freq[i],None,None])

while len(nodes)>1:
  min1=0
  for i in range(1,len(nodes)):
    if nodes[i][1]<nodes[min1][1]:
      min1=i
  left=nodes.pop(min1)
  min2=0
  for i in range(1,len(nodes)):
    if nodes[i][1]<nodes[min2][1]:
      min2=i
  right=nodes.pop(min2)

  new_node=[None,left[1]+right[1],left,right]
  nodes.append(new_node)
root=nodes[0]

codes={}
def generate_code(node,code):
  if node[0] is not None:
    codes[node[0]]=code if code!="" else "0"
    return
  generate_code(node[2],code+"0")
  generate_code(node[3],code+"1")
generate_code(root,"")

print("Huffman Code:")
for ch in chars:
  print(ch," : ",codes[ch])
encoded=""
for ch in text:
  encoded+=codes[ch]
print("Encoded text: ",encoded)
