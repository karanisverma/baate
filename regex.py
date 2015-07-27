import re
#!/usr/bin/python
file=open("B:\work\whatsapp app\_biginput.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
    	matchObj = re.match( r'(\d+:\d+)(pm|am), \d+ \w+',word, re.M|re.I)
        if matchObj:
   			print "match --> matchObj.group() : ", matchObj.group()
		else:
   			print "No match!!"
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    if (v>500):
      print k
      print "====="
      print v
