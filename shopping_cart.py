# shopping_cart.py
#This will be displayed on the top of the receipt
import datetime
now=datetime.datetime.now()

#This downloads the csv file filled with product information
import pandas as pd
products_df = pd.read_csv("https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.csv")


#This part converts the dataframe to a dictionary so the code can process the information easier
products=products_df.to_dict('records')


    # FYI: this wget command is a terminal command, NOT python
    # ... in colab, we can execute terminal commands by prefixing them with an exclamation point
    # ... students are not responsible for knowing terminal commands like this
    #!wget -q $url 

#products = [
#    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
#    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
#    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
#    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
#    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
#    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
#    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
#    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
#    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
#    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
#    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
#    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
#    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
#    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
#    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
#    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
#    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
#    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
#] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#This part defines the to_usd function, which converts float to currency
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

#Defining list a, which collects the item's prices
a=[]

#Definint list b, which collects the item's names
b=[]

#Defining list c, which collects the item's prices as USD to be displayed
c=[]

#Establishes user input and repeats prompt endlessly until the user enters 0
numb=int(input("Please scan the item or if you are finished, enter '0': "))
while numb != 0:
    count=0
    for item in products:
        if numb==item["id"]:
            #The Append functions saves the items checked out by the user
            a.append(item["price"])
            b.append(item["name"])
            count=count+1
    if count==0:
        numb=int(input("Hey, are you sure that product identifier is correct? Please try again!"))
        #This if statement makes makes sure you entered a product id that is in the product csv file
    else:
        numb=int(input("Please scan the item or if you are finished, enter '0': "))


 

#This prints the receipt
else: 
    print("-------------------") 
    print("-------------------") 
#This calls the imported date/time function
    print(now.strftime("%Y-%m-%d %H:%M:%S")) 
    print("Joe's Market") 
    print("3700 O Street NW, Washington, DC 20007")
    print("JoesMarket.com")
    print("-------------------") 
    print("-------------------")
#The for look converts the prices to USD so they can be displayed that way 
    for item in a:
        dollar_price=to_usd(item)
#I seperate them to list C so I can still do calculations with list A
        c.append(dollar_price)
#This prints the items bought and their price
    for item_b, item_c in zip(b, c):
        print(item_b, item_c)
#This calculates the Sum_total
    sum_prices=(sum(a)) 
    print("-------------------")
    print("Your subtotal is ", to_usd(sum_prices))
    #    
#Since sum_prices is saved as a float, I use it to calculate the total with tax
    tax_perc=.0875
    tax=sum_prices*tax_perc
    tax_as_dollars=to_usd(tax)
    print("Sales Tax: ", tax_as_dollars)
#Once Sales Tax is calculate, I add it to the subtotal and present the final cost
    Total_Cost=sum_prices+tax
    print("Your total cost is", to_usd(Total_Cost))
    print("-------------------")
#Thank you message
    print("Thank you for shopping at Joe's Market, come again!")
    print("-------------------") 
    print("-------------------") 