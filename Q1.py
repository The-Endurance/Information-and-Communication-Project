from heapq import *
import collections
flag = 0

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

# Encoder function that writes to a file
def encoder(head, s, fout):
    if head == None:
        return

    if head.dat != "#" and head.dat == s:
        fout.write(head.cw)

    encoder(head.left, s, fout)
    encoder(head.right, s, fout)

#Decoder function that is supposed to take an encoded codeword and write the decoded character to a given file
def decoder(head, ch, fout):
    global flag

    if head == None:
        return

    if head.dat != "#" and head.cw == ch:
        fout.write(head.dat)
        flag = 1
        return

    decoder(head.left, ch, fout)
    decoder(head.right, ch, fout)

# MAIN STARTS HERE NOOB

with open('File1.txt', 'r') as info:
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

cd = open("Encoded1.txt", 'w')
rcd = open("Encoded1.txt", 'r')
info = open("File1.txt", 'r')
dcd = open("Decoded1.txt", 'w')
ptext = info.read().lower()
insize = ptext.__len__()
#print(insize)
i = 0
for i in range (insize):
    encoder(nheap._data[0][2], ptext[i], cd)

cur = ""
while 1:
    encoded = rcd.read(1)
    print(encoded)
    if not encoded:
        break
    cur += encoded
    decoder(nheap._data[0][2], cur, dcd)
    if flag == 1:
        flag = 0
        #print(cur)
        cur = ""

rcd.close()
dcd.close()
cd.close()
info.close()

# The encoded files have characters and not bits in them. 
# So for a comparison of file sizes their actual sizes in bytes need be divided by 16.
# This is because each character takes 2 bytes, which is 16 bits instead of the 1 bit they are supposed to take.
# According to this, we get

# Encoded1.txt = 18122/16 = 1132.625 bytes, Initial size of File1.txt = 7245 bytes 
# Encoded2.txt = 27648/16 = 1728 bytes, Initial size of File2.txt = 7149 bytes
# Encoded3.txt = 42057/16 = 2628.5625 bytes, Initial size of File3.txt = 9851 bytes