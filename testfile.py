
from inventory import *
from register import *




# Create fruit & vegetable products
apples = product(4,2,5,"apples")
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
fruitinvent.products.add(apples)
fruitinvent.products.add(oranges)
fruitinvent.name="Fruit Inventory"

# print("Checking if the print statement works on the inventories: \n")

print(fruitinvent)								
# TODO: Where is the none value coming from ?


# print(vegetableinvent)

# Create a fruit and vegetable store, and test functionality

fruitstore = store()
fruitstore.ID = 9823
fruitstore.address = "5659 Sontas Ln., Littleville, California, 94185"
fruitstore.name = "Great Melons Fruit Store"
fruitstore.inventories.add(fruitinvent)


fruitregister=register({"hundreds":2,"twenties":6,"tens":3,"fives":3,"ones":5,"quarters":1,"dimes":2,"nickels":5,"pennies":0})
fruitstore.register = fruitregister
print(fruitstore.register)




"""
## 					TODO: Where is the none value coming from in my dictionary?


print(" \n \n \n")

veggiestore = store()
veggiestore.ID = 6234
veggiestore.address = "34543 Gashwell Street, New York, New York, 04185"
veggiestore.name = "Great Vegetables Store"
veggiestore.inventories.add(vegetableinvent)
print(veggiestore)








































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
