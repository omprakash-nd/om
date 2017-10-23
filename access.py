class access:
    def __init__(self,comp):
        self.comp = comp
        print "",comp
        
    def getinfo(self):

        name = raw_input("Enter your name:")
        age = raw_input("Enter age:")
        contact = input("Enter contact number:")

def calculateStateTax(price):
    state_sales_tax = .05
    return price * state_sales_tax

def calculateCountyTax(price):
    county_sales_tax =  .025
    return price * county_sales_tax

def displayTotals(price):
    print "Original price:", price
    state_tax = calculateStateTax(price)
    print "State tax:", state_tax
    county_tax = calculateCountyTax(price)
    print "County tax:", county_tax
    print "Total", price + state_tax + county_tax

def main():
    price = float(input('Enter the price of the purchase: '))
    displayTotals(price)
    
ac = access("BILL")
ac.getinfo()        
main()


        

            

        

        
        
        
