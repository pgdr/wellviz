
class Cell():
    def __init__(self, x = float('nan'), y = float('nan'), z = float('nan'),
                 a_idx = - 1, g_idx = float('nan'), i = -1, j = -1, k = -1, 
                 swat = float('nan'), sgas = float('nan'), permx = float('nan')):
        self._x = x
        self._y = y
        self._z = z

        self._a_idx = a_idx
        self._g_idx = g_idx

        self._i = i
        self._j = j
        self._k = k

        self._swat = swat
        self._sgas = sgas
        self._permx = permx
        if self._a_idx < 0:
            self._swat  = float('nan')
            self._sgas  = float('nan')
            self._permx = float('nan')
            

    def x(self):
        return self._x
    def y(self):
        return self._y
    def z(self):
        return self._z
    def xyz(self):
        return self._x, self._y, self._z

    def activeIndex(self):
        return self._a_idx
    def globalIndex(self):
        return self._g_idx

    def i(self):
        return self._i
    def j(self):
        return self._j
    def k(self):
        return self._k
    def ijk(self):
        return self._i, self._j, self._k

    def swat(self):
        return self._swat
    def sgas(self):
        return self._sgas
    def soil(self):
        return 1 - self._swat - self._sgas

    def permx(self):
        return self._permx

    def __str__(self):
        return "(%.2f,%.2f,%.2f) @ (%d,%d,%d):%d:%d, soil=%.2f, permx=%.2f" % (self.x(), self.y(), self.z(), self.i(), self.j(), self.k(),
                   self.activeIndex(), self.globalIndex(), self.soil(),
                   self.permx())
