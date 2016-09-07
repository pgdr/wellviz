from cell import Cell
def constructColumn(x,y,z, grid, swat=None, sgas=None, permx=None):
    col = []
    for k in range(grid.getNZ()):
        i,j = grid.findCellXY(x, y, k)
        g_idx = grid.get_global_index(ijk = (i,j,k))
        a_idx = grid.get_active_index(global_index=g_idx)
        swat_val = float('nan')
        sgas_val = float('nan')
        soil_val = float('nan')
        permx_val = float('nan')
        if swat:
            swat_val = swat[a_idx]
        if sgas:
            sgas_val = sgas[a_idx]
        if permx:
            permx_val = permx[a_idx]

        c = Cell(x=x,y=y,z=z,
                 a_idx=a_idx, g_idx=g_idx,
                 i=i,j=j,k=k,
                 swat=swat_val,
                 sgas=sgas_val,
                 permx=permx_val)
        col.append(c)
    return col

def constructWall(grid, wp, swat=None,sgas=None,permx=None):
    wall = []
    for idx in range(len( wp )):
        col = constructColumn(wp.x(idx),wp.y(idx),wp.z(idx), grid, swat, sgas, permx)
        wall.append(col)

    print('Wall size: %d' % len(wall))
    return wall

def wallToMatrix(wall):
    import numpy as np
    m = len(wall)
    if m == 0:
        return np.empty()
    n = len(wall[0])
    X = np.empty(shape=[n, m])
    for j in range(len(wall)):
        for i in range(len(wall[j])):
            cell = wall[j][i]
            X[i][j] = cell.soil()
    return X
