import bpy
import mathutils
import math

# ==============================================================================
# CG PRÁTICA: MODELAGEM GEOMÉTRICA CONSTRUTIVA (CSG) NO BLENDER 4.5 LTS
# ==============================================================================
# Altere as variáveis com a sua data de nascimento (Dia D, Mês M)
DIA = 15  # Dia de nascimento (D)
MES = 10  # Mês de nascimento (M)

def limpar_cena():
    """Remove todos os objetos existentes na cena para reiniciar o ambiente."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def criar_material(nome, cor_rgba):
    """Cria e retorna um material simples com a cor especificada."""
    mat = bpy.data.materials.new(name=nome)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = cor_rgba
    return mat

def executar_atividade_csg():
    limpar_cena()
    
    print("\n" + "="*80)
    print("        CG PRÁTICA: GEOMETRIA CONSTRUTIVA DE SÓLIDOS (CSG) - BLENDER 4.5 LTS")
    print("="*80)
    
    # --------------------------------------------------------------------------
    # 1. PARÂMETROS DAS PRIMITIVAS (Baseados na data de nascimento)
    # --------------------------------------------------------------------------
    largura_base = 8.0 + (MES * 0.2)   # X
    comprimento_base = 8.0 + (DIA * 0.2) # Y
    altura_base = 2.0                  # Z
    
    raio_flange = 2.0 + (MES * 0.1)
    altura_flange = 2.0
    
    raio_furo_central = 1.0 + (MES * 0.05)
    raio_furo_canto = 0.5
    
    print(f"▶ [1] Dimensões da Peça (Parametrizadas para D={DIA}, M={MES}):")
    print(f"    - Bloco Base (Primitiva A): {largura_base:.2f} x {comprimento_base:.2f} x {altura_base:.2f}")
    print(f"    - Flange Cilíndrica (Primitiva B): Raio={raio_flange:.2f}, Altura={altura_flange:.2f}")
    print(f"    - Furo Central Passante (Primitiva C): Raio={raio_furo_central:.2f}")
    print(f"    - Furos de Fixação nos Cantos (Primitivas D1..D4): Raio={raio_furo_canto:.2f}")
    
    # --------------------------------------------------------------------------
    # 2. CRIAÇÃO DAS PRIMITIVAS GEOMÉTRICAS (Folhas da Árvore CSG)
    # --------------------------------------------------------------------------
    
    # (A) Bloco Base
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, altura_base/2.0))
    bloco_base = bpy.context.active_object
    bloco_base.name = "CSG_Base_Block"
    bloco_base.scale = (largura_base, comprimento_base, altura_base)
    bpy.ops.object.transform_apply(scale=True)
    
    # (B) Flange Cilíndrica (para União U*)
    bpy.ops.mesh.primitive_cylinder_add(
        radius=raio_flange, 
        depth=altura_flange, 
        location=(0, 0, altura_base + (altura_flange/2.0))
    )
    flange = bpy.context.active_object
    flange.name = "CSG_Flange_Cylinder"
    
    # (C) Cortador do Furo Central Passante (para Diferença -*)
    altura_cortador_central = altura_base + altura_flange + 2.0
    bpy.ops.mesh.primitive_cylinder_add(
        radius=raio_furo_central, 
        depth=altura_cortador_central, 
        location=(0, 0, altura_cortador_central/2.0 - 1.0)
    )
    furo_central = bpy.context.active_object
    furo_central.name = "CSG_Cutter_CentralHole"
    
    # (D) Cortadores dos 4 Furos dos Cantos (para Diferença -*)
    offset_x = (largura_base / 2.0) - 1.0
    offset_y = (comprimento_base / 2.0) - 1.0
    posicoes_cantos = [
        (offset_x, offset_y),
        (-offset_x, offset_y),
        (-offset_x, -offset_y),
        (offset_x, -offset_y)
    ]
    
    cortadores_cantos = []
    for i, (cx, cy) in enumerate(posicoes_cantos, 1):
        bpy.ops.mesh.primitive_cylinder_add(
            radius=raio_furo_canto, 
            depth=altura_base + 2.0, 
            location=(cx, cy, altura_base/2.0)
        )
        canto_obj = bpy.context.active_object
        canto_obj.name = f"CSG_Cutter_Corner_{i}"
        cortadores_cantos.append(canto_obj)

    # Materiais visuais para distinguir as primitivas
    mat_principal = criar_material("Mat_Peca", (0.1, 0.4, 0.8, 1.0)) # Azul
    mat_cortador = criar_material("Mat_Cortador", (0.9, 0.2, 0.2, 0.4)) # Vermelho translúcido
    
    bloco_base.data.materials.append(mat_principal)
    flange.data.materials.append(mat_principal)
    furo_central.data.materials.append(mat_cortador)
    for c in cortadores_cantos:
        c.data.materials.append(mat_cortador)

    # --------------------------------------------------------------------------
    # 3. CONSTRUÇÃO E APLICAÇÃO DA ÁRVORE CSG (Operações Booleanas)
    # Estrutura: Peça = ((Base U* Flange) -* FuroCentral) -* FurosCantos
    # --------------------------------------------------------------------------
    print("\n▶ [2] Processando Árvore CSG...")
    
    # Seleciona o objeto principal
    bpy.context.view_layer.objects.active = bloco_base
    
    # OP1: UNIAO (Base U* Flange)
    mod_uniao = bloco_base.modifiers.new(name="CSG_Union_Flange", type='BOOLEAN')
    mod_uniao.operation = 'UNION'
    mod_uniao.operand = 'OBJECT'
    mod_uniao.object = flange
    mod_uniao.solver = 'EXACT'
    print("    [CSG Tree Node 1] União (U*): Base + Flange")
    
    # OP2: DIFERENÇA ( -* Furo Central )
    mod_furo_c = bloco_base.modifiers.new(name="CSG_Diff_CentralHole", type='BOOLEAN')
    mod_furo_c.operation = 'DIFFERENCE'
    mod_furo_c.operand = 'OBJECT'
    mod_furo_c.object = furo_central
    mod_furo_c.solver = 'EXACT'
    print("    [CSG Tree Node 2] Diferença (-*): Subtração do Furo Central Passante")
    
    # OP3..6: DIFERENÇA ( -* Furos dos Cantos )
    for i, canto_obj in enumerate(cortadores_cantos, 1):
        mod_canto = bloco_base.modifiers.new(name=f"CSG_Diff_CornerHole_{i}", type='BOOLEAN')
        mod_canto.operation = 'DIFFERENCE'
        mod_canto.operand = 'OBJECT'
        mod_canto.object = canto_obj
        mod_canto.solver = 'EXACT'
    print("    [CSG Tree Node 3..6] Diferença (-*): Subtração dos 4 Furos de Fixação nos Cantos")

    # Oculta as primitivas operandas na Viewport para visualizar o sólido CSG resultante
    flange.hide_viewport = True
    flange.hide_render = True
    furo_central.hide_viewport = True
    furo_central.hide_render = True
    for c in cortadores_cantos:
        c.hide_viewport = True
        c.hide_render = True

    # --------------------------------------------------------------------------
    # 4. CONFIGURAÇÃO DA CÂMERA E ILUMINAÇÃO PARA RENDERIZAÇÃO
    # --------------------------------------------------------------------------
    bpy.ops.object.light_add(type='SUN', location=(10, -10, 15))
    sol = bpy.context.active_object
    sol.data.energy = 3.0
    
    bpy.ops.object.camera_add(location=(12, -12, 10), rotation=(math.radians(55), 0, math.radians(45)))
    cam = bpy.context.active_object
    bpy.context.scene.camera = cam

    print("\n▶ [3] Modelo Sólido Construtivo (CSG) gerado com sucesso no Blender 4.5!")
    print("    - O objeto principal 'CSG_Base_Block' agora contém a pilha de modificadores CSG.")
    print("    - Para aplicar permanentemente a geometria, selecione 'CSG_Base_Block' e vá em Modifiers > Apply All.")
    print("="*80 + "\n")

if __name__ == "__main__":
    executar_atividade_csg()
