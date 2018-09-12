
from inventory import *
from register import *




# Create fruit & vegetable products
apples = product(4,2,5,"apples")
bannanas = product(2,2,2,"bannanas")
oranges = product(3,5,2,"oranges")
carrots = product(7,3,2,"carrots")
squash = product(9,4,3,"squash")


# print("Testing if the print statement works on a product...")
# print(squash)
# print("Testing if changing book value, changing sell value, and changing quantity work on a product...")
squash.change_price(6)
squash.change_quantity(2)
squash.changevalprice(10)
# print(squash)

# Create a fruit and vegetable inventory, and add the products.

fruitinvent = inventory()
fruitinvent.products.append(apples)
fruitinvent.products.append(oranges)
fruitinvent.products.append(bannanas)
fruitinvent.name="Fruit Inventory"


vegetableinvent = inventory()
vegetableinvent.products.append(squash)
vegetableinvent.products.append(carrots)
vegetableinvent.name="Vegetable Inventory"




# print("Checking if the print statement works on the inventories: \n")

# print(fruitinvent)								
# TODO: Where is the none value coming from ?


# print(vegetableinvent)

# Create a fruit and vegetable store, and test functionality

producestore = store()
producestore.ID = 9823
producestore.address = "5659 Sontas Ln., Littleville, California, 94185"
producestore.name = "Fruit Veg Store"
producestore.inventories.append(fruitinvent)
producestore.inventories.append(vegetableinvent)



storeregister = register({"hundreds":2,"twenties":6,"tens":3,"fives":3,"ones":5,"quarters":1,"dimes":2,"nickels":5,"pennies":12})

producestore.register=storeregister
totalgiven = {"hundreds":0,"twenties":1,"tens":0,"fives":0,"ones":0,"quarters":0,"dimes":0,"nickels":0,"pennies":0}
print("There is {} {} in stock. The bannanas are selling for {} $ each \n".format(fruitinvent.products[2].quantity,fruitinvent.products[2].ide,fruitinvent.products[2].selprice))
print("Attempting to make a sale of 5 bannanas... given {} $ \n".format(getTotal(totalgiven)))
producestore.cashSale("bannanas",5,totalgiven)
print("")
totalgiven = {"hundreds":0,"twenties":0,"tens":0,"fives":0,"ones":0,"quarters":0,"dimes":0,"nickels":0,"pennies":60}
print("Attempting to make a sale of 1 (available) bannana with {} $ \n".format(getTotal(totalgiven)))
producestore.cashSale("bannanas",1,totalgiven)
print("")
print("Attempting to make a sale of an item not in stock... \n")
producestore.cashSale("oranges",1,totalgiven)
print("")
print("Store register state before the succesful sale {}".format(producestore.register.state))
print("Stock of bannanas before the succesful sale: {}".format(fruitinvent.products[2].quantity))
print("")
totalgiven = {"hundreds":0,"twenties":1,"tens":1,"fives":1,"ones":0,"quarters":0,"dimes":0,"nickels":0,"pennies":60}
print("Attempting to make a sale of 1 bannana with enough cash \n")
producestore.cashSale("bannanas",1,totalgiven)
print("")
print("Store register state after the succesful sale {}".format(producestore.register.state))
print("Stock of bannanas after the succesful sale: {}".format(fruitinvent.products[2].quantity))
print("")










"""



# CASE 1: Not enough cash given for the item.

aprice = 1000
testregister=register({"hundreds":2,"twenties":6,"tens":3,"fives":3,"ones":5,"quarters":5,"dimes":5,"nickels":5,"pennies":4})


print("Before the transaction, the register has a total of {} $ and the bills in the register are: {}".format(getTotal(testregister.state),testregister.state))




totalgiven = {"hundreds":1,"twenties":4,"tens":2,"fives":5,"ones":0,"quarters":1,"dimes":3,"nickels":4,"pennies":4}
print("")
print("The total amount of cash given for an item of price: {}$ was {}$".format(aprice,getTotal(totalgiven)))
print("")
print("Let's see if we get an error when we make change for the sale.. \n ")
testregister.makeChange(aprice,totalgiven)
print("")
print("After the attempted sale, the register has a total of {} $ and the bills in the register are {} ".format(getTotal(testregister.state),testregister.state))
print("")
print("That worked... now let's Try another sale. ")



# CASE 2: Enough cash is given, and change is available
print("Before the attempted sale, the register has a total of {} $ and the bills in the register are {} ".format(getTotal(testregister.state),testregister.state))
aprice = 23.45
totalgiven = {"hundreds":0,"twenties":1,"tens":0,"fives":1,"ones":0,"quarters":0,"dimes":0,"nickels":0,"pennies":0}
print("")
print("The total amount of cash given for an item of  price: {}$ was {}$ in the form: {}".format(aprice,getTotal(totalgiven),totalgiven))
print("")
testregister.makeChange(aprice,totalgiven)
print("")
print("")
print("After the attempted sale, the register has a total of {} $ and the bills in the register are {} ".format(getTotal(testregister.state),testregister.state))
print("")
print("")

# CASE 3: Enough money was paid, but the register can not make perfect change. 

testregister=register({"hundreds":2,"twenties":6,"tens":3,"fives":3,"ones":5,"quarters":1,"dimes":2,"nickels":5,"pennies":0})
print("Before the attempted sale, the register has a total of {} $ and the bills in the register are {} ".format(getTotal(testregister.state),testregister.state))
totalgiven = {"hundreds":0,"twenties":0,"tens":0,"fives":1,"ones":0,"quarters":0,"dimes":0,"nickels":0,"pennies":0}
aprice = 4.99
print("The total amount of cash given for an item of  price: {}$ was {}$ in the form: {}".format(aprice,getTotal(totalgiven),totalgiven))
print("")
testregister.makeChange(aprice,totalgiven)
print("")
print("After the attempted sale, the register has a total of {} $ and the bills in the register are {} ".format(getTotal(testregister.state),testregister.state))


"""
