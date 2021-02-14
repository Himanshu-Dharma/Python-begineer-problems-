
psize = input("select a pizza size s, m ,l == ")
bill = 0

if psize == 's':
    bill = 5
elif psize == 'm':
    bill = 10
elif psize == 'l':
    bill = 15

pep = input("pepperoni? y or n ")
if pep == 'y':
    bill += 5
elif pep == 'n':
    bill += 0

cheese = input('cheese? y or n ')
if cheese == 'y':
    bill += 5
elif cheese == 'n':
    bill += 0

print('final bill is:' + str(bill))
