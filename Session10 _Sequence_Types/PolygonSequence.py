from functools import lru_cache
from Polygon import Polygon
import string

class PolygonSequence:

    def __init__(self, num_of_edges, circumradius):
        self.num_of_edges = num_of_edges
        self.circumradius = circumradius
        self.poly_seq = dict()

    def __len__(self):
        return self.num_of_edges

    def __repr__(self):
        """
        The method prints Polygon values
        :return:
        """
        return f'Polygon Sequence: Circumradius : {self.circumradius} , ' \
               f'Largest Number Of Edges: {self.num_of_edges}, length : {self.__len__()}'

    def __get_item__(self, edges):
        """
        Generate Polygon for given edges
        @:param: edges as int value
        :return: return Polygon value
        """
        if isinstance(edges, int):
            if edges > 1:
                return PolygonSequence.generate_polygon(edges, self.circumradius)
            else:
                print("It is not a polygon!!!s")
                return 'it is not a polygon'
        else:
            raise IndexError

    @staticmethod
    @lru_cache(50)
    def generate_polygon(num_of_edges, circum_radius) -> float:
        if num_of_edges < 2:
            return 1
        else:
            p = Polygon(num_of_edges, circum_radius)
            return (p.area / p.perimeter)

    @property
    def max_efficieny(self):
        """
        This method computes the maximum_efficiency and returns the string displaying the output
        @params:
            None
        @returns:
            float  - Calculated output
        """
        print("num_of_edges={}".format(self.num_of_edges))
        for i in range(self.num_of_edges):

             #if i > 1:
                #raise ValueError
              edge = i+2

              self.poly_seq[i + 1] = self.__get_item__(edge)
              print(i, edge, self.poly_seq[i + 1], self.__get_item__(edge))

        key = max(self.poly_seq, key=self.poly_seq.get)
        print(f"Max Ratio is {self.poly_seq[key]} at vertex {key}")
        return f"Max Ratio is {self.poly_seq[key]} at vertex {key}"


if __name__ == "__main__":
    if __name__ == "__main__":
        p = PolygonSequence(25, 40)
        print(p.__repr__())
        try:
            res = p.max_efficieny()
            print(res)
        except Exception as e:
            pass
