import random

def rand_codeword(p):

    word = ""
    for i in range(p):
        temp = str(random.randint(0,1))
        word+=temp
    return word

def make_y(x,p):
    y = ""
    for i in range(len(x)):
        check = random.random()
        if check <= p:
            if x[i] == "1":
                y += "0"
            else:
                y += "1"
        else:
            y += x[i]
    return y


n = 15
k = 10
p = 0.015

N = 2000

codeword_list = set()

while len(codeword_list) < pow(2,k):
    word = rand_codeword(n)
    codeword_list.add(word)

Len = len(codeword_list)
E = 0

for i in range(N):
    ip = random.choice(tuple(codeword_list))
    y = make_y(ip,p)

    j = 0
    min = n
    word = ""
    for j in codeword_list:
        dist = 0
        for k in range(n):
            if y[k] != j[k]:
                dist+=1
        if dist<min:
            min = dist
            word = j

    if word != ip:
        E+=1

print(E)

pOfE = E/N

print("P(Error) = ", pOfE)