seq = input()
rseq = ""

for x in seq:
    rseq = x + rseq

AA = input()
BB = input()
rAA = ""
rBB = ""
for x in AA:
    rAA = x + rAA

for x in BB:
    rBB = x + rBB
startA = seq.find(AA)
endA = len(seq) - 1 - rseq.find(rAA)

leng = len(seq)

startB = seq.find(BB)
endB = len(seq) - 1 - rseq.find(rBB)

rStartA = rseq.find(AA)
rEndA = leng - 1 - seq.find(rAA)

rStartB = rseq.find(BB)
rEndB = leng - 1 - seq.find(rBB)

print(startA,endA)