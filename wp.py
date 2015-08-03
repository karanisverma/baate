
#Notes : regex is changes after line number 44041
import datetime
import re
timeObj = {}
count = 0
count2 = 0
n = 0
start = True
currentMonth = 0 
previousMonth = 0
chatperMonth={}
monthDict={}
mostChatperminTime = 0


chatCount = 0
chatCountDay = 0
chatperDay = {}

chatCountMin= 0
currentMin = 0
previousMin = 0
chatperMin = {}

#temp
fucnTest ={}
chatperX = {}
mostChatpermin=0
#experiment:P
chatperDaywithMin= {}
output_file= open("Output.txt", "w")
with open ("B:\work\whatsapp_app\_smallinput.txt") as f:
	for line in f:
		count2 += 1
		# print "Count2: ", count2
		line = line.replace(",", "")
		line = line.replace("Apr", "4").replace("May", "5")

		matchObj = re.match( r'(\d+:\d+)(pm|am) \d+ \d+',line, re.M|re.I)
		if matchObj:
			datetime.datetime.strptime(matchObj.group(),'%I:%M%p %d %m') 
			s = matchObj.group()		
			timeObj[count] = matchObj.group()
			#print timeObj[count]
			s = s.split()
			#s[0]= time s[1]=date s[2]=month.

			#functional implimentation of code below to count chat per min/hr/day
			# def chatCounter(current, previous, listIndex):
			# 	if (current != previous):
			# 		previous= s[listIndex]
			# 		chatCount = 0
			# 	else:
			# 		chatCount += 1
			# 		chatperX[current] = chatCount
			# 	return chatperX

			# For DEBUGGING purpose
			# print "value s = ",s
			# print timeObj[count]

			#Code to find number of chat perday and permonth
			#when code execute 1st time start is TRUE
			if start:
				currentMin    = s[0]
				previousMin   = s[0]

				currentMonth  = s[2]
				previousMonth = s[2]

				currentDate   = s[1]
				previousDate  = s[1]

			else:
				currentMin   = s[0]
				currentDate  = s[1]
				currentMonth = s[2]
				
			#just for debugging :)
			# print "current = ", currentMonth
			# print "perivious = ", previousMonth
			# print "current Date = ", currentDate
			# print "previousDate = ", previousDate
			#to count number of chat per day
			# print "current  = ", currentMonth
			# print "previous = ", previousMonth

			#fucnTest = chatCounter(currentMonth, previousMonth, 0)
			#Chat count per Min
			if (currentMin != previousMin):
				previousMin = s[0]
				chatCountMin = 0
			else:
				chatCountMin += 1
				chatperMin[currentMin] = chatCountMin;
				
			
			#Chat count per Date
			if (currentDate != previousDate):
				#experiment
				# chatperDaywithMin[previousDate] = chatperMin
				# print "CURRENT DATE = ", previousDate
				# print "CURRENT MONTH = ", currentMonth
				# print chatperMin 
				# print "---------------------"
				# print "---------------------"
				chatperDaywithMin[previousDate] = chatperMin
				output_file.write("%s"%chatperDaywithMin)
				# chatperDaywithMin.clear()
				#chatperMin.clear()
				# print "chat per day with min =", chatperDaywithMin
				previousDate = s[1]	
				chatCountDay  = 0
			else:
				chatCountDay += 1
				chatperDay[currentDate] = chatCountDay;

			#Chat count per Month
			if (currentMonth != previousMonth):

				#This code block reset all he coding after each month
				previousMonth = s[2]
				chatCount     = 0
				# print "chatting per month", chatperMonth
			else:
				chatCount += 1
				chatperMonth[currentMonth] = chatCount
			
		
		
			#creating dictnory for each month
			# monthDict[currentMonth]=previousMonth
			# print monthDict
			# print currentMonth
			#restting start for false after 1st execution
			start  = False
			count += 1
			# print "Count1: ",count
			
		#To check lines with sublime text numbers of lines
		# if ((count2-n)!=count):
		# 	print "count1",count
		# 	print "count2",count2
		# 	n+=1
		# 	print "-----"

		# print n

	
	# print "date = ",s[1]
	# print "Chatting per day = ", chatperDay[0]
	#print "Chatting per month = ", chatperMonth	
	
	#print "Chatting per day = ", chatperDay
	#print "Chatting per min = ", chatperMin
	#print "chat per day with min =", chatperDaywithMin
	for k,v in chatperMin.items():
		if (v>mostChatpermin):
			mostChatpermin=v
			mostChatperminTime = k
	print "Most Chat per Minute = ", mostChatpermin
	print "Most Chat per Time = ", mostChatperminTime
 			

	# for  k,v in chatperDay.items():
	#  	print k , v 
	# print "function test values= ", fucnTest
	
		# else: 
		# 	print "no match found" 
		# 	#print count
			# if (count == 154):
			# 	timediff = timeObj[153]-timeObj[0]
			# 	print timediff

			# print " ", matchObj.group()

		# print line


#regular expression of date (\d+:\d+)(pm|am),