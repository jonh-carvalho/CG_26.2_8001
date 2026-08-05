import bpy
import math

# Limpa a cena inicial (opcional, mas bom para testar o script do zero)
bpy.ops.object.select_all(action='DESELECT')

# 1. Cria o Cubo (Objeto Pai - 3D)
bpy.ops.mesh.primitive_cube_add(location=(8, 0, 1))
cubo = bpy.context.active_object
cubo.name = "obj3d_cubo"
# Transformação 3D: Rotação em eixos diferentes e Escala
cubo.rotation_euler = (math.radians(45), math.radians(0), math.radians(30))
cubo.scale = (1.2, 1.2, 1.2)

# 2. Cria o Quadrado (Objeto Filho - 2D no plano XY)
bpy.ops.mesh.primitive_plane_add(location=(-5, 0, 2)) # Posição relativa ao mundo antes de parentar
plano = bpy.context.active_object
plano.name = "obj2d_quadrado"
# Transformação 2D: Rotação apenas no eixo Z e Escala
plano.rotation_euler = (0, 0, math.radians(45))
plano.scale = (0.5, 0.5, 1.0)

# BÔNUS: Criando a hierarquia (Parent/Child)
# O plano será "filho" do cubo. Se o cubo mover, o plano vai junto.
plano.parent = cubo
plano.matrix_parent_inverse = cubo.matrix_world.inverted()