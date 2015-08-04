"""This is class based implimentation of of wp.py python file of this project. kuch smajhe :P"""
# refer it to make class itrable = http://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python
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
output_file = open("Output.txt", "w")
#function defination
def testFun(self, name):
	print "you are awesome %s" %(name)

def testFun2(self, name):
	print "you are a hot chick  %s :P" %(name)
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
class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)

class User(object):
	__metaclass__ = IterRegistry
	_registry = []
	userName=0
	Year={}
	Month={}
	Day={}
	Time={}

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
			timeObj[count] = matchObj.group()
			# print timeObj[count] #for debuggin
			s = s.split()
			# print s #for debuggin
			temp = s[0] + " " + s[1]+" " + s[2]
			datetime.datetime.strptime(temp,'%I:%M%p %d %m')
			if start:
				currentMin    = s[0]
				previousMin   = s[0]

				currentMonth  = s[2]
				previousMonth = s[2]

				currentDate   = s[1]
				previousDate  = s[1]

				currentUser   = s[4]
				previousUser  = s[4]
			else:
				currentMin   = s[0]
				currentDate  = s[1]
				currentMonth = s[2]
				currentUser  = s[4]

			if (currentUser != previousUser):
				if currentUser not in userList:
					userList.append(currentUser)
					previousUser = currentUser
					newUser = currentUser
					newUser = User()
					newUser.name = currentUser
					# print newUser.name

			if (currentMin != previousMin):
				previousMin = s[0]
				chatCountMin = 0
			else:
				chatCountMin += 1
				chatperMin[currentMin] = chatCountMin;
			
			if (currentDate != previousDate):
				chatperDaywithMin[previousDate] = chatperMin
				output_file.write("%s"%chatperDaywithMin)
				previousDate = s[1]	
				chatCountDay  = 0
			else:
				chatCountDay += 1
				chatperDay[currentDate] = chatCountDay;
			
			if (currentMonth != previousMonth):
				#This code block reset all he coding after each month
				previousMonth = s[2]
				chatCount     = 0
				# print "chatting per month", chatperMonth
			else:
				chatCount += 1
				chatperMonth[currentMonth] = chatCount
			start  = False
			count += 1 
for user in User:
	print "loop worked"
	print User.name
	# for k,v in chatperMin.items():
	# 	if (v>mostChatpermin):
	# 		mostChatpermin=v
	# 		mostChatperminTime = k
	# print "Most Chat per Minute = ", mostChatpermin
	# print "Most Chat per Time = ", mostChatperminTime