s = "hello world"
c={}
d={}
for x in s:
    c[x]=0
for x in s:
    c[x]+=1
print(c)

# logic 2
for x in s:
    d[x]=d.get(x,0)+1
print(d)