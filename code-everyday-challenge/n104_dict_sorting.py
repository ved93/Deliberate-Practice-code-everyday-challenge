

d = {'pratyush':20, 'ved':25, 'rahul':27, 'abhishek':19,'deepak':7}

l1=d.keys()
l2 = sorted(list(d.values()), reverse=True)

# print(sorted(d.items(), key = lambda k : (k[1],k[0]), reverse=True))
tp =sorted(d.items(), key = lambda k : (k[1],k[0]), reverse=True)
print(d.items())
print(dict(tp))