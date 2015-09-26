#NOTE: Replace file text file location according to your dictory in line number 138 (your whatsapp chat backup file in txt format)
#Output: This program will return list of chat done between two use on per Month, Day, Hr, Minute
import datetime
import re
from collections import Counter

tmpMonthList = [None]*12
tmpdayList =  [None]*90
tmpPerHrList = [None]*1000
timeObj = {}
count = 0
wc = 0
chatmin = 0
wcount = {}
chatwordlist ={}
daychatmin = 0
start = True
tmpHour2 = 0
count2 = 0
Hrtmpchat2=0
hrcount2 = 0
perhrchat2 = {}
tmpchat = 0
tmptime = 0
daytmptime = 0
daytmpchat = 0
Hrtmpchat = 0
hrcount = 0
tmpMin = 0
tmpHour = 0
tmpDate = 0
tmpMonth= 0
mostchatperHr = 0
mostchatperDay = 0
mostchatperMonth = 0
daycount = 0
monthcount= 0
perdaychat = {}
perhrchat = {}
permonthchat = {}
chatminperday = {}
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
matchObjType= False
ex1 = 0
everything ={}
class ngram(dict):
    """Based on perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return super(ngram, self).__getitem__(item)
        except KeyError:
            value = self[item] = type(self)()
            return value
def hrchatfun(month,day):
	for k,v in year.items():
		if k == month:
			print "month = ",k
			for x,y in v.items():
				if x == day :
					print "Day = ", x
					for hr,linechat in y.items():
						print "Hr = ",hr
						print "Line Chatting = ",linechat
def daychatfun(month):
	for k,v in days.items():
		if k == month:
			print "Month = ",
			for x,y in v.items():
				print "day = ", x
				print "Line of chats = ", y

def matchfun(line):
	matchObj = re.match(r'(\d+:\d+)(pm|am) \d+ \d+ - \w+',line, re.M|re.I)
	splitObj = re.split(r'(\d+:\d+)(pm|am) \d+ \d+ - \w+', line)
	matchObj2 = re.match(r'(\d+/\d+/\d+) \d+:\d+ (PM|AM) - \w+',line, re.M|re.I)
	splitObj2 = re.split(r'(\d+/\d+/\d+) \d+:\d+ (PM|AM) - \w+',line)
	if matchObj:
		matchObjType = True
		return (matchObj, matchObjType,splitObj)
	elif matchObj2:
		matchObjType = False
		return (matchObj2, matchObjType,splitObj2)
	else:
		matchObjType = None
		return (matchObj, matchObjType,splitObj)


def calcHr(date,month,min1):
	global Hrtmpchat2
	global hrcount2
	global tmpHour2
	
	if date==currentDate and month == currentMonth:
				if min1 != tmpHour2:	
					tmpHour2 = min1
					perhrchat2[min1] = Hrtmpchat2
					Hrtmpchat2 = 0
					hrcount2 += 1
				else:
					perhrchat[min1] = Hrtmpchat2
					if( perhrchat[hrcount2] > mostchatperHr ):
						mostchatperHr2 = perhrchat[hrcount2]
						mcphDate = str(currentMin) +" "+ str(currentDate) +" "+ str(currentMonth)
					Hrtmpchat2 += 1
										
class User(object):
	userName = 0
	userdateTime = {}
	userCount = 0
	def __iter__(self):
		for user in dir(User):
			if not user.startswith("__"):
				yield user

year = ngram()
days = ngram()

with open ("B:\work\Projects\whatsapp_app\chatdb\_biginput.txt","r+") as f:
	for line in f:
		
		line = line.replace(",", "")
		line = line.replace("Apr", "4").replace("May", "5")
		matchObj, matchObjType, splitObj = matchfun(line)
		wordlist = splitObj[len(splitObj)-1].split()
		for w in wordlist:
			if w not in wcount:
				wcount[w] = 1
			else:
				wcount[w] +=1
			wc+=1
		if matchObj:
			s = matchObj.group()		
			s = s.split()
			if matchObjType:
	 			temp = s[0] + " " + s[1] + " " + s[2]
	 			timeObj[count] = datetime.datetime.strptime(temp,'%I:%M%p %d %m')
	 		else:
	 			dateSplit = s[0] 
	 			dateSplit = dateSplit.split('/')
	 			try:
	 				dateSplit1 = s[1] + s[2] + " " + dateSplit[1] + " " + dateSplit[0]
	 				timeObj[count] = datetime.datetime.strptime(dateSplit1,'%I:%M%p %d %m')
	 			except ValueError:
	 				dateSplit2 = s[1] + s[2] + " " + dateSplit[0] + " " + dateSplit[1]
	 				timeObj[count] = datetime.datetime.strptime(dateSplit2,'%I:%M%p %d %m')
	
	 		if timeObj[count].time() !=tmptime:
	 			tmptime = timeObj[count].time()
	 			chatmin += 1

			if start:
				currentMin    = timeObj[count].time()
				previousMin   = timeObj[count].time()
			
				currentMonth  = timeObj[count].month
				previousMonth = timeObj[count].month
			
				currentDate   = timeObj[count].day
				previousDate  = timeObj[count].day
			
				currentUser   = s[4]
				currentUser   = currentUser.lower()
				previousUser  = s[4]

				tmpMonth = str(currentMonth)
				tmpDate  = str(currentDate)
				

			else:
				currentMin   = timeObj[count].time()
				currentDate  = timeObj[count].day
				currentMonth = timeObj[count].month
				currentUser  = s[4]
				currentUser  = currentUser.lower() 
			
			Min = str(currentMin).split(':')
			Day = str(currentDate)
			Month = str(currentMonth)			
#For MONTH

			if Month != tmpMonth:
				tmpMonth = Month
				monthcount += 1
				tmpchat = 0

			else:
				tmpchat += 1
				permonthchat[monthcount]= tmpchat
				everything[monthcount]=tmpchat
				tmpMonthList[monthcount] = tmpchat

				if (permonthchat[monthcount] > mostchatperMonth):
					mostchatperMonth = permonthchat[monthcount]
					mcpmDate = str(currentMin) +" "+ str(currentDate) +" "+ str(currentMonth)
#For DAY
			if Day != tmpDate:
				tmpDate = Day
				daycount += 1
				daytmpchat = 0
				daychatmin = 0
				days[currentMonth][currentDate] = daytmpchat
			else:

				if timeObj[count].time() !=daytmptime:
	 				daytmptime = timeObj[count].time()
	 				daychatmin += 1
	 				chatminperday[daycount] = daychatmin
				daytmpchat += 1
				perdaychat[daycount] = daytmpchat
				days[currentMonth][currentDate] = daytmpchat
				tmpdayList[daycount]  = daytmpchat
				if (perdaychat[daycount] > mostchatperDay):
					mostchatperDay = perdaychat[daycount]
					mcpdDate = str(currentMin) +" "+ str(currentDate) +" "+ str(currentMonth) 
#For HOUR
			calcHr(7,4,Min[0])
			if Min[0] != tmpHour:	
				tmpHour = Min[0]
				perhrchat[hrcount] = Hrtmpchat
				tmpPerHrList[hrcount] =Hrtmpchat
				year[currentMonth][currentDate][Min[0]] = Hrtmpchat
				Hrtmpchat = 0
				hrcount += 1
			else:
				perhrchat[hrcount] = Hrtmpchat
				tmpPerHrList[hrcount] =Hrtmpchat
				year[currentMonth][currentDate][Min[0]] = Hrtmpchat
				if( perhrchat[hrcount] > mostchatperHr ):
					mostchatperHr = perhrchat[hrcount]

					mcphDate = str(currentMin) +" "+ str(currentDate) +" "+ str(currentMonth)
				Hrtmpchat += 1

			"""This block will execute when chatting user will change"""
			if (currentUser != previousUser or start == True):
				"""This block will execute when user is NEW"""
				if currentUser not in userList:
					userList.append(currentUser)
					previousUser = currentUser
					newUser[userNumber] = User()
					newUser[userNumber].userName = currentUser
					newUser[userNumber].userdateTime[newUser[userNumber].userCount] = timeObj[count]
					newUser[userNumber].userCount += 1
					userNumber += 1
				elif currentUser in userList:
					"""This block will execute when user is NOT new"""

					previousUser = currentUser
					tmpUserNum = 0
					for user in User.__iter__(newUser[tmpUserNum]):
						if (tmpUserNum<userNumber and  currentUser == newUser[tmpUserNum].userName):
							newUser[tmpUserNum].userdateTime[newUser[tmpUserNum].userCount] = timeObj[count]
							newUser[tmpUserNum].userCount += 1
							tmpUserNum += 1
						else:
							tmpUserNum += 1
			else:
				"""This block will execute when previous User is saying something in continuation in next line """			
				for user, val in newUser.items():
					if(val.userName == currentUser):
						val.userdateTime[val.userCount]=timeObj[count]
						val.userCount += 1
				sameUserSaying += 1
			start  = False
			count += 1 
	print "Chat Per Month "
	print permonthchat
	print "Per Month List"
	print tmpMonthList
	print "Per Day List"
	print tmpdayList
	print "Per Day Dict"
	print perdaychat
	print "Per Hr Chat List"
	print tmpPerHrList
	print "Per Hr Chat Dict"
	print perhrchat
	for k,v in chatperMin.items():
		if (v>mostChatpermin):
			mostChatpermin=v
			mostChatperminTime = k
	print "Most Chat per Minute = ", mostChatpermin
	print "Most Chat per Time = ", mostChatperminTime
	tmpUserNum = 0
	print "Finction call to show sepcific day chatting per hr"
	hrchatfun(4,7)
	print "Finction call to show sepcific day chatting per hr"
	daychatfun(4)