
"""This is THE Project NOW :D"""
#Status: User Bug is fixed now have to perfect the 
#NOTE : issue is resolved but still there is a bit of error with 44040 lines of data set i.e. there is difference ( 20752(says sublime) and 20745(says my code) for wiiki and similar in karan) in coint value.
#TODO: resolve above issue by inputting smaller chunks of data at time :P it's going to be painful :'( but there is no other go :P

import datetime
import re
from collections import Counter

#variable declaration 
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
  # return (matchObj)
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
        # print "hr. changed"
        # print "(min value) %s,%s(tmpHour2)"%(min1,tmpHour2)
        if min1 != tmpHour2:
          # print "if condition"
          # print "%s!=%s"%(min1, tmpHour2)
          # print "hr. changed"  
          tmpHour2 = min1
          perhrchat2[min1] = Hrtmpchat2
          Hrtmpchat2 = 0
          hrcount2 += 1
        #print perhrchat
          # print " %s, Date: %s, Month: %s"%(currentMin,currentDate,currentMonth)
        else:
          # print"else condition"
          perhrchat[min1] = Hrtmpchat2
          if( perhrchat[hrcount2] > mostchatperHr ):
            mostchatperHr2 = perhrchat[hrcount2]
            mcphDate = str(currentMin) +" "+ str(currentDate) +" "+ str(currentMonth)
          Hrtmpchat2 += 1
          #print perhrchat
            # print " %s, Date: %s, Month: %s"%(currentMin,currentDate,currentMonth)
          
#function defination
class User(object):
  # __metaclass__ = IterRegistry
  userName = 0
  userdateTime = {}
  userCount = 0
  def __iter__(self):
    for user in dir(User):
      if not user.startswith("__"):
        yield user
year = ngram()
days = ngram()  
with open ("B:\work\whatsapp_app\chatdb\_biginput.txt","r+") as f:
# with open ("B:\work\whatsapp_app\chatdb\chat1.txt","r+") as f:
# with open ("B:\work\whatsapp_app\chatdb\chat2.txt","r+") as f:
# with open ("B:\work\whatsapp_app\chatdb\chat3.txt","r+") as f:
# with open ("B:\work\whatsapp_app\chatdb\chat4.txt","r+") as f:
# with open ("B:\work\whatsapp_app\chatdb\Family.txt","r+") as f:
# with open ("B:\work\whatsapp_app\chatdb\HUIT.txt","r+") as f:
# with open ("B:\work\whatsapp_app\chatdb\kh.txt","r+") as f:
  for line in f:
    ##print line
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
    #words = Counter(w for w in splitObj[len(splitObj)-1].split())
    if matchObj:
      s = matchObj.group()    
      # timeObj[count][count] = matchObj.group()
      # print timeObj[count][count] #for debuggin
      s = s.split()
      if matchObjType:
         temp = s[0] + " " + s[1] + " " + s[2]
         timeObj[count] = datetime.datetime.strptime(temp,'%I:%M%p %d %m')
      else:
        dateSplit = s[0] 
        dateSplit = dateSplit.split('/')
        # print dateSplit
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
#-------------------------------------DAY-----------------------------------------
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
#-------------------------------------DAY-----------------------------------------
        if Day != tmpDate:
            tmpDate = Day
            daycount += 1
            daytmpchat = 0
            daychatmin = 0
            days[currentMonth][currentDate] = daytmpchat
        elif timeObj[count].time() !=daytmptime:
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
#------------------------------------HOUR--------------------------------------
        calcHr(7,4,Min[0])
        if Min[0] != tmpHour:
            # print "hr. changed"  
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

        if (currentUser != previousUser or start == True):
            if currentUser not in userList:
                userList.append(currentUser)
                previousUser = currentUser
                newUser[userNumber] = User()
                newUser[userNumber].userName = currentUser
                newUser[userNumber].userdateTime[newUser[userNumber].userCount] = timeObj[count]    
                newUser[userNumber].userCount += 1
                userNumber += 1
        elif currentUser in userList:
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
            for user, val in newUser.items():
                if(val.userName == currentUser):
                    val.userdateTime[val.userCount]=timeObj[count]
                    val.userCount += 1
                    sameUserSaying += 1
        start  = False
        count += 1 
#   for user in User 
#   print "loop worked"
#   print UseruserName
print "Per Month "
print permonthchat
print "Per Month List"
print tmpMonthList

print "Per Day Dict"
print perdaychat
print "Per Day List"
print tmpdayList

print "per hr chat list"
print tmpPerHrListx`
 
  # print "Per Hr Chat List"
  # print tmpPerHrList
  # print "Per Hr Chat Dict"
  # print perhrchat
  # print "Per Day"
  # print perdaychat
  # print "Per hour"
  # print perhrchat
  # print "Chat min per day"
  # print chatminperday
  # print "total chatting min"
  # print chatmin
  # print "most chat per month = ",mostchatperMonth
  # print mcpmDate
  # print "most chat per day = ",mostchatperDay
  # print mcpdDate
  # print "most chat per hour = ",mostchatperHr
  # print mcphDate
  # print "total words = ",wc

  # for k,v in wcount.items():
  #   print k, v
#   for k,v in chatperMin.items():
#     if (v>mostChatpermin):
#       mostChatpermin=v
#       mostChatperminTime = k
  # print "Most Chat per Minute = ", mostChatpermin
  # print "Most Chat per Time = ", mostChatperminTime
#   tmpUserNum = 0
  
  # while(tmpUserNum<userNumber):
  #   print newUser[tmpUserNum].userName
  #   print newUser[tmpUserNum].userCount
  #   val = newUser[tmpUserNum].userCount - 1
  #   # while(val>1):
    #   print newUser[tmpUserNum].userdateTime[val]
    #   val -= 1

    # output_file.write("%s"%forprocessing )
    #print newUser[tmpUserNum].userdateTime
    # tmpUserNum += 1
  # print perhrchat2
  # print sameUserSaying

      # for i in timeObj:
      #   # print timeObj[i]
      #   print newUser[userNumber].userdateTime[i]
      #   print newUser[userNumber]userName
      #   print count
      #   print userList
  # for k,v in year.items():
  #   print "month = ",k
  #   for x,y in v.items():
  #     print "Day = ", x
  #     print "Hour Chatting = ", y

  # for k,v in days.items():
  #   print "Month= ",k
  #   for x,y in v.items():
  #     print "Date= ",x
  #     print "Chat= ",y

#   print "----------------------------------------------------"
#   hrchatfun(4,7)
#   print "----------------------------------------------------"
#   daychatfun(4)

i = 1
ylimit = 100
test = False
j = 1
listIndex = 1
temp = []
showList = []
showList2 = []

def dictToList(vallist,dict):
    global listIndex
    for k,v in dict.items():
        if listIndex==k:
            vallist.append(v)
            listIndex += 1
    return(vallist)
    listIndex=0

def bargraphList(x, y, height, width, hfactor, barwidth, list):
    
    i = 1
    maxv = 1
    xval = 0
    listLan = 0
    yval = 0
    start = True

    for b in list:
        if y > maxv and b is not None:
            maxv = b
        if b is not None:
            listLan += 1
    
    xUnit = width / listLan
    yUnit = height / (maxv * hfactor)

    for val in list:
        if val is not None:
            xval += xUnit
            if start:
                xval = 0
                start = False
            yval = val * yUnit
            rect(xval + x, y, xUnit / barwidth, -yval)
def setup():
    size(1480, 720)
    stroke(255)

def draw():
    background(0)
#   bargraphList(x, y, height, width, hfactor,barwidth, list)
    bargraphList(100, 300, 720, 1280, 3, 4,  tmpMonthList)
    bargraphList(100, 500, 720 , 1280, 7, 3, tmpdayList)
    bargraphList(100, 700, 720 , 1280, 7, 3, tmpPerHrList)
    
    

def mouseClicked():
    global test
    if(mouseX > 100 and mouseY > 100):
        test = True
    else:
        test = False
    print test
    text("Mouse was clicked", 250, 250)

