#Rayne Sutherland 251074382

def generateReceipt(pizzaOrder): #function takes in single parameter of pizza order

   #costs of pizza and additional toppings 
   pizzaCosts = (7.99, 9.99, 11.99, 13.99)
   additionalToppingCosts = (0.50, 0.75, 1, 1.25)

   if len(pizzaOrder) == 0: 
    print("You did not order anything")
   
   else: 
    print("Your order: ")

    totalPizzaCostBeforeTax = 0
    for pizza in range(len(pizzaOrder)):
        
        #if the pizza chosen is a small
        if pizzaOrder[pizza][0] == "S":
            i = 0
        
        #if the pizza chosen is a medium
        elif pizzaOrder[pizza][0] == "M":
            i = 1
        
        #if the pizza chosen is a large 
        elif pizzaOrder[pizza][0] == "L":
            i = 2
        
        #if the pizza chosen is a extra large 
        elif pizzaOrder[pizza][0] == "XL":
            i = 3
        
        #save the base cost of the pizza 
        baseCost = pizzaCosts[i]

        #print first line of receipt
        print("Pizza" + str(pizza+1) + ": " + str(pizzaOrder[pizza][0] + " 				  " + "%.2f" % baseCost))

        #save number of toppings 
        numToppings = len(pizzaOrder[pizza][1])
        if numToppings > 3: 
            numAdditionalToppings = numToppings - 3
        else: 
            numAdditionalToppings = 0
        
        #save the price of the additional toppings 
        extraToppingPrice = additionalToppingCosts[i]

        #print toppings
        for topping in range(numToppings): 
            print ("- " + pizzaOrder[pizza][1][topping])
        
        while numToppings > 3: 
            print("Extra Topping (" + str(pizzaOrder[pizza][0]) + ")" + "		   " + "%.2f" % extraToppingPrice)
            numToppings -= 1
            
        #calculate total pizza cost before tax
        pizzaCostBeforeTax = baseCost + (numAdditionalToppings * extraToppingPrice)
        totalPizzaCostBeforeTax += pizzaCostBeforeTax

    #calculate and print tax
    tax = totalPizzaCostBeforeTax * 0.13
    print("Tax:					   ", "%.2f" % tax)

    #calculate and print total cost
    totalCost = totalPizzaCostBeforeTax + tax
    print("Total:					  ", "%.2f" % totalCost)