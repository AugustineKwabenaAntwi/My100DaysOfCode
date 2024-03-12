def peRatio(price,earnings):
    return price/earnings

def pricetobookRatio(price,bookValue):
    return price/bookValue

if __name__ == "__main__":
    with open("Day6\\stocks.csv","r") as stocks, open("Day6\\stocks_solution.csv","w") as output:
        next(stocks) # next() can be used to skip header line
        output.write('Company Name,PE Ratio,PB Ratio\n')
        for lists in stocks:
            stock_port=lists.strip() # removed all the spaces
            stock_port  = stock_port.split(',')

            stock = stock_port[0]
            #converting values from sting to float 
            stock_port[1]= float(stock_port[1]) # price
            stock_port[2] = float(stock_port[2]) # earnings per share
            stock_port[3] = float(stock_port[3]) # book value

            output.write(f'{stock},{round(peRatio(stock_port[1],stock_port[2]),2)},{round(pricetobookRatio(stock_port[1],stock_port[3]),2)}\n')
            



