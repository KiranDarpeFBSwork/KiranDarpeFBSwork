#calculate selling price of book based on cost price and discount.
cost_price=int(input("Enter Cost of book price:"))
dis=int(input("Enter the discount:"))
selling_price=cost_price*(1-(dis/100))
print(f"selling price of book is:{selling_price}")