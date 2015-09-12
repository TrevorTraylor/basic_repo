x = [random.randint(0,10000) for r in xrange(100)]
for i in range(len(x)):
    a=min(x[i:])
    min_index=x[i:].index(a)
    x[i+min_index]=x[i]
    x[i]=a
print x