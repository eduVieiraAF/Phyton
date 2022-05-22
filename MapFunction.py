
#? map() applies a function to each item in iterable (list, tuple, etc)
# map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 27.00),
         ("jacket", 50.00),
         ("socks", 7.00)]

USD_to_euros = lambda data: (data[0], data[1] * 0.92) #Converting to price of products to Euro
                            # funxtion, iterable
store_euro_price = list(map(USD_to_euros, store))

for i in store_euro_price:
    print("The {} cost(s) {:.2f} in Euros.".format(i[0], i[1]))