def map_coord(coord):
    mapa = {'A': 1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
    return [mapa[coord[0]],int(coord[1])]

def inv_coord(coord):
    mapa = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}
    return mapa[coord[0]]+str(coord[1])

def distancia(p1, p2):
    x1 = map_coord(p1.pos)
    x2 = map_coord(p2.pos) 
    return abs(x1[1]-x2[1])

def diagonais(pos,dist,capt):
    if capt == 1:
        pos_coord = map_coord(pos)
        diagonais = []
        x = pos_coord[0]
        y = pos_coord[1]
        for i in range(1,dist+1):
            all_diagonais = [[x-i,y-i], [x-i, y+i]]
            for casa in all_diagonais:
                if 1<=casa[0]<=8 and 1<=casa[1]<=8:
                    casa = inv_coord(casa)
                    diagonais.append(casa)
        return diagonais
    else:
        pos_coord = map_coord(pos)
        diagonais = []
        x = pos_coord[0]
        y = pos_coord[1]
        for i in range(1,dist+1):
            all_diagonais = [[x+i,y-i],[x+i,y+i],[x-i,y-i], [x-i, y+i]]
            for casa in all_diagonais:
                if 1<=casa[0]<=8 and 1<=casa[1]<=8:
                    casa = inv_coord(casa)
                    diagonais.append(casa)
        return diagonais