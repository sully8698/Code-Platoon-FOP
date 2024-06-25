coins = int(input("Please enter an amount in cents less than a dollar. "))
print(coins)

Q = 0
D = 0
N = 0
P = 0

if coins > 24:
    Q = int(coins / 25)
    coins = coins % 25

if coins > 9:
    D = int(coins / 10)
    coins = coins % 10

if coins > 5:
    N = int(coins / 5)
    coins = coins % 5

if coins > 1:
    P = int(coins / 1)
    coins = coins % 1

print('Your change will be:')
print(f'Q: {Q}')
print(f'D: {D}')
print(f'N: {N}')
print(f'P: {P}')