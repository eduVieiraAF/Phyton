
#? map() applies a function to each item in iterable (list, tuple, etc)
# map(function, iterable)

store = [("shirt", 15.00),
         ("pants", 27.00),
         ("jacket", 50.00),
         ("socks", 5.00)]

USD_to_Real = lambda data: (data[0], (data[1] * 5) * 1.25) #Converting to price of products to Euro
                            # funxtion, iterable
store_real_price = list(map(USD_to_Real, store))

for i in store_real_price:
    print("The {} cost(s) {:.2f} in Reais.".format(i[0], i[1]))