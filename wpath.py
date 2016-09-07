


class Wpath():
    def __init__(self, fname):
        self._points = []
        with open(fname, 'r') as f:
            f.readline() # version
            f.readline() # welltype
            f.readline() # wellname
            logs = int(f.readline().strip())
            for i in range(logs):
                f.readline()
            l = 'x'
            while l:
                l = f.readline()
                d = tuple(map(float, l.split()))
                if len(d)>0:
                    self._points.append(d)
        self._points = tuple(self._points)

    def x(self,idx):
        return self._points[idx][0]
    def y(self,idx):
        return self._points[idx][1]
    def z(self,idx):
        return self._points[idx][2]
    def xyz(self,idx):
        return self.x(idx), self.y(idx), self.z(idx)

    def __getitem__(self, idx):
        return self._points[idx]

    def __str__(self):
        return self._points.__str__()

    def __len__(self):
        return len(self._points)

    def __iter__(self):
        for pt in self._points:
            yield pt
