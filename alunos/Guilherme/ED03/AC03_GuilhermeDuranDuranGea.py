import bpy
import math

# =========================
# Criar um cubo
# =========================
bpy.ops.mesh.primitive_cube_add(location=(-3, -4, 1))
cubo = bpy.context.object
cubo.name = "obj_script_cubo"

# Transformações
cubo.location = (-3, -4, 1)
cubo.scale = (1.2, 1.0, 0.8)

# Rotação com graus → radianos
cubo.rotation_euler = (
    math.radians(45),
    math.radians(30),
    math.radians(60)
)

# =========================
# Criar uma esfera
# =========================
bpy.ops.mesh.primitive_uv_sphere_add(location=(3, -4, 1))
esfera = bpy.context.object
esfera.name = "obj_script_esfera"

# Transformações
esfera.location = (3, -4, 1)
esfera.scale = (0.7, 0.7, 0.7)

# Rotação
esfera.rotation_euler = (
    math.radians(0),
    math.radians(45),
    math.radians(0)
)