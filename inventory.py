
"""
 Product Inventory Project - Create an application which manages an inventory of products.
 Create a product class which has a price, id, and quantity on hand. 
 Create a cash Register that keeps trach of totals bills, ect
 Create a sale option that allows for credit cards or cash
 Then create an inventory class which keeps track of various products and can sum up the inventory value.
"""
regVals = {"hundreds":100,"twenties":20,"tens":10,"fives":5,"ones":1,"quarters":.25,"dimes":.10,"nickels":.05,"pennies":.01}


class product:

	def __init__(self,quantity=0,selprice=0,valprice=0,ide=""):
		self.quantity=quantity
		self.selprice=selprice
		self.ide=ide
		self.valprice=valprice

	def change_price(self,newprice):
		self.price = newprice

	def changevalprice(self,newvalprice):
		self.valprice=newvalprice

	def change_quantity(self,newquantity):
		self.quantity=newquantity

	def __str__(self):
		return "ID: {} quantity: {} selling price: {} value price: {}".format(self.ide,self.quantity,self.selprice,self.valprice)


class inventory:
	def __init__(self,val=0,sellval=0,name="",state={}):
		self.products=list()
		self.val=val
		self.sellval=sellval
		self.name=name

	def deleteproduct(self,todelete):
		self.products.remove(todelete)

	def getValue(self):
		for product in self.products:
			self.val+=product.valprice
		return self.val

	def getsellValue(self):
		for product in self.products:
			self.sellval+=product.selprice
		return self.sellval

	def getproducts(self):
		for product in self.products:
			print(product)

	def __str__(self):
		return self.name+str(self.getproducts())

class store:
	def __init__(self,address="", ID="",name="",state={}):
		self.inventories=list()
		self.address=address
		self.ID=ID
		self.name=name
		self.state=state

	def getinventory(self):
		for inventory in self.inventories:
			inventory.getproducts()

	def getproduce(self):
		productlist=[]
		for i in range(0,self.inventories):
			for j in self.inventories[i]:
				pass
		return productlist


	def __str__(self):
		print("Store ID: {} Store Address: {} Store name: {} \n".format(self.ID,self.address,self.name))
		print("Inventories: \n")
		return str(self.getinventory())

	def cashSale(self,item,quantity,cashVals):

			changearr = {"hundreds":0,"twenties":0,"tens":0,"fives":0,"ones":0,"quarters":0,"dimes":0,"nickels":0,"pennies":0}

			totalcashVals = getTotal(cashVals)

			for i in range(0,len(self.inventories)):					#Iterate through inventories and prducts to get a match on the item.

				for j in range(0,len(self.inventories[i].products)):

					if (self.inventories[i].products[j].ide==item and self.inventories[i].products[j].quantity>=quantity and getTotal(cashVals)>=quantity*self.inventories[i].products[j].selprice):	

						change_due=totalcashVals-self.inventories[i].products[j].selprice*quantity
						round(change_due,2)
						
						for key in cashVals:
							self.state[key]+=cashVals[key]	# Add the given bills to the register

						change_due=totalcashVals-self.inventories[i].products[j].selprice*quantity # Calculate change due
						round(change_due,2)

						while (self.state["hundreds"] and round(change_due/100)>=1):      
							print("hundred")
							changearr["hundreds"]+=1
							self.state["hundreds"]-=1
							change_due-=100
							change_due=round(change_due,2)
						while(self.state["twenties"] and change_due/20 >=1):
							print("twenty")
							changearr["twenties"]+=1
							self.state["twenties"]-=1
							change_due-=20
							change_due=round(change_due,2)
						while(self.state["tens"] and change_due/10 >=1):
							print("ten")
							changearr["tens"]+=1
							self.state["tens"]-=1
							change_due-=10
							change_due=round(change_due,2)
						while(self.state["fives"] and change_due/5 >=1):
							print("five")
							changearr["fives"]+=1
							self.state["fives"]-=1
							change_due-=5
							change_due=round(change_due,2)
						while(self.state["ones"] and change_due/1 >=1):
							print("one")
							changearr["ones"]+=1
							self.state["ones"]-=1
							change_due-=1
							change_due=round(change_due,2)
						while(self.state["quarters"] and change_due/.25 >=1):
							print("quarter")
							changearr["quarters"]+=1
							self.state["quarters"]-=1
							change_due-=.25
							change_due=round(change_due,2)
						while(self.state["dimes"] and change_due/.10 >=1):
							print("dime")
							changearr["dimes"]+=1
							self.state["dimes"]-=1
							change_due-=.10
							change_due=round(change_due,2)
						while(self.state["nickels"] and change_due/.05>=1):
							print("nickel")
							changearr["nickels"]+=1
							self.state["nickels"]-=1
							change_due-=.05
							change_due=round(change_due,2)
						while(self.state["pennies"] and change_due/.01>=1):
							changearr["pennies"]+=1
							self.state["pennies"]-=1
							change_due-=.01
							change_due=round(change_due,2)


						if (change_due==0):				# We had perfect change for the sale.

							print("Change Distributed, your change is: {}".format(changearr))
							self.inventories[i].products[j].quantity -= quantity # Decrease the stock of the item quantity by quantity
							changearr={"hundreds":0,"twenties":0,"tens":0,"fives":0,"ones":0,"quarters":0,"dimes":0,"nickels":0,"pennies":0}	# Reset the change array
							

						if (change_due>0):			

							for key in cashVals:
								self.state[key]-=cashVals[key]							# Return the bills, reset change array.

							print("Not Exact Change. Transaction Cancelled. ")
							changearr = {"hundreds":0,"twenties":0,"tens":0,"fives":0,"ones":0,"quarters":0,"dimes":0,"nickels":0,"pennies":0}							# Reset the change array

					
					else:
						pass
					# Invalid Sale





def getTotal(thing):
	regtotal=0
	for bills in thing:
		regtotal+=thing[bills]*regVals[bills]
	return regtotal

