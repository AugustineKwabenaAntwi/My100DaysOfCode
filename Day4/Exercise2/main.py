stock_prices = {
    "info":[600,630,620],
    "ril":[1430,1490,1567],
    "mtl":[234,180,160]
    }

choice = input("Enter the operation you want\nprint\nadd\n\n")

if choice == 'print':
    for key,value in stock_prices.items():
         avg=sum(value)/len(value)
         print(f'{key}==> {value}==> avg: {round(avg,2)}')
         avg = 0

elif choice =='add':
     new_stock =  input("Enter name of stock\n\n")
     price = int(input("Enter the price of the stock\n\n"))
     if new_stock in stock_prices:
          #work on adding new this may be wrong
          stock_prices[new_stock]=price
     else:          

                   