
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
		# print("The change due is {}".format(change_due))


		if (totalgiven<price):
			return False									# The total amount is not enough to cover the price. Remove the bills from the register.
			print("Not enough. Transaction cancelled. The price is {} ".format(price))	
			for key in given:
				self.state[key]-=given[key]		

		while (self.state["hundreds"] and round(change_due/100)>=1):       # The total amount is not enough to cover the price. Remove the bills from the register.
			# print("hundred")
			changearr[0]+=1
			self.state["hundreds"]-=1
			change_due-=100
			change_due=round(change_due,2)
		while(self.state["twenties"] and round(change_due/20) >=1):
			# print("twenty")
			changearr[1]+=1
			self.state["twenties"]-=1
			change_due-=20
			change_due=round(change_due,2)
		while(self.state["tens"] and round(change_due/10) >=1):
			# print("ten")
			changearr[2]+=1
			self.state["tens"]-=1
			change_due-=10
			change_due=round(change_due,2)
		while(self.state["fives"] and round(change_due/5) >=1):
			# print("five")
			changearr[3]+=1
			self.state["fives"]-=1
			change_due-=10
			change_due=round(change_due,2)
		while(self.state["ones"] and round(change_due/1,2) >=1):
			# print("one")
			changearr[4]+=1
			self.state["ones"]-=1
			change_due-=1
			change_due=round(change_due,2)
		while(self.state["quarters"] and round(change_due/.25,2) >=1):
			# print("quarter")
			changearr[5]+=1
			self.state["quarters"]-=1
			change_due-=.25
			change_due=round(change_due,2)
		while(self.state["dimes"] and round(change_due/.10,2) >=1):
			# print("dime")
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
			return True
		
			print("Change Distributed, your change is: {} hundred {} twenty {} ten {} five {} one {} quarter {} dime {} nickel {} penny".format(changearr[0],changearr[1],changearr[2],changearr[3],changearr[4],changearr[5],changearr[6],changearr[7],changearr[8]))

			for i in changearr:
				for key in self.state:
					self.state[key]=self.state[key]-changearr[i]


			# Subtract the change array values from the register state 
			changearr=[0,0,0,0,0,0,0,0,0]						# Reset the change array

		elif (change_due>0):
			return False									
			for key in given:
				self.state[key]-=given[key]							# We did not have perfect change for the sale. Return the bills, reset change array.
			print("Not Exact Change. Transaction Cancelled. ")
			changearr=[0,0,0,0,0,0,0,0,0]

	def __str__(self):
		return "Register Total: {} Register state: {}".format(getTotal(self.state),self.state)


def getTotal(thing):
	regtotal=0
	for bills in thing:
		regtotal+=thing[bills]*regVals[bills]
	return regtotal










