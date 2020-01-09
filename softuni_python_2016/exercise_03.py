
def get_input_prices():
    input_text = input('Enter a price or "stop": ')
    prices = []
    while input_text != 'stop':
        new_price = None
        try:
            new_price = float(input_text)
        except:
            print('Input could not be parsed. Please choose another.')
            input_text = input('Enter a price or "stop": ')
            continue

        prices.append(new_price)
        input_text = input('Enter a price or "stop": ')
    
    return prices

def main():
    prices = []

    while (len(prices) == 0):
        print('No prices provided. Retry.')
        prices = get_input_prices()

    prices.sort()

    lowest = prices[0]
    while len(prices) > 0 and prices[0] == lowest:
        prices.pop(0)

    highest = None
    if len(prices) > 0:
        highest = prices[-1]
        while len(prices) > 0 and prices[-1] == highest:
            prices.pop(-1)

    if len(prices) == 0:
        print('No values left after trimming lowest and highest prices.')
    else:
        print('''
        Highest price: %.2f
        Lowest price: %.2f
        Average from rest: %.2f
        ''' % (highest, lowest, sum(prices)/max(1, len(prices))))

if __name__ == "__main__":
    main()