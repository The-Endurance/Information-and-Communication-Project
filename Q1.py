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

#Defining a class for the heap
class MyHeap():
    def __init__(self):
       self.key = lambda x:x.freq       #Criteria to use for the min heap
       self.index = 0                   #Number of elements in the heap
       self._data = []                  #Initialising it as an empty heap

    def push(self, item):
       heappush(self._data, (self.key(item), self.index, item))
       self.index += 1

    def pop(self):
        self.index -= 1
        return heappop(self._data)[2]

#Defining a class for nodes of the tree
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
    if head == None:                    #We reach a leaf and are trying to go further
        return
    
    if head.dat != "#":                 #A node that is a leaf, as it has an actual symbol, not '#'
        head.cw = s
        print(head.dat, "->", head.freq, "\t\t\t", head.cw)
    codegen(head.left, s+"0")           #Recursively calling the method onto the two branches of the current leaf
    codegen(head.right, s+"1")


# Reversing a list using reverse()
def Reverse(lst):
    lst.reverse()
    return lst

def encoder(head, s, fout):
    if head == None:
        return

    if head.dat != "#" and head.dat == s:
        fout.write(head.cw)

    encoder(head.left, s, fout)
    encoder(head.right, s, fout)


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

cd = open("Encoded3.txt", 'w')
info = open("File3.txt", 'r')
ptext = info.read().lower()
insize = ptext.__len__()
i = 0
for i in range (insize):
    encoder(nheap._data[0][2], ptext[i], cd)

cd.close()
info.close()

# The encoded files have characters and not bits in them. 
# So for a comparison of file sizes their actual sizes in bytes need be divided by 16.
# This is because each character takes 2 bytes, which is 16 bits instead of the 1 bit they are supposed to take.
# According to this, we get

# Encoded1.txt = 18122/16 = 1132.625 bytes, Initial size of File1.txt = 7245 bytes 
# Encoded2.txt = 27648/16 = 1728 bytes, Initial size of File2.txt = 7149 bytes
# Encoded3.txt = 42057/16 = 2628.5625 bytes, Initial size of File3.txt = 9851 bytes