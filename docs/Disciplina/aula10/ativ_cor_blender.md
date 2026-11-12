## Laboratório 3D em Blender 4.5: Síntese Aditiva e Percepção Visual

### **Objetivos Didáticos:**

1. **Projeção de Maxwell e Síntese Aditiva**: Visualizar computacionalmente a superposição dos fidedignos primários de luz (\\(R, G, B\\)) gerando as cores secundárias (\\(C, M, Y\\)) e a luz branca (\\(W\\)).
2. **Absorção Seletiva de Luz-Matéria**: Observar como pigmentos coloridos (matéria) respondem quando iluminados por fontes de luz monocromáticas ou filtradas.
3. **Gestão de Cor e Gerenciamento Cromatico**: Utilizar a transformação de visualização **AgX** (padrão do Blender 4.x+) para simular a resposta fotorreceptora da retina sem contaminação por iluminação estourada (*clipping*).

---

### **1. Script em Python para a Aba *Scripting* do Blender 4.5**

Abra o Blender 4.5, vá até a aba **Scripting**, crie um novo texto, cole o código abaixo e clique em **Run Script** (\\(\triangleright\\)). O script monta automaticamente a cena de testes, as luzes RGB direcionadas, o plano difuso e três objetos com pigmentos primários.

```python
import bpy
import math

# ==============================================================================
# 1. LIMPEZA DA CENA
# ==============================================================================
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# ==============================================================================
# 2. CONFIGURAÇÃO DO ENGINE E GERENCIAMENTO DE COR (AgX)
# ==============================================================================
scene = bpy.context.scene
# Configuração do motor de renderização para EEVEE Next (Blender 4.5)
scene.render.engine = 'BLENDER_EEVEE_NEXT' 
# Configuração de gerenciamento de cor para simular a resposta fotorreceptora da retina
scene.display_settings.display_device = 'sRGB'
# AgX é a transformação de visualização moderna que simula a resposta fotorreceptora da retina
scene.view_settings.view_transform = 'AgX' # Transformação moderna de iluminação

# ==============================================================================
# 3. TELA BRANCA DE PROJEÇÃO (Pano de Fundo Difuso)
# ==============================================================================
bpy.ops.mesh.primitive_plane_add(size=12, location=(0, 0, 0))
plane = bpy.context.active_object
plane.name = "Plano_Projecao"

mat_plane = bpy.data.materials.new(name="Mat_Branco_Difuso")
mat_plane.use_nodes = True
p_plane = mat_plane.node_tree.nodes.get("Principled BSDF")
if p_plane:
    p_plane.inputs["Base Color"].default_value = (1.0, 1.0, 1.0, 1.0) # Reflectância 100%
    p_plane.inputs["Roughness"].default_value = 0.9
plane.data.materials.append(mat_plane)

# ==============================================================================
# 4. FONTES DE LUZ ADITIVA (PROJETORES SPOT RGB)
# ==============================================================================
# Luzes posicionadas em triângulo focando no centro da tela
spots_data = [
    ("Spot_Red",   (1.0, 0.0, 0.0), (-1.2, -3.0, 4.0), (math.radians(35), 0, math.radians(-15))),
    ("Spot_Green", (0.0, 1.0, 0.0), ( 1.2, -3.0, 4.0), (math.radians(35), 0, math.radians(15))),
    ("Spot_Blue",  (0.0, 0.0, 1.0), ( 0.0, -4.2, 3.2), (math.radians(45), 0, 0))
]

for name, color, loc, rot in spots_data:
    light_data = bpy.data.lights.new(name=name, type='SPOT')
    light_data.energy = 800  # Potência em Watts
    light_data.color = color
    light_data.spot_size = math.radians(50)
    light_data.spot_blend = 0.4 # Suavidade das bordas
    
    light_obj = bpy.data.objects.new(name=name, object_data=light_data)
    bpy.context.collection.objects.link(light_obj)
    light_obj.location = loc
    light_obj.rotation_euler = rot

# ==============================================================================
# 5. OBJETOS DE PIGMENTO (Testes de Absorção/Reflexão)
# ==============================================================================
objetos = [
    ("Esfera_Vermelha", 'SPHERE',   (-2.0, 0.5, 0.6), (0.9, 0.05, 0.05, 1.0)),
    ("Cubo_Verde",      'CUBE',     ( 0.0, 0.5, 0.6), (0.05, 0.9, 0.05, 1.0)),
    ("Cilindro_Azul",   'CYLINDER', ( 2.0, 0.5, 0.6), (0.05, 0.05, 0.9, 1.0))
]

for name, mesh_type, loc, rgba in objetos:
    if mesh_type == 'SPHERE':
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.6, location=loc)
    elif mesh_type == 'CUBE':
        bpy.ops.mesh.primitive_cube_add(size=1.2, location=loc)
    elif mesh_type == 'CYLINDER':
        bpy.ops.mesh.primitive_cylinder_add(radius=0.6, depth=1.2, location=loc)
        
    obj = bpy.context.active_object
    obj.name = name
    
    mat = bpy.data.materials.new(name=f"Mat_{name}")
    mat.use_nodes = True
    p_node = mat.node_tree.nodes.get("Principled BSDF")
    if p_node:
        p_node.inputs["Base Color"].default_value = rgba
        p_node.inputs["Roughness"].default_value = 0.4
    obj.data.materials.append(mat)

# ==============================================================================
# 6. CÂMERA E VISUALIZAÇÃO
# ==============================================================================
bpy.ops.object.camera_add(location=(0, -7.5, 5.0), rotation=(math.radians(50), 0, 0))
cam = bpy.context.active_object
scene.camera = cam

print("Laboratório de Cor e Visão Humana criado com sucesso no Blender 4.5!")
```

---

### **2. Roteiro de Experimentos Práticos para os Alunos**

#### **Experimento A: Comprovação da Projeção de Maxwell (Síntese Aditiva)**
1. Mude a visualização do Viewport para **Rendered** (`Z` \\(\rightarrow\\) *Rendered*).
2. Oculte temporariamente os 3 objetos geométricos da cena.
3. Observe no plano branco as interseções das luzes dos três projetores (*Spots*):
   * **Vermelho + Verde**: resulta em **Amarelo**.
   * **Verde + Azul**: resulta em **Ciano**.
   * **Vermelho + Azul**: resulta em **Magenta**.
   * **Interseção Tripla no Centro**: resulta no **Branco**.

#### **Experimento B: Fenômeno de Absorção e Iluminação Monocromática**
1. Reexiba os três objetos na cena (**Esfera Vermelha**, **Cubo Verde**, **Cilindro Azul**).
2. No painel de objetos (*Outliner*), desative as luzes `Spot_Red` e `Spot_Blue`, deixando ligada apenas a **`Spot_Green`** (Luz Verde).
3. **Pergunta para o aluno**: *O que acontece com a aparência da Esfera Vermelha sob luz exclusivamente verde?*
   * **Resposta esperada**: A esfera vermelha parecerá **escura/preta**, pois seu pigmento só reflete comprimentos de onda longos (vermelhos) e absorve totalmente os médios (verdes). Como não há luz vermelha no ambiente, não há radiação refletida até a câmera.

#### **Experimento C: Alterando Temperatura de Cor via Shader Nodes**
1. Selecione a luz `Spot_Red`.
2. No Editor de Nodos (*Shader Editor* com tipo *Light* selecionado), adicione o nodo **Blackbody** (Corpo Negro).
3. Conecte a saída *Color* do nodo **Blackbody** à entrada *Color* do nodo de saída da luz.
4. Varie o parâmetro `Temperature` entre **2000 K** (luz alaranjada/quente, estilo vela/incandescente) e **7500 K** (luz azulada/fria, estilo céu nublado) para observar o deslocamento espectral na cena.


💡 *Gostaria que eu adaptasse este script para exportar automaticamente as renderizações comparativas dos experimentos para uma pasta do seu computador?*