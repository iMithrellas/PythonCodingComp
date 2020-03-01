hodnoty = {"#":0,"~":800,"*":200,"+":150,"X":120,"_":100,"H":70,"T":50}


with open('../Data/1_victoria_lake.txt', 'r') as f:
    lines = f.readlines()

lines_2 = []
for i in lines:
    i = i.split()
    lines_2.append(i)

zakaznici = lines_2[1:int(lines_2[0][2])+1]
mapa = []

for i in lines_2[int(lines_2[0][2])+1:]:
    mapa.append([x for x in i[0]])

for i in mapa:
    print(i)
