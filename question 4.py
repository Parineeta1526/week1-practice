def calculate_bill(price,quantity):
    total=price*quantity
    if total>=2000:
        discount=total*0.10
    else:
        discount=0
    final_amount=total-discount
    return total,discount,final_amount
product_name=input("Enter product name:")
price=float(input("Enter price per item:"))
quantity=int(input("Enter quantity:"))
total,discount,final_amount=calculate_bill(price,quantity)
print(f"Product name:{product_name}")
print(f"Total:{total}")
print(f"Discount:{discount}")
print(f"Final amount:{final_amount}")