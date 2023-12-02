# solution part 1
sumnum = 0
with open('caldoc.txt') as topo_file:
    for line in topo_file:
        res = [int(i) for i in line if i.isnumeric()]
        dig = int(str(res[0]) + str(res[len(res)-1]))
        sumnum += dig
    print("Part 1 solution = " + str(sumnum))


#solution part 2 didn't realize until late that zoneight234 has one and eight sharing a letter

sumnum = 0
numstrs = ["one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
nums = ["o1e","t2o","t3e","f4r","f5e","s6x","s7n","e8t","n9e"]

with open('caldoc.txt') as topo_file:
    for line in topo_file:
        for j,numname in enumerate(numstrs):
            line = line.replace(numname,str(nums[j]))
        res = [int(i) for i in line if i.isnumeric()]
        dig = int(str(res[0]) + str(res[len(res)-1]))
        sumnum += dig
    print("Part 2 solution = " + str(sumnum))