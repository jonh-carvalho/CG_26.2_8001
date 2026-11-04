import bpy
import mathutils
import math

# ==============================================================================
# CONFIGURAÇÃO DE PARÂMETROS (EXERCÍCIO III)
# ==============================================================================
DIA = 15  # Dia de nascimento (D)
MES = 10  # Mês de nascimento (M)

# Parâmetros de Projeção sugeridos pelas notas de aula [20]
Z_NEAR = DIA / 100.0  # znear = D / 100
Z_FAR = 10.0 * DIA    # zfar = 10 * D

# Parâmetros de câmera definidos pelo usuário (conforme escolha livre permitida)
FOV_GRAUS = 60.0      # Campo de visão de 60 graus
ASPECT_RATIO = 16 / 9 # Proporção widescreen comum

def limpar_cena_atual():
    """Remove todos os objetos da cena do Blender para reiniciar o cenário."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def criar_piramide_local():
    """Gera os vértices locais da pirâmide (Y-Up) conforme notas de aula."""
    vertices_locais = [
        (0.0, 1.0, 0.0),          # V0 (Ápice)
        (-0.5, 0.0, 0.5),         # V1 (Base Frontal-Esquerda)
        (0.5, 0.0, 0.5),          # V2 (Base Frontal-Direita)
        (0.5, 0.0, -0.5),         # V3 (Base Traseira-Direita)
        (-0.5, 0.0, -0.5)         # V4 (Base Traseira-Esquerda)
    ]
    # Faces triangulares para representação canônica
    faces_locais = [
        (0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1), # Laterais
        (1, 4, 3), (1, 3, 2)                         # Base dividida em 2 triângulos
    ]
    mesh = bpy.data.meshes.new("Piramide_Mesh")
    obj = bpy.data.objects.new("Piramide_Objeto", mesh)
    bpy.context.scene.collection.objects.link(obj)
    mesh.from_pydata(vertices_locais, [], faces_locais)
    mesh.update()
    return obj, vertices_locais

def construir_matrizes_e_projetar(obj, vertices_locais):
    """
    Computa todo o Pipeline de Visualização Gráfica 3D:
    Local -> World -> View -> Clip -> NDC
    E configura a câmera na viewport do Blender.
    """
    print("\n" + "="*95)
    print("             CG PRÁTICA: PIPELINE COMPLETO DE PROJEÇÃO PERSPECTIVA (BLENDER 4.5)")
    print("="*95)
    
    # --- 1. MATRIZ MODEL (Exercício I) ---
    s_x, s_y, s_z = MES, DIA, MES
    t_x, t_y, t_z = 0.5 * MES, 0.0, 0.5 * MES
    angulo_rot = math.radians(45)
    
    S = mathutils.Matrix.Diagonal((s_x, s_y, s_z, 1.0))
    R = mathutils.Matrix.Rotation(angulo_rot, 4, 'Y')
    T = mathutils.Matrix.Translation((t_x, t_y, t_z))
    Model = T @ R @ S
    
    # Aplica a transformação de mundo ao objeto físico
    obj.matrix_world = Model

    # --- 2. MATRIZ VIEW (Exercício II) ---
    # Parâmetros do Exercício II: P0 = (0, 0, M), Target = (0,0,0), Up = (0, 1, 0)
    P0 = mathutils.Vector((0.0, 0.0, float(MES)))
    Target = mathutils.Vector((0.0, 0.0, 0.0))
    V_up = mathutils.Vector((0.0, 1.0, 0.0))
    
    # Lógica de cálculo dos eixos locais da câmera (u, v, n) [2, 3, 4]
    n = (P0 - Target).normalized()
    u = V_up.cross(n).normalized()
    v = n.cross(u)
    
    # Montagem da Matriz View [4, 5]
    R_view = mathutils.Matrix((
        (u.x, u.y, u.z, 0.0),
        (v.x, v.y, v.z, 0.0),
        (n.x, n.y, n.z, 0.0),
        (0.0, 0.0, 0.0, 1.0)
    ))
    T_view = mathutils.Matrix.Translation(-P0)
    View = R_view @ T_view

    # --- 3. MATRIZ PROJECTION PERSPECTIVA NORMALIZADA (Exercício III) ---
    # Fatores trigonométricos e matemáticos [11, 12, 16]
    cot_fov_2 = 1.0 / math.tan(math.radians(FOV_GRAUS / 2.0))
    
    m00 = cot_fov_2 / ASPECT_RATIO
    m11 = cot_fov_2
    m22 = -(Z_FAR + Z_NEAR) / (Z_FAR - Z_NEAR)
    m23 = -(2.0 * Z_FAR * Z_NEAR) / (Z_FAR - Z_NEAR)
    
    # Matriz conforme slides teóricos [16]
    Projection = mathutils.Matrix((
        (m00, 0.0, 0.0, 0.0),
        (0.0, m11, 0.0, 0.0),
        (0.0, 0.0, m22, m23),
        (0.0, 0.0, -1.0, 0.0)
    ))

    # --- EXIBIÇÃO DAS MATRIZES ---
    print(f"\n▶ PARÂMETROS DA PROJEÇÃO:")
    print(f"   znear = {Z_NEAR:.4f} (DIA/100) | zfar = {Z_FAR:.2f} (10*DIA)")
    print(f"   FOV = {FOV_GRAUS}° | Aspect Ratio = {ASPECT_RATIO:.3f}")

    print("\n▶ MATRIZ PROJECTION (M_norm_pers) [4x4]:")
    for row in Projection:
        print(f"     [ {row[0]:8.4f}  {row[1]:8.4f}  {row[2]:8.4f}  {row[3]:8.4f} ]")

    # --- CÁLCULO VÉRTICE A VÉRTICE DO PIPELINE ---
    print("\n▶ PROCESSAMENTO DOS VÉRTICES NO PIPELINE:")
    print(f"{'Vér.':<4} | {'Espaço Local':<18} | {'Espaço Mundo':<22} | {'Espaço Visão':<22} | {'Espaço Clip':<22} | {'NDC (Após Div. Persp.)':<22}")
    print("-" * 135)

    for i, v_loc in enumerate(vertices_locais):
        p_local = mathutils.Vector((v_loc[0], v_loc[1], v_loc[2], 1.0))
        
        # Transformações sucessivas [1, 23]
        p_mundo = Model @ p_local
        p_visao = View @ p_mundo
        p_clip = Projection @ p_visao
        
        # Divisão Perspectiva (Normalização de Clip Space para NDC) [14, 35]
        # Se w_clip for zero ou muito próximo, evitamos divisão por zero
        w_c = p_clip.w
        if abs(w_c) > 0.0001:
            p_ndc = mathutils.Vector((p_clip.x / w_c, p_clip.y / w_c, p_clip.z / w_c))
        else:
            p_ndc = mathutils.Vector((0.0, 0.0, 0.0))

        # Formatando strings para visualização tabular
        str_loc = f"({p_local.x:4.1f}, {p_local.y:4.1f}, {p_local.z:4.1f})"
        str_mun = f"({p_mundo.x:5.2f}, {p_mundo.y:5.2f}, {p_mundo.z:5.2f})"
        str_vis = f"({p_visao.x:5.2f}, {p_visao.y:5.2f}, {p_visao.z:5.2f})"
        str_clp = f"({p_clip.x:5.2f}, {p_clip.y:5.2f}, {p_clip.z:5.2f}, {p_clip.w:5.2f})"
        str_ndc = f"({p_ndc.x:5.2f}, {p_ndc.y:5.2f}, {p_ndc.z:5.2f})"
        
        print(f"V{i:<2}  | {str_loc:<18} | {str_mun:<22} | {str_vis:<22} | {str_clp:<22} | {str_ndc:<22}")

    # --- 4. CONFIGURAÇÃO DA CÂMERA NO BLENDER ---
    # Cria uma câmera física para visualizarmos na Viewport exatamente o que calculamos
    cam_data = bpy.data.cameras.new("Camera_Projecao_Data")
    cam_obj = bpy.data.objects.new("Camera_Projecao", cam_data)
    bpy.context.scene.collection.objects.link(cam_obj)
    
    # Aplica a rotação/translação de câmera de acordo com a inversa da Matriz View [43]
    cam_obj.matrix_world = View.inverted()
    
    # Configura os limites clipping e lente com base nos cálculos teóricos
    cam_data.lens_unit = 'FOV'
    cam_data.angle = math.radians(FOV_GRAUS)
    cam_data.clip_start = Z_NEAR
    cam_data.clip_end = Z_FAR
    
    # Ativa a câmera recém-criada como câmera ativa da cena
    bpy.context.scene.camera = cam_obj
    
    print("\n▶ [PASSO EXTRA] Câmera do Blender configurada com os parâmetros físicos exatos!")
    print(f"   Camera Clip Start = {cam_data.clip_start:.4f} | Clip End = {cam_data.clip_end:.2f}")
    print("="*95 + "\n")

if __name__ == "__main__":
    limpar_cena_atual()
    piramide, vertices_loc = criar_piramide_local()
    construir_matrizes_e_projetar(piramide, vertices_loc)
