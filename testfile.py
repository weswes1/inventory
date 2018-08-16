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
print("Store Inventory: \n")
fruitstore.getinventory()
print("Value of the inventory of the store: \n")       # I have to use list notation to convert the set to a list

print((list(fruitstore.invent)[0]).getValue())