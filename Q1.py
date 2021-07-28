#f = open('File1.txt', 'r')
#tx = f.read()
#print(tx)
#f.close()
import collections

def min_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l].data[1] < A[k].data[1]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r].data[1] < A[smallest].data[1]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A, smallest)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def build_min_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A,k)
#Tree

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)


# Reversing a list using reverse()
def Reverse(lst):
    lst.reverse()
    return lst

with open('File3.txt', 'r') as info:
  count = collections.Counter(info.read().lower())
  total = sum(count.values())

ncount = count.most_common()
nheap = []
dist = ncount.__len__()
i = 1
for i in range (dist):
  nheap.append(Node(ncount[i]))
print(nheap[0].data[1])
# Huffman

build_min_heap(nheap)
print("hi")
while (ncount.__len__() != 1):
  l = Node(ncount[0])
  #temp = ncount[0]
  ncount.remove(ncount[0])
  build_min_heap(ncount)
  r = Node(ncount[0])
  #temp = ncount[0]
  ncount.remove(ncount[0])
  build_min_heap(ncount)
  join = Node(['#', l.data[1] + r.data[1]])
  join.left = l;
  join.right = r;
  ncount.append(join)
  build_min_heap(ncount)
#print(ncount)