# rent calculater 

rent=int(input("enter the total rent of hostel flat: "))
food=int(input("enter the total food cost: "))
electricity_spend=int(input("enter the total unit spent: "))
per_unit_charge=int(input("enter per unit charge: "))
person=int(input("enter the the total persons: "))

electricity_bill=electricity_spend*per_unit_charge
total_expences=rent+food+electricity_bill
pay=total_expences/person

print("total expences is ",total_expences)
print("each person has to pay :",pay)


