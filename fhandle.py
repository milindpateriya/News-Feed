'''f = open("sp.txt","w+")
f1 = open("ent.txt","w+")
f2 = open("poli.txt","w+")
f3 = open("sci.txt","w+")

for i in range(4):
    f.write("Sports News %d\n"%(i+1))
    f1.write("Entertainment News %d\n"%(i+1))
    f2.write("Politics News %d\n"%(i+1))
    f3.write("Science News %d\n"%(i+1))

f.close()
f1.close()
f2.close()
f3.close()
'''
def readnews(v):
    f=open("%s.txt"%(v),"r")
    news=f.read()
    return news