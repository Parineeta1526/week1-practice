name=input("Enter the customer's name:")
units=float(input("Enter the number of units consumed:"))
if units<=100:
    charge=units*2
elif units<=200:
    charge=(100*2)+((units-100)*3)
else:
    charge=(100*2)+(100*3)+((units-200)*5)
if charge>1000:
    surcharge=charge* 0.05
else:
    surcharge=0
final_bill=charge+surcharge
print(f"Customer name:{name}")
print(f"Units Consumed:{units}")
print(f"Electricity Charge:{charge}")
print(f"Surcharge:{surcharge}")
print(f"Final Bill:{final_bill}")