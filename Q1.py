#f = open('File1.txt', 'r')
#tx = f.read()
#print(tx)
#f.close()
import collections

def min_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l].freq < A[k].freq:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r].freq < A[smallest].freq:
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
   def __init__(self, dat, freq):
      self.left = None
      self.right = None
      self.dat = dat
      self.freq = freq
   def PrintTree(self):
      print(self.dat, "->", freq)


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
i = 0
for i in range (dist):
  nheap.append(Node(ncount[i][0], ncount[i][1]))
# Huffman

build_min_heap(nheap)
#print("hi")
while (ncount.__len__() != 0):
  #print("Hey")
  l = Node(ncount[0][0], ncount[0][1])
  #temp = ncount[0]
  ncount.remove(ncount[0])
  build_min_heap(nheap)
  r = Node(ncount[0][0], ncount[0][1])
  #temp = ncount[0]
  ncount.remove(ncount[0])
  build_min_heap(nheap)
  join = Node('#', l.freq + r.freq)
  join.left = l
  join.right = r
  nheap.append(join)
  build_min_heap(nheap)
print(nheap)