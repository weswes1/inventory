

regVals = {"hundreds":100,"twenties":20,"tens":10,"fives":5,"ones":1,"quarters":.25,"dimes":.10,"nickels":.05,"pennies":.01}

class register:
	def __init__(self,state={}):
		self.state=state

	def makeChange(self,price,given):

		changearr=[0,0,0,0,0,0,0,0,0]
		totalgiven=0

		for key in given:
			totalgiven+=given[key]*regVals[key]    			# Calculate the total value of the bills that the customer has given to pay,
		
		for key in given:
			self.state[key]+=given[key]								# Add the given bills to the self.state of the register

		change_due=totalgiven-price
		round(change_due,2)


		if (totalgiven<price):										# The total amount is not enough to cover the price. Remove the bills from the register.
			print("Not enough. Transaction cancelled. The price is {} ".format(price))	
			for key in given:
				self.state[key]-=given[key]		

		while (self.state["hundreds"] and round(change_due/100)>=1):       # The total amount is not enough to cover the price. Remove the bills from the register.
			changearr[0]+=1
			self.state["hundreds"]-=1
			change_due-=100
			change_due=round(change_due,2)
		while(self.state["twenties"] and round(change_due/20) >=1):
			changearr[1]+=1
			self.state["twenties"]-=1
			change_due-=20
			change_due=round(change_due,2)
		while(self.state["tens"] and round(change_due/10) >=1):
			changearr[2]+=1
			self.state["tens"]-=1
			change_due-=10
			change_due=round(change_due,2)
		while(self.state["fives"] and round(change_due/5) >=1):
			changearr[3]+=1
			self.state["fives"]-=1
			change_due-=10
			change_due=round(change_due,2)
		while(self.state["ones"] and round(change_due/1) >=1):
			changearr[4]+=1
			self.state["ones"]-=1
			change_due-=1
			change_due=round(change_due,2)
		while(self.state["quarters"] and round(change_due/.25) >=1):
			changearr[5]+=1
			self.state["quarters"]-=1
			change_due-=.25
			change_due=round(change_due,2)
		while(self.state["dimes"] and round(change_due/.10) >=1):
			changearr[6]+=1
			self.state["dimes"]-=1
			change_due-=.10
			change_due=round(change_due,2)
		while(self.state["nickels"] and round(change_due/.05)>=1):
			# print("nickel")
			changearr[7]+=1
			self.state["nickels"]-=1
			change_due-=.05
			change_due=round(change_due,2)
		while(self.state["pennies"] and round(change_due/.01)>=1):
			changearr[8]+=1
			self.state["pennies"]-=1
			change_due-=.01
			change_due=round(change_due,2)

		if (change_due==0):										# We had perfect change for the sale.
		
			print("Change Distributed, your change is: {} hundred {} twenty {} ten {} five {} one {} quarter {} dime {} nickel {} penny".format(changearr[0],changearr[1],changearr[2],changearr[3],changearr[4],changearr[5],changearr[6],changearr[7],changearr[8]))
			changearr=[0,0,0,0,0,0,0,0,0]						# Reset the change array

		elif (change_due>0):									
			for key in given:
				self.state[key]-=given[key]							# We did not have perfect change for the sale. Return the bills, reset change array.
			print("Not Exact Change. Transaction Cancelled. ")
			changearr=[0,0,0,0,0,0,0,0,0]

	def getTotal(self):											# Calculates the total amount of cash in the regitser
			atotal = 0
			for i in self.state:
				atotal+=regVals[i]*self.state[i]
			return atotal


def getTotals(Thing):
	atotal = 0
	for i in Thing:
		atotal+=regVals[i]*Thing[i]
	return atotal

"""
aprice = 1000
print("")
testregister=register({"hundreds":3,"twenties":6,"tens":0,"fives":0,"ones":0,"quarters":1,"dimes":0,"nickels":0,"pennies":4})
print("Before the transaction, the register has {} $ and the bills in the register are: {}".format(testregister.getTotal(),testregister.state))
totalgiven = {"hundreds":1,"twenties":4,"tens":2,"fives":5,"ones":0,"quarters":1,"dimes":3,"nickels":4,"pennies":4}
print("The total amount of cash given for an item of price: {} was {} ".format(aprice,getTotals(totalgiven)))
print("Let's see if we get an error when we make change for the sale.. \n ")
testregister.makeChange(aprice,totalgiven)
print("")
print("After the attempted sale, the register has a total of {} $ and the bills in the register are {} ".format(testregister.getTotal(),testregister.state))
print("")
print("That worked... now let's Try another sale. ")
print("")
"""

print("")
print("")
print("")

testregister=register({"hundreds": 0,"twenties":2,"tens":4,"fives":2,"ones":12,"quarters":1,"dimes":3,"nickels":5,"pennies":2})

totalgiven = {"hundreds":1,"twenties":0,"tens":0,"fives":0,"ones":0,"quarters":0,"dimes":0,"nickels":0,"pennies":0}
anewprice = 99.99

print("The total amount of cash given for an item of price: {} was {} \n".format(anewprice,getTotals(totalgiven)))
print("The bills given to pay were {} ".format(totalgiven))
print("")
print("Before the sale, the register has a total of {} $ and the bills in the register are {} ".format(testregister.getTotal(),testregister.state))
print("")
testregister.makeChange(anewprice,totalgiven)
print("")

print("After the attempted sale, the register has a total of {} $ and the bills in the register are {} ".format(testregister.getTotal(),testregister.state))















