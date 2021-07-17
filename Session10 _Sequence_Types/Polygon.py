import math

class Polygon:
    """
    Ploygon Class holds num of edges and circumradius as variables.
    This has many supporting properties and methods through which one
    can compare two polygon objects are equal, greater than or etc

    """


    def __init__(self, number_of_edges :int, circum_radius :float) -> None:
        self.number_of_edges = number_of_edges
        self.circum_radius = circum_radius

    @property
    def num_edges(self):
        return self.number_of_edges

    @property
    def num_vertices(self):
        return self.number_of_edges

    @property
    def circumradius(self):
        return self._circumradius

    @property
    def interior_angle(self) -> float:
        """
        This method computes interior angle from number of edges
        :param self:
        :return: interior ange as float value
        """
        # Each Angle (of a Regular Polygon) = (n−2) × 180° / n
        return (self.number_of_edges - 2)* 180 / self.number_of_edges

    @property
    def edge_length(self) -> float:
        return 2*self.circum_radius*math.sin(math.pi/self.number_of_edges)

    @property
    def apothem(self) -> float:
        """
        Method computes apothem from circum radius and number of edges
        :param self:
        :return: value as float
        Reference: https://www.mathopenref.com/apothem.html
        """
        return self.circum_radius*math.cos(math.pi/self.number_of_edges)

    @property
    def area(self) -> float:
        return 0.5*self.apothem*self.edge_length * self.number_of_edges

    @property
    def perimeter(self) -> float:
        return self.number_of_edges * self.edge_length


    def __repr__(self):
        """
        Method returns number of edges and circumradius of the Polygon
        :param self:
        :return: value as string
        """
        return f'Polygen has {self.number_of_edges} edges and {self.circum_radius} as circum radius'


    def __eq__(self, other) -> bool:
        """
        This method checks whether two Polygon objects are equal or not using number of edges and
        cirum radius of the polygen.
        @params:
            other : Polygen object
        @returns: return True if both classes were equals otherwise False.
        """
        if not isinstance(other, Polygon):
            raise ValueError('This function compare only Polygon Types!')
        return ((self.number_of_edges == other.number_of_edges) and (self.circum_radius == other.circum_radius))

    def __gt__(self, other) -> bool:
        """
        Compares two Plolygen objects and return True, if given object is greater than currnet object.
        :param self: another Polygen typeas argument
        :return: return True, if given object is greater than current object.
        """
        if not isinstance(other, Polygon):
            raise ValueError('This method compares only two Polygon Objects!')
        return (self.number_of_edges > other.number_of_edges)



if __name__ == "__main__":
    p = Polygon(10, 10)  # no of edges , circumradius
    print("Polygon1:", p.__repr__())

    print("Num of edges: {}".format(p.number_of_edges))

    print("circum_radius : {}".format(p.circum_radius))
    print("area: {}".format(p.area))
    print("edge_length:{}".format(p.edge_length))

    p2 = Polygon(22, 12)
    print("Polygon2:", p2.__repr__())
    print("Ploygon1 > polygon2 => ", p.__gt__(p2))
    print("Ploygon1 == polygon2 => ", p2.__eq__(p))


