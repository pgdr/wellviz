#!/usr/bin/env ipython
from ert.ecl import EclGrid, EclFile
from wpath import Wpath
from wellwall import constructWall, wallToMatrix

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def drawWall(wall, wp=None):
    X = wallToMatrix(wall)
     
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(X, cmap=cm.jet, interpolation='nearest')
     
    numrows, numcols = X.shape
    def format_coord(x, y):
        col = int(x+0.5)
        row = int(y+0.5)
        if 0 <= col < numcols and 0 <= row < numrows:
            z = X[row,col]
            return 'x=%1.4f, y=%1.4f, z=%1.4f'%(x, y, z)

    ax.format_coord = format_coord
    plt.show()

def main():
    grid = EclGrid('/home/pgdr/statoil/norne/NORNE_ATW2013.EGRID')
    init = EclFile('/home/pgdr/statoil/norne/NORNE_ATW2013.INIT')
    rest = EclFile('/home/pgdr/statoil/norne/NORNE_ATW2013.UNRST')
    wp   = Wpath('/home/pgdr/statoil/norne/norne-test-2-mid.w')
    swat, sgas = rest._iget_named_kw('SWAT', 0), rest._iget_named_kw('SGAS', 0)
    permx = init._iget_named_kw('PERMX', 0)
 
    wall = constructWall(grid, wp, swat, sgas, permx)
    drawWall(wall)

if __name__ == '__main__':
    main()
