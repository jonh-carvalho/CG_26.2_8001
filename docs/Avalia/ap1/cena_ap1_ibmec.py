import bpy
import math

def limpar_cena_inicial():
    """
    Remove todos os objetos padrão da cena (Cubo, Luz, Câmera)
    para garantir um ambiente limpo.
    """
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    # Limpa blocos de dados órfãos para manter o arquivo leve
    for mesh in bpy.data.meshes:
        if mesh.users == 0:
            bpy.data.meshes.remove(mesh)
    for curve in bpy.data.curves:
        if curve.users == 0:
            bpy.data.curves.remove(curve)

def criar_cena_ap1():
    # 1. LIMPEZA INICIAL
    limpar_cena_inicial()
    
    print("\n" + "="*80)
    print("      BLENDER 4.5 LTS - GERADOR AUTOMÁTICO DE CENA CONCEITO DA AP1")
    print("="*80)
    
    # 2. CRIAÇÃO DA COLEÇÃO PRINCIPAL (Requisito 2 da AP1)
    nome_colecao = "AP1_Ibmec_Conceito"
    colecao_ap1 = bpy.data.collections.new(nome_colecao)
    bpy.context.scene.collection.children.link(colecao_ap1)
    print(f"▶ Coleção '{nome_colecao}' criada com sucesso.")

    # Função auxiliar para mover objetos para a coleção principal
    def mover_para_colecao_ap1(obj):
        for col in obj.users_collection:
            col.objects.unlink(obj)
        colecao_ap1.objects.link(obj)

    # 3. CRIAÇÃO DA PALAVRA 'Ibmec' (Requisitos 3 e 6)
    print("▶ Gerando a marca 'Ibmec' (Texto 3D convertido para MalhaPoligonal)...")
    bpy.ops.object.text_add(location=(0.0, -0.3, 2.2))
    text_obj = bpy.context.active_object
    text_obj.name = "Ibmec_Texto"
    text_obj.data.body = "Ibmec"
    text_obj.data.size = 1.8
    text_obj.data.extrude = 0.15
    text_obj.data.bevel_depth = 0.02
    text_obj.data.align_x = 'CENTER'
    text_obj.data.align_y = 'CENTER'
    
    # Rotação para ficar em pé virado para a Câmera (90° em X)
    text_obj.rotation_euler = (math.radians(90), 0, 0)
    
    # Conversão de Texto para Malha Poligonal (Mesh)
    bpy.context.view_layer.objects.active = text_obj
    bpy.ops.object.convert(target='MESH')
    
    # Congela Transformações (All Transforms)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    mover_para_colecao_ap1(text_obj)

    # 4. OBJETO AUTORAL 1: Obj_PodioFuturista (Modelagem Poligonal)
    print("▶ Modelando Objeto Autoral 1: 'Obj_PodioFuturista'...")
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, 0.0, 0.5))
    podio = bpy.context.active_object
    podio.name = "Obj_PodioFuturista"
    podio.scale = (6.0, 3.5, 1.0)
    bpy.ops.object.transform_apply(scale=True)
    
    # Adiciona modificador Bevel para suavizar quinas do pódio
    mod_bevel = podio.modifiers.new(name="Suavizacao_Bevel", type='BEVEL')
    mod_bevel.width = 0.08
    mod_bevel.segments = 3
    mover_para_colecao_ap1(podio)

    # 5. OBJETO AUTORAL 2: Obj_PortalInovacao (Modificadores Solidify e Bevel)
    print("▶ Modelando Objeto Autoral 2: 'Obj_PortalInovacao'...")
    bpy.ops.mesh.primitive_cylinder_add(
        radius=3.2, 
        depth=0.3, 
        vertices=64, 
        location=(0.0, 0.5, 2.8),
        rotation=(math.radians(90), 0, 0)
    )
    portal = bpy.context.active_object
    portal.name = "Obj_PortalInovacao"
    
    # Entra no Edit Mode para remover as faces frontal e traseira (deixando o cilindro oco)
    bpy.context.view_layer.objects.active = portal
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Seleciona faces de tampa (z local / normal direcionada em Y)
    mesh_portal = portal.data
    for polygon in mesh_portal.polygons:
        if abs(polygon.normal.z) > 0.9:
            polygon.select = True
            
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.delete(type='FACE')
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Aplica modificador Solidify para dar espessura estrutural
    mod_solid = portal.modifiers.new(name="Espessura_Solidify", type='SOLIDIFY')
    mod_solid.thickness = 0.25
    
    # Aplica modificador Bevel para acabamento
    mod_bevel_p = portal.modifiers.new(name="Bordas_Bevel", type='BEVEL')
    mod_bevel_p.width = 0.03
    mod_bevel_p.segments = 2
    
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    mover_para_colecao_ap1(portal)

    # 6. OBJETO AUTORAL 3: Obj_TrofeuMarco (Modelagem por Curva Bézier + Modificador Screw)
    print("▶ Modelando Objeto Autoral 3: 'Obj_TrofeuMarco'...")
    curve_data = bpy.data.curves.new(name="Perfil_Trofeu_Curve", type='CURVE')
    curve_data.dimensions = '3D'
    
    spline = curve_data.splines.new('BEZIER')
    spline.bezier_points.add(3) # Total de 4 pontos de controle no perfil
    
    # Posições do perfil 2D da taça/troféu (X=Raio, Z=Altura)
    pts = spline.bezier_points
    pts[0].co = (0.05, 0.0, 0.0)   # Centro da Base
    pts[1].co = (0.6,  0.0, 0.1)   # Borda da Base
    pts[2].co = (0.15, 0.0, 0.8)   # Haste Fina Central
    pts[3].co = (0.5,  0.0, 1.6)   # Bojo Superior
    
    # Suaviza os pontos de controle
    for p in pts:
        p.handle_left_type = 'AUTO'
        p.handle_right_type = 'AUTO'
        
    trofeu = bpy.data.objects.new("Obj_TrofeuMarco", curve_data)
    trofeu.location = (2.2, -0.8, 1.0)
    bpy.context.scene.collection.objects.link(trofeu)
    
    # Aplica o modificador Screw para revolução 360° em Z
    mod_screw = trofeu.modifiers.new(name="Revolucao_Screw", type='SCREW')
    mod_screw.axis = 'Z'
    mod_screw.steps = 32
    mod_screw.render_steps = 32
    mover_para_colecao_ap1(trofeu)

    # 7. CONFIGURAÇÃO DA CÂMERA PRINCIPAL (Requisito 7)
    print("▶ Posicionando e configurando 'Cam_Principal_AP1'...")
    bpy.ops.object.camera_add(
        location=(0.0, -9.0, 2.8),
        rotation=(math.radians(82), 0, 0)
    )
    cam = bpy.context.active_object
    cam.name = "Cam_Principal_AP1"
    cam.data.lens = 50.0 # Lente de 50mm padrão de retrato/composição
    cam.data.show_composition_thirds = True # Guias da Regra dos Terços
    
    # Define como Câmera Ativa da Cena
    bpy.context.scene.camera = cam
    mover_para_colecao_ap1(cam)

    # 8. ELEMENTO AUXILIAR: Iluminação Básica
    bpy.ops.object.light_add(type='SUN', location=(5.0, -5.0, 10.0))
    sol = bpy.context.active_object
    sol.name = "Luz_Sol_Principal"
    sol.data.energy = 3.0
    mover_para_colecao_ap1(sol)

    # 9. CONFIGURAÇÃO DA LINHA DO TEMPO (Requisito 8: 15s @ 24fps = 360 frames)
    print("▶ Configurando Timeline: 360 Frames a 24 fps (15 Segundos)...")
    bpy.context.scene.render.fps = 24
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 360
    bpy.context.scene.frame_current = 1

    print("="*80)
    print(" SUCCESS: Cena conceitual da AP1 gerada com sucesso no Blender 4.5 LTS!")
    print(" Toque 'Numpad 0' na Viewport 3D para visualizar o enquadramento final.")
    print("="*80 + "\n")

if __name__ == "__main__":
    criar_cena_ap1()
