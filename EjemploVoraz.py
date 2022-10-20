coins = [1000,500,200,100,50]

def changeMoney(coins, money):
    solution_set = []
    for coin in coins:        
        while money>=coin:
            solution_set.append(coin)
            money -= coin
        if money==0:
            break
    return solution_set

print(changeMoney(coins,1500))
print(f"La cantidad mímina de monedas es:{len(changeMoney(coins,1500))}")
