import sqlite3
import datetime
import market

num = 1

utilitymarkup = 0.01
lowercostlimit = 0.06
lowerpricelimit = lowercostlimit + utilitymarkup

uppercostlimit = 0.16
upperpricelimit = uppercostlimit - utilitymarkup

class Mockuser:
	def __init__(self)
		self.userid = str(num)
		num = num + 1
		self.location = 0
		self.max_capacity = randrange(5,20)
		#this is the capacity that the user has available for trading.
		self.avl_capacity = 0 
		#the money the individual holds
		self.capital = 100
		#determins how many KWH can be traded in a single hour
		self.throughputcapacity = 5
		# sell&buy confidences are % offsets from therotical maxs that can be altered by if trades are accepted.
		self.sellconf = random.random()
		self.buyconf = random.random()
		self.buyconf = random.random()
		self.openorder = False


	def makeorder(self):
	
		if avl_capacity == max_capacity & self.openorder == False:
			market.order('sell', upperpricelimit*self.sellconf, self.userid, self.max_capacity, datetime, effectivetill):
			self.openorder = True
		elif avl_capacity != max_capacity & self.openorder == False :
			market.order('buy', lowerpricelimit*self.buyconf, self.userid, (self.max_capacity-self.avl_capacity), datetime, effectivetill):
			self.openorder = True

	def cancelorder(self):


	def tradefulfilled(self, capacity):



