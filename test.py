wcount={}
txt =  open ("B:\work\whatsapp_app\_biginput.txt","r+")
for w in txt.read().split():
	if w not in wcount:
		wcount[w] = 1
	else:
		wcount[w] +=1

for k,v in wcount.items():
    print k, v