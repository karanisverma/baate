import datetime
import re
timeObj = {}
count = 0
count2 = 0
n=0
with open ("B:\work\whatsapp_app\_smallinput.txt") as f:
	for line in f:
		count2 += 1
		# print "Count2: ", count2
		line = line.replace(",", "")
		line = line.replace("Apr", "4")
		matchObj = re.match( r'(\d+:\d+)(pm|am) \d+ \d+',line, re.M|re.I)
		if matchObj:
			timeObj[count] = datetime.datetime.strptime(matchObj.group(),'%I:%M%p %d %m') 
			print timeObj[count]
			print matchObj.group()
			count += 1
			print "Count1: ",count
		if ((count2-n)!=count):
			print "count1",count
			print "count2",count2
			n+=1
			print "-----"
		print n
			
			
		# else: 
		# 	print "no match found" 
		# 	#print count
			# if (count == 154):
			# 	timediff = timeObj[153]-timeObj[0]
			# 	print timediff

			# print " ", matchObj.group()

		# print line

#Working demo only with time after text modification
# textfile = open("B:\work\whatsapp_app\_smallinput.txt","r+")
# timeObj = {}
# count = 0
# for word in textfile.read().split():
# 	time = re.match(r'((\d+:\d+)(pm|am),)',word)
# 	if time:
# 		word=word.replace(",","")
# 		print word
# 		timeObj[count] = datetime.datetime.strptime(word,'%I:%M%p')
# 		count = count + 1
# 		print "-------------"
# 		print count
# 		if count == 100:
# 			timediff = timeObj[99]-timeObj[0]
# 			print timediff
# 		# continue
# 	# print word
# 	if (count==100):
# 		break


#regular expression of date (\d+:\d+)(pm|am),