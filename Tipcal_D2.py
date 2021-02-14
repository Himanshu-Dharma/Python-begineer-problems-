total = int(input("enter totla bill"))
tip = int(input("input tip 11,12,15% "))

final_tip = (total * tip)/100
f_bill = total + final_tip

nump = int(input("enter number of people"))

split = f_bill/nump
print(split)
