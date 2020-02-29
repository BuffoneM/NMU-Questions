def flip(a, b):
    for i in range(a, b + 1):
        coins[i] = not coins[i]


def heads(a, b):
    temp = coins[a:b + 1]
    return temp.count(True)


file = open('Question_2\\q2.in')
string = file.read().replace('\n', ' ').split(' ')

num_coins = int(string.pop(0))
lines = int(string.pop(0))

coins = [False] * num_coins

while (string):
    # print(coins)
    if (string.pop(0) == '1'):
        print(heads(int(string.pop(0)), int(string.pop(0))))
    else:
        flip(int(string.pop(0)), int(string.pop(0)))