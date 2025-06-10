pv=0
cv=1
nv=0
print(pv,"\n",cv)
for i in range(1,9):
    nv=pv+cv
    print(nv)
    pv=cv
    cv=nv