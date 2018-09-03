
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
	def __init__(self,val=0,sellval=0,products=set()):
		self.val=val
		self.products=products
		self.sellval=sellval

	def addproduct(self,newproduct):
		self.products.add(newproduct)

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


class store:
	def __init__(self,address="", ID="",inventory=set(),name=""):
		self.address=address
		self.ID=ID
		self.name=name
		self.inventory=inventory

	def addinventory(self,newinventory):
		self.inventory.add(newinventory)

	def getinventory(self):
		for inventory in self.inventory:
			print(self.inventory)
			inventory.getproducts()
	def __str__(self):
		return "Store ID: {} Store Address: {} Store Inventory: {}  ".format(self.ID,self.address,self.inventory)






