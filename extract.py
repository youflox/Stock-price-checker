import time
from scraper import GetStockPrice
from send_email import send
import sys

sys.setrecursionlimit(10**6)

symbols = ['NESTLEIND', 'HINDUNILVR', 'LUPIN', 'CIPLA']
bought_price = [17302.00, 2466.71, 852.19, 617.25]
qty = [2, 2, 2, 3]
current_price = [-2000, -3430, 2340, -20]
margin = [0, 0, 0, 0]


while True:
    h = (time.strftime('%H'))
    m = (time.strftime('%M'))
    d = (time.strftime('%a'))

    greet = f'Hello sir/miss,\nplease find the  current status of your stocks {time.strftime("%c")} below. \n\n'
    header = ("Name          | Current  Price | Gain/Loss      | \n\n")

    f = open('helping.txt', 'w')

    if d != 'Sun' and d !='Sat':
        if 9 <= int(h) <= 15:

            f.write(header)
            for i in range(len(symbols)):
                stock_price = GetStockPrice(symbols[i]).current_price()
                current_price[i] = float(stock_price.replace(",", ""))

                profit = float(current_price[i] - bought_price[i])
                margin[i] = round(profit * qty[i], 2)

            for i in range(len(symbols)):
                f.write( str(symbols[i]) + str(" " * (15 - len(symbols[i]))) + "|  " +
                           str(bought_price[i]) + str(" " * (14 - len(str(bought_price[i])))) + '|  ' +
                           str(margin[i]) + str(" " * (14 - len(str(margin[i]))))  + '\n')

            f.write('-' * 50)
            f.write('\n')
            f.write(" " * 42 + str(round(sum(margin), 2)))
            f.close()

            g = open('helping.txt', 'rt')
            send(g.read())
            f.close()
            print('sent')
            time.sleep(3600)

    time.sleep(((60 - int(m)) * 60) + (24 - int(h)) * 3600)

