
input_text = input('Enter a price or "stop": ')
prices = []
while input_text != 'stop':
    new_price = None
    try:
        new_price = float(input_text)
    except:
        print('Input could not be parsed. Please choose another.')
        continue

    prices.append(new_price)
    input_text = input('Enter a price or "stop": ')

prices.sort()

lowest = prices[0]
while prices[0] == lowest and len(prices) > 0:
    prices.pop(0)

highest = prices[-1]
while prices[-1] == highest and len(prices) > 0:
    prices.pop(-1)

print('''
Highest price: %.2f
Lowest price: %.2f
Average from rest: %.2f
''' % (highest, lowest, sum(prices)/max(1, len(prices))))