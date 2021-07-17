# Assignment10

 

Name: Thamizhannal 

Email: annalwins@gmail.com



1. A regular strictly convex polygon is a polygon that has the following characteristics:

   1. all interior angles are less than 180
   2. all sides have equal length
      ![ywVyfMa1Zt.png](https://canvas.instructure.com/courses/2734597/files/143701655/preview) 

2. For a regular strictly convex polygon with:

   - **n** edges (=n vertices)
   - **R** circumradius
   - interiorAngle=(n−2)⋅180ninteriorAngle=(n−2)⋅180n
   - edgeLength,s=2⋅R⋅sin(πn)edgeLength,s=2⋅R⋅sin⁡(πn)
   - apothem,a=R⋅cos(πn)apothem,a=R⋅cos⁡(πn)
   - area=12⋅n⋅s⋅aarea=12⋅n⋅s⋅a
   - perimeter=n⋅sperimeter=n⋅s

3. Objective 1 [pts:400]:

   1. Create a Polygon Class:

      1. where initializer takes in:
         1. number of edges/vertices
         2. circumradius
      2. that can provide these properties:
         1. \# edges
         2. \# vertices
         3. interior angle
         4. edge length
         5. apothem
         6. area
         7. perimeter
      3. that has these functionalities:
         1. a proper __repr__ function
         2. implements equality (==) based on # vertices and circumradius (__eq__)
         3. implements > based on number of vertices only (__gt__)

   2. Objective 2 [pts:600]:

      1. Implement a Custom Polygon sequence type:

         1. where initializer takes in:

            1. number of vertices for largest polygon in the sequence
            2. common circumradius for all polygons

         2. that can provide these properties:

            1. max efficiency polygon: returns the Polygon with the highest **area: perimeter** ratio

         3. that has these functionalities:

            1. functions as a sequence type (__getitem__)

            2. supports the len() function (__len__)

            3. has a proper representation (__repr__)

               



# Polygon: 

Polygon Class holds number of edges and circumradius as variables. This has many supporting properties and methods through which one  can compare two polygon objects are equal, greater than or etc. This class further extended to add additional methods, if anything in future.



**Properties:**

number of edges

num_vertices
circumradius



**interior_angle():**

This method computes interior angle from number of edges


```
self.number_of_edges - 2)* 180 / self.number_of_edges
```



**edge_length:**

​	2*self.circum_radius*math.sin(math.pi/self.number_of_edges)

**apothem():**
Method computes apothem from circumradius and number of edges
self.circum_radius*math.cos(math.pi/self.number_of_edges)

Reference: https://www.mathopenref.com/apothem.html



**Interior Angles:**

Interior angles = = (**n**−2) × 180**°** / **n**

Here n is number of edges

https://www.mathsisfun.com/geometry/interior-angles-polygons.html



**Area:**

0.5*self.apothem*self.edge_length * self.number_of_edges



**perimeter:**

self.number_of_edges * self.edge_length

__eq__():

This method checks whether two Polygon objects are equal or not using number of edges and circumradius of the polygon.
     

**gt()**

​	Compares two Plolygon objects and return True, if given object is greater than current object.

```
self.number_of_edges * self.edge_length
```



**Calling Polygon class:**

```python
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



output:
Polygon1: Polygen has 10 edges and 10 as circum radius
Num of edges: 10
circum_radius : 10
area: 293.8926261462365
edge_length:6.180339887498948
Polygon2: Polygen has 22 edges and 12 as circum radius
Ploygon1 > polygon2 =>  False
Ploygon1 == polygon2 =>  False
```



# Polygon Sequence

Class that stores sequences of Polygon objects and have couple of helper methods. max_efficiency is the method decided which polygon in this sequence has max efficiency using area / perimeter ratio.



**max_efficiency:** 

```
This method computes the maximum_efficiency and returns the string displaying the output
```

```




```

**generate polygon:**

method generates Polygon for given edges and circumradius.



**get_item()**

method to get an Polygon object for given edge and circumradius from Polygon class.



```
Calling PolygonSequence:
if __name__ == "__main__":
    p = PolygonSequence(25, 40)
    print(p.__repr__())
    try:
        res = p.max_efficieny()
        print(res)
    except Exception as e:
        pass
        
        
        
Output:
Polygon Sequence: Circumradius : 40 , Largest Number Of Edges: 25, length : 25
num_of_edges=25
0 2 1.2246467991473533e-15 1.2246467991473533e-15
1 3 10.000000000000002 10.000000000000002
2 4 14.142135623730951 14.142135623730951
3 5 16.18033988749895 16.18033988749895
4 6 17.320508075688778 17.320508075688778
5 7 18.019377358048384 18.019377358048384
6 8 18.477590650225736 18.477590650225736
7 9 18.793852415718174 18.793852415718174
8 10 19.02113032590307 19.02113032590307
9 11 19.189859472289942 19.189859472289942
10 12 19.318516525781362 19.318516525781362
11 13 19.41883634852104 19.41883634852104
12 14 19.498558243636474 19.498558243636474
13 15 19.562952014676114 19.562952014676114
14 16 19.61570560806461 19.61570560806461
15 17 19.65946199367804 19.65946199367804
16 18 19.696155060244163 19.696155060244163
17 19 19.727226068054446 19.727226068054446
18 20 19.753766811902757 19.753766811902757
19 21 19.776616524502572 19.776616524502572
20 22 19.796428837618652 19.796428837618652
21 23 19.813718920726615 19.813718920726615
22 24 19.82889722747621 19.82889722747621
23 25 19.842294026289558 19.842294026289558
24 26 19.85417748196108 19.85417748196108
Max Ratio is 19.85417748196108 at vertex 25
```







