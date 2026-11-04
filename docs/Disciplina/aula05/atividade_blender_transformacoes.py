import bpy
import mathutils
import math

# ==============================================================================
# ATIVIDADE PRÁTICA: TRANSFORMAÇÕES GEOMÉTRICAS 3D (BLENDER 4.5)
# Disciplina: Computação Gráfica / Fundamentos das Transformações
#
# OBJETIVO:
# 1. Criar uma pirâmide no Espaço Local conforme especificado nas notas de aula.
# 2. Aplicar a transformação Model (Escala, Rotação e Translação) parametrizada
#    com base no dia (D) e mês (M) de nascimento do aluno.
# 3. Exibir no console os vértices originais (Local) e os transformados (Mundo).
# ==============================================================================

# --- [PASSO 1]: PARAMETRIZAÇÃO DO SEU ANIVERSÁRIO ---
# Altere os valores abaixo com o seu dia e mês de nascimento para personalizar:
DIA = 15  # Substitua pelo seu dia (D)
MES = 10  # Substitua pelo seu mês (M)

def limpar_cena_atual():
    """Remove todos os objetos da cena do Blender para começar limpo."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def criar_piramide_local():
    """
    Cria a pirâmide tridimensional no Espaço Local com base nas notas de aula:
    - Ápice: (0, 1, 0)
    - Base: quadrilátero com vértices (-0.5, 0, 0.5), (0.5, 0, 0.5), (0.5, 0, -0.5), (-0.5, 0, -0.5)
    """
    # Coordenadas locais (Aula 7 - Exercícios II)
    vertices_locais = [
        (0.0, 1.0, 0.0),          # V0: Ápice (Y é a altura no espaço OpenGL/Slides)
        (-0.5, 0.0, 0.5),         # V1: Base Frontal-Esquerda
        (0.5, 0.0, 0.5),          # V2: Base Frontal-Direita
        (0.5, 0.0, -0.5),         # V3: Base Traseira-Direita
        (-0.5, 0.0, -0.5)         # V4: Base Traseira-Esquerda
    ]
    
    # Faces divididas em triângulos para facilitar a renderização (Aula 8)
    faces_locais = [
        (0, 1, 2),  # Face Lateral Frontal
        (0, 2, 3),  # Face Lateral Direita
        (0, 3, 4),  # Face Lateral Traseira
        (0, 4, 1),  # Face Lateral Esquerda
        (1, 4, 3),  # Base - Triângulo A
        (1, 3, 2)   # Base - Triângulo B
    ]
    
    # Criação do objeto e da malha no banco de dados do Blender
    mesh = bpy.data.meshes.new("Piramide_Mesh")
    obj = bpy.data.objects.new("Piramide_Objeto", mesh)
    
    # Vincula o objeto à coleção principal da cena ativa
    cena = bpy.context.scene
    cena.collection.objects.link(obj)
    
    # Constrói a geometria da malha
    mesh.from_pydata(vertices_locais, [], faces_locais)
    mesh.update()
    
    return obj, vertices_locais

def executar_transformacoes_e_exibir(obj, vertices_locais):
    """
    Calcula manualmente as coordenadas do Espaço de Mundo usando matrizes homogêneas 4x4
    e depois aplica o resultado ao objeto 3D na Viewport do Blender.
    """
    print("\n" + "="*80)
    print("             CG PRÁTICA: TRANSFORMAÇÕES GEOMÉTRICAS COM PYTHON")
    print("="*80)
    
    # 1. Exibir vértices iniciais no Espaço Local
    print("\n▶ [PASSO A] Vértices Iniciais no ESPAÇO LOCAL:")
    for i, v in enumerate(vertices_locais):
        print(f"   V{i}_local = [{v[0]:5.2f}, {v[1]:5.2f}, {v[2]:5.2f}, 1.0]T")
        
    # 2. Configurar os fatores de transformação (Exercício 1 da Aula 8 / Aula 7)
    # - Lados da base multiplicados por M (eixos X e Z)
    # - Altura multiplicada por D (eixo Y)
    s_x = MES
    s_y = DIA  # Eixo de altura na convenção dos slides
    s_z = MES
    
    # Translação para garantir que o objeto fique no 1º octante (X >= 0, Y >= 0, Z >= 0)
    # Como a base esticada varia de -0.5*M a 0.5*M nos eixos X e Z:
    # Deslocamos por 0.5*M para mover o menor vértice (-0.5*M) para a origem (0.0).
    t_x = 0.5 * MES
    t_y = 0.0          # A altura já é >= 0, pois varia de 0.0 a DIA (Y >= 0)
    t_z = 0.5 * MES
    
    # Ângulo de rotação opcional em torno da altura (Y) para enriquecer a atividade
    angulo_rot = math.radians(45)  # 45 graus
    
    # 3. Construir as Matrizes Homogêneas 4x4
    # Matriz de Escala (S)
    S = mathutils.Matrix.Diagonal((s_x, s_y, s_z, 1.0))
    
    # Matriz de Rotação (R) de 45° em torno do eixo Y (Y-Up)
    # Na biblioteca 'mathutils' do Blender, especificamos a rotação passando o ângulo, tamanho 4x4 e o eixo 'Y'.
    R = mathutils.Matrix.Rotation(angulo_rot, 4, 'Y')
    
    # Matriz de Translação (T)
    T = mathutils.Matrix.Translation((t_x, t_y, t_z))
    
    # Matriz Model Composta (Model = T * R * S)
    # No Blender Python, a multiplicação de matrizes é realizada através do operador '@'
    Model = T @ R @ S
    
    print("\n▶ [PASSO B] Matrizes Homogêneas Utilizadas (Convenção OpenGL / Vetores-Coluna):")
    print(f"   - Fatores de Escala: Sx={s_x}, Sy={s_y}, Sz={s_z}")
    print(f"   - Vetor de Translação: Tx={t_x:.2f}, Ty={t_y:.2f}, Tz={t_z:.2f}")
    print("\n   Matriz Model Composta (M_model = T * R * S):")
    for row in Model:
        print(f"     [ {row[0]:6.2f}  {row[1]:6.2f}  {row[2]:6.2f}  {row[3]:6.2f} ]")
        
    # 4. Multiplicar manualmente cada vértice pela matriz composta
    # P_mundo = M_model * P_local
    print("\n▶ [PASSO C] Vértices Calculados no ESPAÇO MUNDO (Multiplicação de Matriz):")
    for i, v_loc in enumerate(vertices_locais):
        # Converte para vetor homogêneo 4D [x, y, z, 1]
        p_local_4d = mathutils.Vector((v_loc[0], v_loc[1], v_loc[2], 1.0))
        
        # Realiza o produto matriz-vetor (Model @ ponto)
        p_mundo_4d = Model @ p_local_4d
        
        # Divisão perspectiva (opcional aqui, pois h=1.0 em transformações afins ordinárias)
        p_mundo_3d = mathutils.Vector((
            p_mundo_4d[0] / p_mundo_4d[3],
            p_mundo_4d[1] / p_mundo_4d[3],
            p_mundo_4d[2] / p_mundo_4d[3]
        ))
        print(f"   V{i}_mundo = [{p_mundo_3d[0]:7.2f}, {p_mundo_3d[1]:7.2f}, {p_mundo_3d[2]:7.2f}]")
        
    # 5. Aplicar a transformação final diretamente no Blender
    # No Blender, definir a 'matrix_world' do objeto aplica a transformação global instantaneamente na 3D Viewport.
    obj.matrix_world = Model
    print("\n▶ [PASSO D] Objeto atualizado visualmente na Viewport 3D do Blender!")
    print("="*80 + "\n")

# --- EXECUÇÃO DO SCRIPT ---
if __name__ == "__main__":
    limpar_cena_atual()
    piramide, vertices_loc = criar_piramide_local()
    executar_transformacoes_e_exibir(piramide, vertices_loc)
