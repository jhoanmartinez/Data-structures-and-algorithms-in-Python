import decimal
x=decimal.Decimal(3.14)
y=decimal.Decimal(2.74)
r=x*y
print(r)
decimal.getcontext().prec=4
r=x*y
print(r)
