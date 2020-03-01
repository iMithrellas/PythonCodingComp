import random
map_01 =[]
for i in range(30):
    map_01.append(random.sample(range(1, 50), 40))




def find_path(map, start_y, start_x, end_y, end_x):
    path = [[start_y, start_x],]
    akt_y = start_y
    akt_x = start_x
    counter = 0
    counter_2 = 0
    while True:
        #print([akt_x, akt_y])
        while True:

            if counter > 9:
                counter = 0
                akt_y = start_y
                akt_x = start_x
                path = [[start_y, start_x],]
                continue

            nah = random.choice([-1,1])
            if random.choice([0,1]) == 0 and len(map[0]) > (akt_x + nah) >= 0:
                if [akt_y,(akt_x + nah)] not in path:
                    #print(akt_x, nah, "x")
                    akt_x += nah
                    #print(akt_x)
                    break
                else:
                    counter += 1
                    continue

            elif len(map) > (akt_y + nah) >= 0:
                if [(akt_y + nah),akt_x] not in path:
                    #print(akt_y, nah, "y")
                    akt_y += nah
                    #print(akt_y)
                    break
                else:
                    counter += 1
                    continue


        coord = [akt_y, akt_x]
        path.append(coord)


        if map[akt_y][akt_x] == map[end_y][end_x]:
            break


    return(path)



kap = len(map_01)*len(map_01[0])
paths = []
counter = 0
while counter < 5:
    path = find_path(map_01, 15, 6, 3, 12)
    if path not in paths:
        paths.append(path)
        counter = 0
    else:
        counter += 1

for i in paths:
    pass
    #print(i)


print(len(paths))
