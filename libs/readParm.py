f=open(r'config\\setParameter.txt')
dat=f.read()
f.close()
print('in readParm.py,print(.txt):\n',dat)

parms=eval(dat)
