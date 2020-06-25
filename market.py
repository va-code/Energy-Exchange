import sqlite3
import datetime


conn = sqlite3.connect('market.db')

c = conn.cursor()

def main():
	this checks to see actionable orders


def order(buysell, price, userid, capacity, datetime, effectivetill):
	orderlist = (price, userid, capacity, datetime, effectivetill)
	#print(orderlist)
	if buysell == 'buy':
		c.execute("INSERT INTO buyorder VALUES (?, ?, ?, ?, ?)", orderlist)
		conn.commit()
	if buysell == 'sell':
		c.execute("INSERT INTO sellorder VALUES (?, ?, ?, ?, ?)", orderlist)
		conn.commit()



for row in c.execute('SELECT * FROM sellorder ORDER BY price'):
        print(row)


	
###used to initialize the tables that I wanted, no longer need to call every time so they are commented out

#c.execute('''CREATE TABLE buyorder
 #            (price real, userid text, capacity real, Datetime text, Effectivetill text)''')
#c.execute('''CREATE TABLE sellorder
 #            (price real, userid text, capacity real, Datetime text, Effectivetill text)''')
#c.execute("INSERT INTO buyorder VALUES (.023,'admin',5,'now','5 minutes from now')")
#conn.commit()
#conn.close()

#rough demand california in MegaWatts
'''
