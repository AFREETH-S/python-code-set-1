def profit_units(cost,sell,inventory):
    a=round((sell-cost)*inventory)
    print(a)


cost=float(input("cost_price: "))
sell=float(input("sell_price: "))
inventory=int(input("inventory: "))
profit_units(cost,sell,inventory)
