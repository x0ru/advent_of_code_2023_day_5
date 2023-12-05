import csv


soils = []
n = 0
hashmap = {}


with open('file.csv') as file:
    file = csv.reader(file)
    for line in file:
        if not soils:
            soils.append(line[0].split(' ')[1:])
        if not line:
            n += 1
        else:
            if n not in hashmap.keys():
                hashmap[n] = [line]
            else:
                hashmap[n] += [line[0].split(' ')]


result = 0
chosen_soil = 0
trim_value = 10000

for m in range(0, len(soils[0]), 2):
    print(range(int(soils[0][m]), (int(soils[0][m]) + int(soils[0][m + 1]))))
    for soil in range(int(int(soils[0][m])/trim_value), int((int(soils[0][m])/trim_value) +
                                                            int(int(soils[0][m + 1])/trim_value))):
        var = soil
        print(var)
        for j in range(1, len(hashmap)):
            for k in range(1, len(hashmap[j])):
                if var in range(int(int(hashmap[j][k][1])/trim_value), int(int(hashmap[j][k][1])/trim_value) +
                                int(int(hashmap[j][k][2])/trim_value)):
                    diff = int(int(hashmap[j][k][1])/trim_value) - int(int(hashmap[j][k][0])/trim_value)
                    var -= diff
                    break
        if result == 0:
            result = var
        if var < result:
            result = var
            chosen_soil = soil

    print(result, "<<<This is the answer", chosen_soil)

result = 0

for soil in range((chosen_soil*trim_value)-trim_value, (chosen_soil*trim_value)+trim_value):
    var = soil
    print(soil)
    for j in range(1, len(hashmap)):
        for k in range(1, len(hashmap[j])):
            if var in range(int(hashmap[j][k][1]), int(hashmap[j][k][1]) + int(hashmap[j][k][2])):
                diff = int(hashmap[j][k][1]) - int(hashmap[j][k][0])
                var -= diff
                break
        if result == 0:
            result = var
        if var < result:
            result = var

print(result, "<<<This the answer")
