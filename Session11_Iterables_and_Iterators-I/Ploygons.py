class Polygons:
    def __init__(self, m, R):
        self._index = 0 # To access each element in Polygon sequence
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m + 1)]

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        print("polygon called!")
        return f'Polygons(m={self._m}, R={self._R})'

    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons,
                                 key=lambda p: p.area / p.perimeter,
                                 reverse=True)
        print(sorted_polygons[0])
        return sorted_polygons[0]

    def __iter__(self):
        print("Calling Polygon instance __iter__")
        # PolygonIterator
        return self

    def __next__(self):
        # check index is greater than edges(m)
        if self._index >= self._m:
            raise StopIteration
        else:
            self._index += 1
            return self._polygons[self.__index]

