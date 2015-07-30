
#Notes : regex is changes after line number 44041
import datetime
import re
timeObj = {}
count = 0
count2 = 0
n = 0
currentMonth = 0 
previousMonth = 0
chatperMonth={}
monthval=0 #i for month array
start = True
monthDict={}
chatCount = 0

with open ("B:\work\whatsapp_app\_smallinput.txt") as f:
	for line in f:
		count2 += 1
		# print "Count2: ", count2
		line = line.replace(",", "")
		line = line.replace("Apr", "4")
		line = line.replace("May", "5")
		matchObj = re.match( r'(\d+:\d+)(pm|am) \d+ \d+',line, re.M|re.I)
		if matchObj:
			datetime.datetime.strptime(matchObj.group(),'%I:%M%p %d %m') 
			s = matchObj.group()		
			timeObj[count] = matchObj.group()
			print timeObj[count]
			print "value s = ",s.split()
			# print timeObj[count]
			#to find the current month and test current and perivious month
			strSize = len(matchObj.group()) - 1 
			print matchObj.group()[strSize-3]
			#if loop is just starting
			if start:
				currentMonth  = matchObj.group()[strSize]
				previousMonth = matchObj.group()[strSize]
			else:
				currentMonth = matchObj.group()[strSize]

			print "current = ", currentMonth
			print "perivious = ", previousMonth
			
			if (currentMonth != previousMonth):
				#This code block reset all he coding after each month
				monthval +=1
				print "month val = ", monthval
				previousMonth = matchObj.group()[strSize]
				chatCount = 0
				# print "chatting per month", chatperMonth
			else:
				chatCount += 1
				chatperMonth[monthval] = chatCount
			#creating dictnory for each month
			monthDict[monthval]=previousMonth
			print monthDict
			print currentMonth
			#restting start for false after 1st execution
			start = False
			count += 1
			# print "Count1: ",count
		if ((count2-n)!=count):
			print "count1",count
			print "count2",count2
			n+=1
			print "-----"

		# print n
	print "Chatting per month = ", chatperMonth	
			
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