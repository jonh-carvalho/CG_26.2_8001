import bpy
import math

# Cria um cilindro e aplica transformacoes 3D
bpy.ops.mesh.primitive_cylinder_add(location=(4, 0, 1))
cilindro = bpy.context.active_object
cilindro.name = "obj3d_cilindro_script"
cilindro.rotation_euler = (math.radians(0), math.radians(45), math.radians(20))
cilindro.scale = (1.0, 1.0, 1.8)

# Cria um triangulo 2D no plano XY
bpy.ops.mesh.primitive_circle_add(vertices=3, radius=1, fill_type='NGON', location=(-4, -1, 0))
triangulo = bpy.context.active_object
triangulo.name = "obj2d_triangulo_script"
triangulo.rotation_euler = (0, 0, math.radians(45))
triangulo.scale = (1.2, 1.2, 1.0)