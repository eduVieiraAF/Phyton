import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([10, 11, 12, 13, 14, 15])

new_arr_add = np.add(arr1, arr2)
print(new_arr_add)

new_arr_sub = np.subtract(arr1, arr2)
print(new_arr_sub)

new_arr_mult = np.multiply(arr1, arr2)
print(new_arr_mult)

new_arr_div = np.divide(arr1, arr2)
print(new_arr_div)

new_arr_pow = np.power(arr1, arr2)
print(new_arr_pow)

# remainder
new_arr_mod = np.mod(arr1, arr2) # remainder() as well
print(new_arr_mod)

# Quotient and Mod - The divmod() function return both the quotient and the mod.
new_arr_divmod = np.divmod(arr1, arr2)
print(new_arr_divmod)
