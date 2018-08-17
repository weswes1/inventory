

regVals = {"hundreds":100,"twenties":20,"tens":10,"fives":5,"ones":1,"quarters":.25,"dimes":.10,"nickels":.05,"pennies":.01}

class register:
	def __init__(self,total=0,state={}):
		self.total=total
		self.state=state
	def makeChange(self,price,given):
		changearr=[0,0,0,0,0,0,0,0,0]
		change_due=given-price
		round(change_due,2)

		if (given<price):
			print("Not enough. The price is {} ".format(price))

		while (self.state["hundreds"] and change_due/100>=1):
			#print(change_due)
			#print("hundred")
			changearr[0]+=1
			self.state["hundreds"]-=1
			change_due-=100
			change_due=round(change_due,2)
			#print(change_due)
		while(self.state["twenties"] and change_due/20>=1):
			#print("twenty")
			changearr[1]+=1
			self.state["twenties"]-=1
			change_due-=20
			change_due=round(change_due,2)
			#print(change_due)

		while(self.state["tens"] and change_due/10>=1):
			#print("ten")
			changearr[2]+=1
			self.state["tens"]-=1
			change_due-=10
			change_due=round(change_due,2)
			#print(change_due)

		while(self.state["fives"] and change_due/5>=1):
			#print("five")
			changearr[3]+=1
			self.state["fives"]-=1
			change_due-=10
			change_due=round(change_due,2)
			#print(change_due)


		while(self.state["ones"] and change_due/1>=1):
			#print("one")
			changearr[4]+=1
			self.state["ones"]-=1
			change_due-=1
			change_due=round(change_due,2)
			#print(change_due)

		while(self.state["quarters"] and change_due/.25>=1):
			#print("quarter")
			changearr[5]+=1
			self.state["quarters"]-=1
			change_due-=.25
			change_due=round(change_due,2)
			#print(change_due)

		while(self.state["dimes"] and change_due/.10>=1):
			#print("dime")
			changearr[6]+=1
			self.state["dimes"]-=1
			change_due-=.10
			change_due=round(change_due,2)
			#print(change_due)

		while(self.state["nickels"] and change_due/.05>=1):
			#print("nickel")
			changearr[7]+=1
			self.state["nickels"]-=1
			change_due-=.05
			change_due=round(change_due,2)
			#print(change_due)

		while(self.state["pennies"] and change_due/.01>=1):
			#print("penny")
			changearr[8]+=1
			self.state["pennies"]-=1
			change_due-=.01
			change_due=round(change_due,2)
			# print(change_due)
		if (change_due==0):
			"""
			print("Change Distributed, your change is: \n{} hundred \n".format(changearr[0]))
			print("{} twenty \n".format(changearr[1]))
			print("{} ten\n".format(changearr[2]))
			print("{} five \n".format(changearr[3]))
			print("{} one \n".format(changearr[4]))
			print("{} quarter \n".format(changearr[5]))
			print("{} dime \n".format(changearr[6]))
			print("{} nickel \n".format(changearr[7]))
			print("{} penny \n".format(changearr[8]))
			"""

			self.total +=price
			self.total = round(self.total)
			changearr=[0,0,0,0,0,0,0,0,0]

		elif (change_due>0):
			print("Not Exact Change")
			self.total+=price
			changearr=[0,0,0,0,0,0,0,0,0]

	def getTotal(self):
			for i in self.state:
				self.total+=regVals[i]*self.state[i]
			return self.total



aregister = register()
aregister.state = { "hundreds":3,"twenties":6,"tens":4,"fives":5,"ones":40,"quarters":6,"dimes":10,"nickels":5,"pennies":15 }
print(aregister.getTotal())
aregister.makeChange(100,500)
print(aregister.getTotal())




