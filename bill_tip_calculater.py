print("Bill Split Calculator")
bill_amount = float(input())
tip_percentage = float(input())
num_people = int(input())

tip_amount = (tip_percentage / 100) * bill_amount
total = tip_amount + bill_amount
amount_per_person = total / num_people

print("Total (including tip):",f"${total}")
print("Each person pays:",f"${amount_per_person}" )
