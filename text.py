arr = [1, 11, 13, 14, 99, 8, 9, 66, 90, 100, 121, 134]
# [1, 8, 9, 11, 13, 14, 66, 90, 99, 100, 121, 134]
N = 24
arr_sort = []
middle = 0
arr_divide = []

if len(arr) % 2 != 0:
    arr.append(0)
arr_sort = sorted(arr)
middle = round(len(arr_sort) / 2)
if arr_sort[middle] >= N:
    arr_divide = arr_sort[:middle]

import os
os.remove('prices_from_kaspi_kz.xlsx')