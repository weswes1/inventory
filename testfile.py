
from inventory import *
from register import *




# Create fruit & vegetable products
apples = product(4,2,5,"apples")
oranges = product(3,5,2,"oranges")
carrots = product(7,3,2,"carrots")
squash =product(9,4,3,"squash")


print("Testing if the print statement works on a product...")
print(squash)
print("Testing if changing book value, changing sell value, and changing quantity work on a product...")
squash.change_price(6)
squash.change_quantity(2)
squash.changevalprice(10)
print(squash)

# Create a fruit and vegetable inventory, and add the products.

fruitinvent = inventory()
vegetableinvent=inventory()
fruitinvent.addproduct(apples)
fruitinvent.addproduct(oranges)
vegetableinvent.addproduct(carrots)
vegetableinvent.addproduct(squash)

# Check the selling value and book value of the vegetable inventory
print("")
print("Selling value of the vegetable inventory: {} actual value of the vegetable inventory: {}".format(vegetableinvent.getValue(),vegetableinvent.getsellValue()))
print("")
# Remove carrots from the vegetable inventory, and check the value again.
print("")
print("We removed carrots from the vegetable inventory. Let's check the new book and selling value: ")
print("")
vegetableinvent.deleteproduct(carrots)
print("")
print("Selling value of the vegetable inventory: {} Actual value of the vegetable inventory: {}".format(vegetableinvent.getValue(),vegetableinvent.getsellValue()))



fruitstore = store()
fruitstore.addinventory(fruitinvent)
fruitstore.ID=9823
fruitstore.address="5659 Sontas Ln., Littleville, California, 94185"

print(fruitstore)
print("")
print("Store Inventory: \n")
print("")
fruitstore.getinventory()
print("")
print("Value of the inventory of the store: \n")       # I have to use list notation to convert the set to a list
print((list(fruitstore.inventory)[0]).getValue())



# CASE 1: Not enough cash given for the item.
"""
aprice = 1000
testregister=register({"hundreds":2,"twenties":6,"tens":3,"fives":3,"ones":5,"quarters":1,"dimes":2,"nickels":1,"pennies":4})
print("Before the transaction, the register has a total of {} $ and the bills in the register are: {}".format(testregister.getTotal(),testregister.state))
totalgiven = {"hundreds":1,"twenties":4,"tens":2,"fives":5,"ones":0,"quarters":1,"dimes":3,"nickels":4,"pennies":4}
print("")
print("The total amount of cash given for an item of price: {}$ was {}$".format(aprice,getTotals(totalgiven)))
print("")
print("Let's see if we get an error when we make change for the sale.. \n ")
testregister.makeChange(aprice,totalgiven)
print("")
print("After the attempted sale, the register has a total of {} $ and the bills in the register are {} ".format(testregister.getTotal(),testregister.state))
print("")
print("That worked... now let's Try another sale. ")


# CASE 2: Enough cash is given, and change is available
testregister=register({"hundreds":2,"twenties":6,"tens":3,"fives":3,"ones":5,"quarters":1,"dimes":2,"nickels":5,"pennies":4})
print("Before the attempted sale, the register has a total of {} $ and the bills in the register are {} ".format(getTotals(testregister.state),testregister.state))
aprice = 23.45
totalgiven = {"hundreds":0,"twenties":1,"tens":0,"fives":1,"ones":0,"quarters":0,"dimes":0,"nickels":0,"pennies":0}
print("")
print("The total amount of cash given for an item of  price: {}$ was {}$ in the form: {}".format(aprice,getTotals(totalgiven),totalgiven))
print("")
testregister.makeChange(aprice,totalgiven)
print("")
print("")
print("After the attempted sale, the register has a total of {} $ and the bills in the register are {} ".format(getTotals(testregister.state),testregister.state))


# CASE 3: Enough money was paid, but the register can not make perfect change. 

testregister=register({"hundreds":2,"twenties":6,"tens":3,"fives":3,"ones":5,"quarters":1,"dimes":2,"nickels":5,"pennies":0})
print("Before the attempted sale, the register has a total of {} $ and the bills in the register are {} ".format(getTotals(testregister.state),testregister.state))
totalgiven = {"hundreds":0,"twenties":0,"tens":0,"fives":1,"ones":0,"quarters":0,"dimes":0,"nickels":0,"pennies":0}
aprice = 4.99
print("The total amount of cash given for an item of  price: {}$ was {}$ in the form: {}".format(aprice,getTotals(totalgiven),totalgiven))
print("")
testregister.makeChange(aprice,totalgiven)
print("")
print("After the attempted sale, the register has a total of {} $ and the bills in the register are {} ".format(getTotals(testregister.state),testregister.state))
"""

