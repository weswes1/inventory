
"""
 Product Inventory Project - Create an application which manages an inventory of products.
 Create a product class which has a price, id, and quantity on hand. 
 Create a cash Register that keeps trach of totals bills, ect
 Create a sale option that allows for credit cards or cash
 Then create an inventory class which keeps track of various products and can sum up the inventory value.
"""

from register import *

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
	def __init__(self,val=0,sellval=0,name=""):
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
	def __init__(self,address="", ID="",name=""):
		self.inventories=list()
		self.register=register()
		self.address=address
		self.ID=ID
		self.name=name

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
		isValid = False
		for i in range(0,len(self.inventories)):
			for j in range(0,len(self.inventories[i].products)):
				if (self.inventories[i].products[j].ide==item and self.inventories[i].products[j].quantity>= quantity and getTotal(cashVals)>=quantity*self.inventories[i].products[j].selprice):
					isValid = True
					print("The check has passed.")
																				# Decrease the stock of the item quantity by quantity
					self.inventories[i].products[j].quantity-=quantity
					self.register.makeChange(self.inventories[i].products[j].selprice*quantity,cashVals)
					# print("Found a match, and we have enough stock")

		if (isValid==False):
			print("No match found, not enough stock of the item, not enough cash, or not perfect change")


