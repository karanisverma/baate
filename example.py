"""This code is just sample  structre  of  functioning program.
   It include class  defination, function  declareation, object 
   deceleartion and function call from class fucntion  which is 
   defined out of calss. kuch smajhe :P"""

import datetime
import re

#function defination
def testFun(self, name):
	print "you are awesome %s" %(name)

def testFun2(self, name):
	print "you are a hot chick  %s :P" %(name)
#class for user object
class user(object):
	asignFun = testFun
	asignFun2 = testFun2
	name = 0
	age = 0

karan = user()
karan.name = "Karan Verma"
karan.age = 23
# print karan.age
# print karan.name
s = "cool"
# testFun(karan.name)
karan.asignFun(karan.name)
supi = user()
supi.name = "Suprabha"
supi.age = "44"
supi.asignFun2(supi.name)
# check = karan.asignFun(karan.name)

