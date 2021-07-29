#f = open('File1.txt', 'r')
#tx = f.read()
#print(tx)
#f.close()
from heapq import *
import collections
"""
def min_heapify(A,k,key):
    l = left(k)
    r = right(k)
    if l < len(A) and key(A[l]) < key(A[k]):
        smallest = l
    else:
        smallest = k
    if r < len(A) and key(A[r]) < key(A[smallest]):
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A, smallest, key)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def build_min_heap(A, key):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A,k, key)
#Tree
"""

class MyHeap():
    def __init__(self):
       self.key = lambda x:x.freq
       self.index = 0 
       self._data = []

    def push(self, item):
       heappush(self._data, (self.key(item), self.index, item))
       self.index += 1

    def pop(self):
        self.index -= 1
        return heappop(self._data)[2]

class Node:
    def __init__(self, dat, freq):
      self.left = None
      self.right = None
      self.dat = dat
      self.freq = freq
      self.cw = ""
    def __repr__(self):
        return str(self.dat) + " -> " + str(self.freq)


def codegen(head, s):
    #print(head)
    if head == None:
        return
    
    if head.dat != "#":
        head.cw = s
        print(head.dat, "->", head.freq, "\t\t\t", head.cw)
    codegen(head.left, s+"0")
    codegen(head.right, s+"1")


# Reversing a list using reverse()
def Reverse(lst):
    lst.reverse()
    return lst

with open('File3.txt', 'r') as info:
  count = collections.Counter(info.read().lower())
  total = sum(count.values())

ncount = count.most_common()
nheap = MyHeap()
dist = ncount.__len__()
i = 0
for i in range (dist):
    temp = Node(ncount[i][0], ncount[i][1])
    nheap.push(temp)



while nheap.index != 1:
    l = nheap.pop()
    r = nheap.pop()
    temp = Node("#", l.freq+r.freq)
    temp.left = l
    temp.right = r
    nheap.push(temp)

codegen(nheap._data[0][2], "")
#[print(n) for n in nheap._data]

# Huffman

#print("spez")

#build_min_heap(nheap, lambda n : n.freq)

#print("hi")

#while (ncount.__len__() != 0):
  #print("Hey")


