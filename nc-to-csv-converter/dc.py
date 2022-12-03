import xarray as xr
from itertools import product
import csv
from copy import copy

ds = xr.open_dataset('data.nc')


all_vars = [i for i in ds.variables]
main_vars = copy(all_vars)
val_vars = [i for i in ds]
[main_vars.remove(i) for i in val_vars]

main_var_vals = [ds[i] for i in main_vars]
val_var_vals = [ds[i] for i in val_vars]

f = open('data.csv','w')

writer = csv.writer(f)

writer.writerow(all_vars)
main_var_indexes = [0 for _ in main_vars]
main_var_lengths = [len(i)-1 for i in main_var_vals]
main_var_lengths.reverse()


def get_values(val_var):
    global main_var_indexes
    x = copy(val_var)
    for i in main_var_indexes:
        x = x[i]
    return x.valuesp

def update_indexes():
    global main_var_indexes,main_var_lengths
    for idx,i in enumerate(main_var_indexes):
        main_var_indexes[idx] = i+1
        if main_var_indexes[idx] > main_var_lengths[idx]:
            main_var_indexes[idx] = 0
        else: break

for i in product(*main_var_vals):
    row = list()
    row.extend([j.values for j in i])
    values = [get_values(i) for i in val_var_vals]
    row.extend(values)
    print(row)
    writer.writerow(row)
    update_indexes()

f.close()