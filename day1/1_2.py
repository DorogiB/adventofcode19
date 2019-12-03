def calc_fuel(mass) :
    result = 0
    fuel = int(mass/3)-2
    if fuel >= 0 :
        result += fuel
        result += calc_fuel(fuel)
    return result


with open("1.in", "r+") as infile :
    fuel_sum = 0
    for line in infile :
        fuel_sum += calc_fuel(float(line.strip()))
infile.close()
print(fuel_sum)
