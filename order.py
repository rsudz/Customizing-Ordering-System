import pizzaReceipt

def theOrder():

    TOPPINGS = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")

    SIZES = ("S", "M", "L", "XL")

    pizzaOrder = [] #list gets sent to generateReceipt()

    noPizzaQuestion = ["Q","NO"]
    pizzaSize = ""
    pizzaToppingsList = []

    initialOrderQuestion = input("Do you want to order a pizza? ")
    if initialOrderQuestion.upper() in noPizzaQuestion:
        orderingPizza = False
    else:
        orderingPizza = True

    while orderingPizza == True:
        #ask for pizza size selection
        initialSizeQuestion = input("\nChoose a size: S, M, L, or XL: ")

        #if an invalid size is selected, loop until a valid selection is made
        while initialSizeQuestion.upper() not in SIZES:
            print(" ")
            initialSizeQuestion = input("Choose a size: S, M, L, or XL: ")
            initialSizeQuestion = initialSizeQuestion.upper()

        #save the pizza size selected
        pizzaSize = initialSizeQuestion.upper()

        #ask for toppings
        toppingsPrompt = input(("\nType in one of our toppings to add it to your pizza. To see the list of toppings, enter 'LIST'. When you are done adding toppings, enter 'X' "))

        newTopping = toppingsPrompt.upper()
        orderingToppings = True

        #if user chooses to order toppings
        while orderingToppings == True:

            #if user chooses a topping in topping list
            if newTopping in TOPPINGS:
                pizzaToppingsList.append(newTopping)
                print(" ")
                print(newTopping)
                print ("Added", newTopping.upper(), "to your pizza")
                toppingsPrompt = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter 'LIST'. When you are done adding toppings, enter 'X' ")
                newTopping = toppingsPrompt.upper()

            #if user chooses to view the list
            elif newTopping == "LIST":
                print(" ")
                print(TOPPINGS)
                toppingsPrompt = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter 'LIST'. When you are done adding toppings, enter 'X' ")
                print(newTopping)
                newTopping = toppingsPrompt.upper()

            #if user enters "x" or 'X' to finish adding toppings
            elif newTopping.upper() == "X":
                print("\"X\"\n('")
                orderingToppings = False

            #if user enters an invalid topping (anything other than toppings or list)
            else:
                print("\nThis is not a valid topping option. Please try again.")
                toppingsPrompt = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter 'LIST'. When you are done adding toppings, enter 'X' ")
                newTopping = toppingsPrompt.upper()

        #format the pizza to put into pizzaOrder for generateReceipt()

        thePizza = (pizzaSize.upper(), pizzaToppingsList)
        pizzaOrder.append(thePizza)
        pizzaToppingsList = []

        continueOrder = input("\nDo you want to continue ordering: ")
        continueOrder = continueOrder.upper()
        if continueOrder.upper() in noPizzaQuestion:
            orderingPizza = False
        else:
            orderingPizza = True

        #print receipt
        if orderingPizza == False:
            pizzaReceipt.generateReceipt(pizzaOrder)

theOrder()