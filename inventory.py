"""
 Product Inventory Project - Create an application which manages an inventory of products.
 Create a product class which has a price, id, and quantity on hand. 
 Then create an inventory class which keeps track of various products and can sum up the inventory value.
"""

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
	def __init__(self,products=set(),val=0):
		self.val=val
		self.products=products

	def addproduct(self,newproduct):
		self.products.add(newproduct)

	def getValue(self):
		for product in self.products:
			self.val+=product.valprice
		return self.val

	def getproducts(self):
		for product in self.products:
			print(product)




apples = product()
oranges = product()

apples.ide="apples"
apples.quantity=1
apples.price=2
apples.valprice=1
apples.selprice=2

oranges.ide="oranges"
oranges.quantity=1
oranges.price=2
oranges.valprice=1
oranges.selprice=2

# print(apples)
# print(oranges)

fruitinvent = inventory()

fruitinvent.addproduct(apples)
fruitinvent.addproduct(oranges)

print(fruitinvent.getproducts())

print(fruitinvent.getValue())


