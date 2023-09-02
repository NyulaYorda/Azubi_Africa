
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

#calculate the total price average for all products
price_total= sum(prices)

Average_price = (price_total) / len(prices)

print(' The Average price is : ')

print(Average_price)

#create a new price list that reduces the old prices by $ 5

new_price_list = [item - 5 for item in prices]

print('The new price list :')

print(new_price_list)

#calculate the total revenue generated from the products

d = {
        'Sankofa Foods' :30*2,
        'Jamestown coffee' : 25*3,
        'Bioko chocolate' : 40*5,
        'Blue skies' : 20*8,
        'Fair Afric' : 20*4,
        'Kawa Moka' : 35*4,
        'Aphro Spirit' : 45*6,
        'Mensado':50*2,
        'Voltic' : 35*9,

}
total_revenue = 1

for i in d:
    total_revenue = total_revenue*d[i]

print('total revenue is:')
print(total_revenue)


#calculate the average daily revenue generated from the products

daily_revenue = total_revenue / 7

print('daily revenue is : ')
print(daily_revenue)


#based on the new prices, which products are less than $ 30 


