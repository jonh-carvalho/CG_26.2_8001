import bpy
import mathutils
import math
import os

# Parâmetros de Aniversário (Dia D, Mês M)
DIA = 15  # Dia de nascimento (D)
MES = 10  # Mês de nascimento (M)

def limpar_cena():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def atividade_csg_para_brep_e_export_obj():
    limpar_cena()
    
    print("\n" + "="*80)
    print("   CG PRÁTICA: CONVERSÃO DE ÁRVORE CSG PARA B-REP E EXPORTAÇÃO WAVEFRONT .OBJ")
    print("="*80)
    
    # -------------------------------------------------------------------------
    # 1. CONSTRUÇÃO DA ÁRVORE CSG (Nós Primitivas e Modificadores Booleanos)
    # -------------------------------------------------------------------------
    largura_base = 8.0 + (MES * 0.2)   
    comprimento_base = 8.0 + (DIA * 0.2) 
    altura_base = 2.0                  
    
    raio_flange = 2.0 + (MES * 0.1)
    altura_flange = 2.0
    
    raio_furo_central = 1.0 + (MES * 0.05)
    raio_furo_canto = 0.5
    
    # Primitiva Base
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, altura_base/2.0))
    bloco_base = bpy.context.active_object
    bloco_base.name = "Peca_Mecanica_CSG"
    bloco_base.scale = (largura_base, comprimento_base, altura_base)
    bpy.ops.object.transform_apply(scale=True)
    
    # Primitiva Flange
    bpy.ops.mesh.primitive_cylinder_add(
        radius=raio_flange, 
        depth=altura_flange, 
        location=(0, 0, altura_base + (altura_flange/2.0))
    )
    flange = bpy.context.active_object
    
    # Primitiva Cortador Central
    altura_cortador_central = altura_base + altura_flange + 2.0
    bpy.ops.mesh.primitive_cylinder_add(
        radius=raio_furo_central, 
        depth=altura_cortador_central, 
        location=(0, 0, altura_cortador_central/2.0 - 1.0)
    )
    furo_central = bpy.context.active_object
    
    # Primitivas Cortadores de Canto
    offset_x = (largura_base / 2.0) - 1.0
    offset_y = (comprimento_base / 2.0) - 1.0
    posicoes_cantos = [
        (offset_x, offset_y), (-offset_x, offset_y),
        (-offset_x, -offset_y), (offset_x, -offset_y)
    ]
    
    cortadores_cantos = []
    for cx, cy in posicoes_cantos:
        bpy.ops.mesh.primitive_cylinder_add(
            radius=raio_furo_canto, 
            depth=altura_base + 2.0, 
            location=(cx, cy, altura_base/2.0)
        )
        cortadores_cantos.append(bpy.context.active_object)

    # Aplicação da Pilha de Operações Booleanas (Árvore CSG Procedural)
    bpy.context.view_layer.objects.active = bloco_base
    
    # União (U*)
    mod = bloco_base.modifiers.new(name="CSG_Union", type='BOOLEAN')
    mod.operation = 'UNION'
    mod.object = flange
    
    # Diferença (-*) Furo Central
    mod = bloco_base.modifiers.new(name="CSG_Diff_Central", type='BOOLEAN')
    mod.operation = 'DIFFERENCE'
    mod.object = furo_central
    
    # Diferença (-*) Furos dos Cantos
    for i, canto in enumerate(cortadores_cantos, 1):
        mod = bloco_base.modifiers.new(name=f"CSG_Diff_Corner_{i}", type='BOOLEAN')
        mod.operation = 'DIFFERENCE'
        mod.object = canto

    # -------------------------------------------------------------------------
    # 2. AVALIAÇÃO DE FRONTEIRA (Boundary Evaluation: CSG -> B-Rep)
    # -------------------------------------------------------------------------
    print("\n▶ [PASSO 1] Executando 'Boundary Evaluation' (Aplicando modificadores CSG)...")
    
    # 'Aplicar' os modificadores no Blender colapsa a árvore CSG procedural
    # em uma malha explícita com fronteiras topológicas (B-Rep)
    for modifier in list(bloco_base.modifiers):
        bpy.ops.object.modifier_apply(modifier=modifier.name)
        
    # Deletar as primitivas auxiliares cortadoras
    bpy.ops.object.select_all(action='DESELECT')
    flange.select_set(True)
    furo_central.select_set(True)
    for c in cortadores_cantos:
        c.select_set(True)
    bpy.ops.object.delete()

    # Inspecionar os elementos topológicos B-Rep da malha resultante
    mesh_brep = bloco_base.data
    num_vertices = len(mesh_brep.vertices)
    num_arestas = len(mesh_brep.edges)
    num_faces = len(mesh_brep.polygons)
    
    print("\n▶ [PASSO 2] Estrutura Topológica B-Rep Gerada:")
    print(f"   • Vértices  (V) : {num_vertices}")
    print(f"   • Arestas   (E) : {num_arestas}")
    print(f"   • Faces     (F) : {num_faces}")
    
    # -------------------------------------------------------------------------
    # 3. EXPORTAÇÃO DA MALHA B-REP EM FORMATO WAVEFRONT .OBJ
    # -------------------------------------------------------------------------
    output_dir = os.path.expanduser("~")
    filepath_obj = os.path.join(output_dir, "peca_mecanica_brep.obj")
    
    # Selecionar apenas o objeto B-Rep final
    bpy.ops.object.select_all(action='DESELECT')
    bloco_base.select_set(True)
    bpy.context.view_layer.objects.active = bloco_base
    
    # Operador nativo de exportação OBJ do Blender 4.0+
    try:
        bpy.ops.wm.obj_export(
            filepath=filepath_obj,
            export_selected_objects=True,
            export_materials=False
        )
        print(f"\n▶ [PASSO 3] Arquivo Wavefront .OBJ exportado com sucesso!")
        print(f"   Caminho de saída: {filepath_obj}")
    except Exception as e:
        print(f"\n▶ [PASSO 3] Erro ao exportar OBJ via operador wm: {e}")

    print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    atividade_csg_para_brep_e_export_obj()
