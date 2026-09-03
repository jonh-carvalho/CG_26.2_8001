import bpy
import mathutils
import math

# Altere com os seus dados de aniversário (Dia = D, Mês = M)
DIA = 15  # Dia (D)
MES = 10  # Mês (M)

def limpar_cena():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def criar_piramide_mundo():
    # Vértices Locais da Pirâmide (Y-Up conforme slides teóricos)
    vertices_locais = [
        (0.0, 1.0, 0.0),          # V0 (Ápice)
        (-0.5, 0.0, 0.5),         # V1
        (0.5, 0.0, 0.5),          # V2
        (0.5, 0.0, -0.5),         # V3
        (-0.5, 0.0, -0.5)         # V4
    ]
    faces = [
        (0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1),
        (1, 4, 3), (1, 3, 2)
    ]
    
    mesh = bpy.data.meshes.new("Piramide_Mesh")
    obj = bpy.data.objects.new("Piramide_Mundo", mesh)
    bpy.context.scene.collection.objects.link(obj)
    mesh.from_pydata(vertices_locais, [], faces)
    mesh.update()
    
    # Matriz Model do laboratório anterior (T * R * S)
    s_x, s_y, s_z = MES, DIA, MES
    t_x, t_y, t_z = 0.5 * MES, 0.0, 0.5 * MES
    angulo_rot = math.radians(45)
    
    S = mathutils.Matrix.Diagonal((s_x, s_y, s_z, 1.0))
    R = mathutils.Matrix.Rotation(angulo_rot, 4, 'Y')
    T = mathutils.Matrix.Translation((t_x, t_y, t_z))
    
    Model = T @ R @ S
    obj.matrix_world = Model
    
    # Calcular coordenadas globais (Espaço de Mundo)
    vertices_mundo = []
    for v in vertices_locais:
        v_4d = mathutils.Vector((v[0], v[1], v[2], 1.0))
        v_world = Model @ v_4d
        vertices_mundo.append(v_world.to_3d())
        
    return obj, vertices_mundo

def configurar_e_calcular_view(vertices_mundo):
    # 1. Definir Posição da Câmera (P0) e Alvo (Target)
    # Posicionamos a câmera um pouco acima e afastada para visualizar a pirâmide
    P0 = mathutils.Vector((float(MES * 1.5), float(DIA * 1.2), float(MES * 2.0)))
    Target = mathutils.Vector((0.5 * MES, 0.5 * DIA, 0.5 * MES))  # Foco no centro do objeto transformado
    
    print("\n" + "="*80)
    print("             CG PRÁTICA: ESPAÇO DE VISÃO (MATRIZ VIEW) NO BLENDER")
    print("="*80)
    print(f"▶ Posição da Câmera (P0) = {P0}")
    print(f"▶ Ponto de Foco (Target)  = {Target}")
    
    # 2. Calcular o vetor de direção Normal (N) da câmera
    N = P0 - Target
    n = N.normalized()  # Eixo Z da câmera (zview)
    
    # 3. Definir o vetor View-Up padrão (V)
    V = mathutils.Vector((0.0, 1.0, 0.0))
    
    # 4. Calcular o vetor U (Eixo X da câmera - xview)
    # u = (V x n) / |V x n|
    cross_V_n = V.cross(n)
    u = cross_V_n.normalized()
    
    # 5. Calcular o vetor V_view (Eixo Y da câmera - yview)
    # v = n x u
    v = n.cross(u)
    
    print(f"\n▶ Vetores Diretores do Sistema de Visão (Câmera):")
    print(f"   u (x_view) = {u}")
    print(f"   v (y_view) = {v}")
    print(f"   n (z_view) = {n}")
    
    # 6. Construir as Matrizes de Rotação (R) e Translação (T) da Câmera
    R = mathutils.Matrix([
        [u.x, u.y, u.z, 0.0],
        [v.x, v.y, v.z, 0.0],
        [n.x, n.y, n.z, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])
    
    T = mathutils.Matrix.Translation(-P0)
    
    # Matriz View Composta (View = R * T)
    View = R @ T
    
    print("\n▶ Matriz View Composta (M_view = R * T):")
    for r in View:
        print(f"     [ {r[0]:6.3f}  {r[1]:6.3f}  {r[2]:6.3f}  {r[3]:6.3f} ]")
        
    # 7. Transformar os Vértices do Espaço de Mundo para o Espaço de Visão
    print("\n▶ [COMPARAÇÃO] Vértices nos Espaços Mundo e Visão (P_visao = M_view * P_mundo):")
    for i, v_world in enumerate(vertices_mundo):
        v_world_4d = mathutils.Vector((v_world.x, v_world.y, v_world.z, 1.0))
        v_view = View @ v_world_4d
        print(f"   V{i} -> Mundo: [{v_world.x:6.2f}, {v_world.y:6.2f}, {v_world.z:6.2f}] | Visão: [{v_view.x:6.2f}, {v_view.y:6.2f}, {v_view.z:6.2f}]")
        
    # 8. Atualizar a Câmera Ativa do Blender para refletir essa Matriz matematicamente!
    # No Blender, camera.matrix_world é a transformação que leva da câmera para o mundo.
    # Portanto, camera.matrix_world = View.inverted()
    
    # Garante que temos uma câmera na cena
    if "Camera" in bpy.data.objects:
        cam_obj = bpy.data.objects["Camera"]
    else:
        bpy.ops.object.camera_add()
        cam_obj = bpy.context.object
        cam_obj.name = "Camera"
        
    # Aplica a inversa da nossa matriz View
    cam_obj.matrix_world = View.inverted()
    
    # Configura a cena para usar essa câmera
    bpy.context.scene.camera = cam_obj
    print("\n▶ Câmera do Blender posicionada e rotacionada usando a inversa da Matriz View!")
    print("="*80 + "\n")

if __name__ == "__main__":
    limpar_cena()
    pyr_obj, verts_mundo = criar_piramide_mundo()
    configurar_e_calcular_view(verts_mundo)
