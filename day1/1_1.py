def calc_fuel(mass) :
    return int(mass/3)-2

with open("1.in", "r+") as infile :
    fuel_sum = 0
    for line in infile :
        fuel_sum += calc_fuel(float(line.strip()))
infile.close()
print(fuel_sum)
