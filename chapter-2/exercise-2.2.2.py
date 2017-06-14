"""
exercise-2.2.2

Suppose the cover price of a book is $24.95, but bookstores 
get a 40% discount. Shipping costs $3 for the first copy 
and 75 cents for each additional copy. What is the total 
wholesale cost for 60 copies?

"""

# input values
mrp = 24.95           # single price in usd
discount = 40.0       # in percentages (%)
copies = 60.0

# calculations
unit_price = mrp - mrp * discount / 100
total = unit_price * 60

shipping = 3 + 0.75 * (copies - 1)
grand_total = total + shipping

print("total wholesale cost for 60 copies is $", round(grand_total, 2))

