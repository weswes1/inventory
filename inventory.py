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
	def __init__(self,products=set(),val=0,sellval=0):
		self.val=val
		self.products=products
		self.sellval=sellval

	def addproduct(self,newproduct):
		self.products.add(newproduct)

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
	def __init__(self,address="",rent=0,ID="",invent=set()):
		self.address=""
		self.ID=0
		self.invent=invent
		self.rent=rent

	def addinventory(self,newinventory):
		self.invent.add(newinventory)

	def getinventory(self):
		for inventory in self.invent:
				inventory.getproducts()

	def __str__(self):
		return "Store ID: {} Store Address: {} Store Rent: {} Inventory: ".format(self.ID,self.address,self.rent)



# Create two fruit products, and initialize Them
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

# Create a fruit inventory, and add apples and oranges to it.
print("Below is an inventory of apples and oranges: ")
fruitinvent = inventory()
fruitinvent.addproduct(apples)
fruitinvent.addproduct(oranges)
print("")
fruitinvent.getproducts()
print("")
print("The actual value of the inventory is: {} $ \n".format(fruitinvent.getValue()))
print("The selling value of the inventory is: {} $ \n".format(fruitinvent.getsellValue()))
############
print("Below is a fruit store with the inventory above, an adress, rent, and ID number: \n ")
fruitstore = store()
fruitstore.addinventory(fruitinvent)
fruitstore.ID=9823
fruitstore.address="5659 Sontas Ln., Littleville, California, 94185"
fruitstore.rent=1200

print(fruitstore)
print("")
fruitstore.getinventory()


