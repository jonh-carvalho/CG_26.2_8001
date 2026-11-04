import bpy
import math
import mathutils

# Parâmetros de Aniversário (Dia D, Mês M)
DIA = 15  # Dia (D)
MES = 10  # Mês (M)

def limpar_cena():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def atividade_curvas_parametrica_vs_nao_parametrica():
    limpar_cena()
    
    print("\n" + "="*80)
    print("   CG PRÁTICA: CURVAS PARAMÉTRICAS VS. NÃO-PARAMÉTRICAS NO BLENDER 4.5 LTS")
    print("="*80)
    
    # -------------------------------------------------------------------------
    # 1. CURVA NÃO-PARAMÉTRICA EXPLÍCITA (Parábola: y = a*x^2 + b*x + c)
    # -------------------------------------------------------------------------
    # Limitação: Cada valor de x gera exatamente um valor de y (função de valor único).
    a = 0.1 * (MES / 5.0)
    b = 0.0
    c = 0.0
    
    verts_explicita = []
    num_amostras = 50
    x_min, x_max = -5.0, 5.0
    dx = (x_max - x_min) / (num_amostras - 1)
    
    for i in range(num_amostras):
        x = x_min + i * dx
        y = a * (x ** 2) + b * x + c
        z = 0.0
        verts_explicita.append((x, y, z))
        
    edges_explicita = [(i, i + 1) for i in range(num_amostras - 1)]
    
    mesh_exp = bpy.data.meshes.new("NaoParametrica_Explicita_Mesh")
    mesh_exp.from_pydata(verts_explicita, edges_explicita, [])
    mesh_exp.update()
    
    obj_exp = bpy.data.objects.new("Curva_Explicita_Parabola", mesh_exp)
    bpy.context.scene.collection.objects.link(obj_exp)
    obj_exp.location.z = 0.0
    
    print(f"\n1. Curva Não-Paramétrica Explícita (Parábola y = {a:.2f}*x^2) gerada com {num_amostras} pontos.")

    # -------------------------------------------------------------------------
    # 2. CURVA PARAMÉTRICA CÚBICA DE BÉZIER (Amostrada algebricamente via Bernstein)
    # -------------------------------------------------------------------------
    # P(t) = (1-t)^3 * P0 + 3*t*(1-t)^2 * P1 + 3*t^2*(1-t) * P2 + t^3 * P3,  0 <= t <= 1
    P0 = mathutils.Vector((-4.0, 0.0, 3.0))
    P1 = mathutils.Vector((-1.0, 0.5 * MES, 3.0))
    P2 = mathutils.Vector((1.0, -0.5 * DIA, 3.0))
    P3 = mathutils.Vector((4.0, 0.0, 3.0))
    
    verts_bezier_amostrada = []
    dt = 1.0 / (num_amostras - 1)
    
    for i in range(num_amostras):
        t = i * dt
        # Polinômios de Bernstein de grau 3
        b0 = (1.0 - t) ** 3
        b1 = 3.0 * t * ((1.0 - t) ** 2)
        b2 = 3.0 * (t ** 2) * (1.0 - t)
        b3 = t ** 3
        
        P_t = b0 * P0 + b1 * P1 + b2 * P2 + b3 * P3
        verts_bezier_amostrada.append((P_t.x, P_t.y, P_t.z))
        
    edges_bezier = [(i, i + 1) for i in range(num_amostras - 1)]
    
    mesh_bez = bpy.data.meshes.new("Parametrica_Bezier_Bernstein_Mesh")
    mesh_bez.from_pydata(verts_bezier_amostrada, edges_bezier, [])
    mesh_bez.update()
    
    obj_bez = bpy.data.objects.new("Curva_Parametrica_Bezier_Amostrada", mesh_bez)
    bpy.context.scene.collection.objects.link(obj_bez)
    
    print(f"2. Curva Paramétrica de Bézier Cúbica gerada via Polinômios de Bernstein com 4 Pontos de Controle:")
    print(f"   • P0 = {list(P0)}")
    print(f"   • P1 = {list(P1)}")
    print(f"   • P2 = {list(P2)}")
    print(f"   • P3 = {list(P3)}")

    # -------------------------------------------------------------------------
    # 3. CURVA DE BÉZIER NATIVA DO BLENDER (Objeto CURVE)
    # -------------------------------------------------------------------------
    curve_data = bpy.data.curves.new(name="Bezier_Nativa_Data", type='CURVE')
    curve_data.dimensions = '3D'
    
    spline = curve_data.splines.new('BEZIER')
    spline.bezier_points.add(1)  # Já possui 1 ponto padrão, totalizando 2 pontos (início e fim)
    
    # Ponto Inicial
    p_start = spline.bezier_points[0]
    p_start.co = P0
    p_start.handle_right = P1
    p_start.handle_left_type = 'VECTOR'
    
    # Ponto Final
    p_end = spline.bezier_points[1]
    p_end.co = P3
    p_end.handle_left = P2
    p_end.handle_right_type = 'VECTOR'
    
    obj_curve_nativa = bpy.data.objects.new("Curva_Parametrica_Bezier_Nativa", curve_data)
    obj_curve_nativa.location.z = 2.0  # Deslocada para comparação visual
    bpy.context.scene.collection.objects.link(obj_curve_nativa)
    
    print("\n3. Objeto de Curva Nativo do Blender criado com Suporte Paramétrico para Edição Interativa!")
    print("="*80 + "\n")

if __name__ == "__main__":
    atividade_curvas_parametrica_vs_nao_parametrica()
