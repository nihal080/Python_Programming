#specific functions
from graphics.rectangle import area as rect_area, perimeter as rect_perimeter
from graphics.circle import area as circ_area, perimeter as circ_perimeter
print("Rectangle: Area =", rect_area(10, 5))
print("Rectangle: Perimeter =", rect_perimeter(10, 5))
print("Circle: Area =", circ_area(7))
print("Circle: Perimeter =", circ_perimeter(7))
print()


#modules with another name
import graphics.rectangle as rect
import graphics.circle as circ
print("Rectangle: Area =", rect.area(10, 5))
print("Rectangle: Perimeter =", rect.perimeter(10, 5))
print("Circle: Area =", circ.area(7))
print("Circle: Perimeter =", circ.perimeter(7))
print()




#all functions
from graphics import *
print("Rectangle: Area =", rectangle.area(10, 5))
print("Rectangle: Perimeter =", rectangle.perimeter(10, 5))
print("Circle: Area =", circle.area(7))
print("Circle: Perimeter =", circle.perimeter(7))
print()



from graphics.graphics_3D.cuboid import surface_area as sa_cuboid, volume as vol_cuboid
from graphics.graphics_3D.sphere import surface_area as sa_sphere, volume as vol_sphere
print("Cuboid: Surface Area =", sa_cuboid(10, 5, 3))
print("Cuboid: Volume =", vol_cuboid(10, 5, 3))
print("Sphere: Surface Area =", sa_sphere(7))
print("Sphere: Volume =", vol_sphere(7))
