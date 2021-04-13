inv_p = float(input('invoice price: '))
ship_cost = float(input('shipping cost: '))

allowance = float(input('allowance: '))

c_dis = float(input('cash discount offered: '))


total_value = inv_p - allowance - (inv_p - allowance)*c_dis

print(total_value)