cubes = [12,13,14]
colors = ["red", "green", "blue"]
p1sum =0
p2sum = 0
with open('cubedoc.txt') as topo_file:
    for line in topo_file:
        valid = True
        maxes = [0,0,0]
        prod = 1
        gameID = line.split(":")[0].split(" ")[1]
        for draw in line.split(":")[1].split(";"):
            for colornum in draw.split(","):
                colornum = colornum.strip()
                color= colornum.split(" ")[1]
                idx = colors.index(color)
                num = int(colornum.split(" ")[0])
                if num > maxes[idx]:
                    maxes[idx] = num
                if num > cubes[idx]:
                    valid = False
        for max in maxes : prod *= max
        p2sum += prod
        if valid:
            p1sum += int(gameID)
    print("p1 solution: " + str(p1sum))
    print("p2 solution: " + str(p2sum))




