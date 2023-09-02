print("Welcome to Asanka Hotel Tip Calculator")
#Get the total  bill for the meal
bill = float(input("What was the total bill of your meal? $"))

tip_percentage = .18
sales_tax = .07

#calculate the 18% tip 
tip = (bill * tip_percentage)
#print('the tip is $' float{tip})

#calculate the 7% sales tax
sales_tax = (bill * sales_tax)
#print('The sales tax due is $' + sales_tax)

#calculate the total sale
total_sale = ( bill + tip + sales_tax)

print('\nCharge for food = $', format(bill, ',.2f'), sep='')
#Bill= $----9,9384.00
print('Tip = $', format(tip, ',.2f'), sep='')
print('Sales tax = $', format(sales_tax, ',.2f'), sep='')
print('Grand total = $', format(total_sale, ',.2f'), sep='', end='\n\n')

