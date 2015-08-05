"""This is class based implimentation of of wp.py python file of this project."""
# refer it to make class itrable = http://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python
#NOTE : Key error is occuring because there is no else condition on newUser[userNumber] segment of code, use userList to find out existing object in list and append new timeObject in the perticuller object.
import datetime
import re


#variable declaration 
timeObj = {}
count = 0
start = True
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
mostChatpermin = 0
chatperDaywithMin = {}
userList = []
userNumber = 0
newUser = {}
sameUserSaying = 0
output_file = open("Output.txt", "w")
#function defination
def testFun(self, name):
	# print "you are awesome %s" %(name)
	pass

def testFun2(self, name):
	# print "you are a hot chick  %s :P" %(name)
	pass
#class for user1 object
class user1(object):
	asignFun = testFun
	asignFun2 = testFun2
	name = 0
	age = 0

karan = user1()
karan.name = "Karan Verma"
karan.age = 23
# print karan.age
# print karan.name
s = "cool"
# testFun(karan.name)
karan.asignFun(karan.name)
supi = user1()
supi.name = "lol"
supi.age = "23"
supi.asignFun2(supi.name)
# check = karan.asignFun(karan.name)

"""--------------------------------"""
# class IterRegistry(type):
#     def __iter__(cls):
#         return iter(cls._registry)


class User(object):
	# __metaclass__ = IterRegistry
	userName = 0
	userdateTime = {}
	userCount = 0
	def __iter__(self):
		for user in dir(User):
			if not user.startswith("__"):
				yield user

# Main busniess logic of program sort of main body
with open ("B:\work\whatsapp_app\_smallinput.txt","r+") as f:
	for line in f:
		##print line
		line = line.replace(",", "")
		line = line.replace("Apr", "4").replace("May", "5")
		# print line
		matchObj = re.match( r'(\d+:\d+)(pm|am) \d+ \d+ - \w+',line, re.M|re.I)
		if matchObj:
			s = matchObj.group()		
			# timeObj[count][count] = matchObj.group()
			# print timeObj[count][count] #for debuggin
			s = s.split()
			# print s #for debuggin
			temp = s[0] + " " + s[1] + " " + s[2]
			timeObj[count] = datetime.datetime.strptime(temp,'%I:%M%p %d %m')
			# print timeObj[count]
			# print timeObj[count].second
			if start:
				currentMin    = timeObj[count].time()
				previousMin   = timeObj[count].time()
				# print currentMin
				# print timeObj[count].minute

				currentMonth  = timeObj[count].month
				previousMonth = timeObj[count].month
				# print currentMonth
				# print timeObj[count].month

				currentDate   = timeObj[count].day
				previousDate  = timeObj[count].day
				# print currentDate
				# print timeObj[count].day

				currentUser   = s[4]
				previousUser  = s[4]

			else:
				currentMin   = timeObj[count].time()
				currentDate  = timeObj[count].day
				currentMonth = timeObj[count].month
				currentUser  = s[4]
				# print currentDate
				# print timeObj[count].day
				# print currentMonth
				# print timeObj[count].month
				# print currentMin
				# print timeObj[count].time()

			if (currentUser != previousUser):
				# print "Use Changed"
				#if new user appears
				# print " if started"
				# print currentUser
				# print previousUser
				if currentUser not in userList:
					userList.append(currentUser)
					previousUser = currentUser
					newUser[userNumber] = User()
					newUser[userNumber].userName = currentUser
					newUser[userNumber].userdateTime[newUser[userNumber].userCount] = timeObj[count]
					# print newUser[userNumber].userName
					print "%s : %s"%(newUser[userNumber].userdateTime[newUser[userNumber].userCount],newUser[userNumber].userName)
					newUser[userNumber].userCount += 1
					userNumber += 1
					# print "From if"
				else:
					#of user already exist
					tmpUserNum = 0
					for existingUser in userList:
						for user in User.__iter__(newUser[tmpUserNum]):
							# if contidion to chack temp user number with existing user
							if (tmpUserNum<userNumber and  existingUser == newUser[tmpUserNum].userName ):
								newUser[tmpUserNum].userdateTime[newUser[tmpUserNum].userCount] = timeObj[count]
								print "%s : %s"%(newUser[tmpUserNum].userdateTime[newUser[tmpUserNum].userCount],newUser[tmpUserNum].userName)
								newUser[tmpUserNum].userCount += 1
								tmpUserNum += 1
			else:
				# print "From else"
				# print "Current user :", currentUser
				# print "previousUser :", previousUser
				# print newUser
				# print newUser[].userCount
				
				for user, val in newUser.items():
					# print val.userCount
					# print valuserName
					# val.userCount += 1
					# print val.userCount
					pass 
				#THIS PART of CODE is really FUCKED UP!
				#FIx IT! Then project is done :P
				#SOLUTION :- 
				#write else condition for condition when same user is saying something in continuation 
				#and assign User Count to the same user again so it will percisely count total number of 
				#line said by each user.		
				print"Same User is saything something"
				sameUserSaying += 1

			if (currentMin != previousMin):
				previousMin = timeObj[count].time()
				chatCountMin = 0
			else:
				chatCountMin += 1
				chatperMin[currentMin] = chatCountMin;
			
			if (currentDate != previousDate):
				chatperDaywithMin[previousDate] = chatperMin
				# output_file.write("%s"%chatperDaywithMin)
				previousDate = timeObj[count].day
				chatCountDay  = 0
			else:
				chatCountDay += 1
				chatperDay[currentDate] = chatCountDay;
			
			if (currentMonth != previousMonth):
				#This code block reset all he coding after each month
				previousMonth = timeObj[count].month
				chatCount     = 0
				# print "chatting per month", chatperMonth
			else:
				chatCount += 1
				chatperMonth[currentMonth] = chatCount
			start  = False
			count += 1 
# for user in User:
# 	print "loop worked"
# 	print UseruserName
	for k,v in chatperMin.items():
		if (v>mostChatpermin):
			mostChatpermin=v
			mostChatperminTime = k
	print "Most Chat per Minute = ", mostChatpermin
	print "Most Chat per Time = ", mostChatperminTime
	tmpUserNum = 0
	for user in User.__iter__(newUser[tmpUserNum]):
		if (tmpUserNum < userNumber):
			print newUser[tmpUserNum].userName
			print newUser[tmpUserNum].userCount
			#print newUser[tmpUserNum].userdateTime
			tmpUserNum += 1
	print sameUserSaying


			# for i in timeObj:
			# 	# print timeObj[i]
			# 	print newUser[userNumber].userdateTime[i]
			# 	print newUser[userNumber]userName
			# 	print count
			# 	print userList