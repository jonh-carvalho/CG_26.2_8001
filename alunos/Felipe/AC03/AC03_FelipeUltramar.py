import bpy
import math

# OBJETO 3D - ESFERA
bpy.ops.mesh.primitive_uv_sphere_add(location=(-6, 2, 1))
esfera = bpy.context.active_object
esfera.name = "obj3d_esfera_script"

# Transformações 3D
esfera.location = (1.5, 0, 1.5)
esfera.rotation_euler = (math.radians(15),math.radians(25),math.radians(10))
esfera.scale = (1.2, 1.2, 1.2)

# OBJETO 2D - CÍRCULO

bpy.ops.mesh.primitive_circle_add(location=(-6, -1, 0))
circulo = bpy.context.active_object
circulo.name = "obj2d_circulo_script"

# Transformações 2D 
circulo.location = (1.5, -1.5, 0)
circulo.rotation_euler = (0, 0, math.radians(45))
circulo.scale = (1.8, 1.2, 1.0)
