# first part
def get_fuel(mass):
    return int(int(mass) / 3) - 2

# second part
def get_total_fuel(mass):
    fuel = get_fuel(mass)
    if fuel <= 0:
        return 0
    else:
        return fuel + get_total_fuel(fuel) # get fuel from fuel


with open('input1.txt') as modules:
    total_sum1 = 0
    total_sum2 = 0
    for mass in modules: # for each module
        total_sum1 = total_sum1 + get_fuel(mass) # first part: add fuel from next module
        total_sum2 = total_sum2 + get_total_fuel(mass) # second part: add fuel from next module


print(total_sum1)
print(total_sum2)