# Visualizando o Modelo de Iluminação de Phong no Blender

O modelo de Phong é uma técnica de iluminação que simula como a luz interage com superfícies, combinando três componentes: ambiente, difusa e especular.

## Exemplo Prático no Blender

### 1. Configuração Básica da Cena
- Adicione uma esfera (Shift + A → Mesh → Sphere)
- Adicione um plano como superfície abaixo da esfera
- Adicione uma luz pontual (Shift + A → Light → Point)

### 2. Configurando o Material com Shader Phong

```python
# Script Python para configurar material Phong (opcional)
import bpy

# Criar novo material
material = bpy.data.materials.new(name="Phong_Material")
material.use_nodes = True
nodes = material.node_tree.nodes

# Limpar nodes padrão
nodes.clear()

# Adicionar nodes do shader Phong
output = nodes.new(type='ShaderNodeOutputMaterial')
bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')

# Conectar nodes
links = material.node_tree.links
links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])

# Aplicar à esfera
bpy.context.object.data.materials.append(material)
```

### 3. Configuração Manual nos Nodes

1. **Abra o Shader Editor**
2. **Adicione estes nodes:**
   - **BSDF Principled** (mais moderno que o Phong puro)
   - **Mix Shader** para combinar efeitos
   - **Glossy BSDF** para o componente especular

### 4. Ajustando os Parâmetros Phong

No BSDF Principled:
- **Base Color**: Cor difusa
- **Subsurface**: 0.0 (para materiais não-subsurface)
- **Metallic**: Controla o quão "metálico" é o material
- **Specular**: Intensidade do componente especular (equivalente ao coeficiente especular de Phong)
- **Roughness**: Controla a nitidez do brilho (inverso do expoente de Phong)

### 5. Visualizando os Componentes Separadamente

Para entender melhor o modelo de Phong, crie três materiais:

**Material Ambiente:**
- Cor: Azul escuro
- Sem componentes difusa ou especular

**Material Difuso:**
- Specular: 0.0
- Roughness: 1.0

**Material Especular:**
- Base Color: Preto
- Specular: 1.0
- Roughness: 0.0

### 6. Dicas para Melhor Visualização

- Use **Viewport Shading → Rendered** para ver o resultado em tempo real
- Experimente com diferentes ângulos de luz
- Teste diferentes valores de Roughness (0.0 = brilho muito concentrado, 1.0 = brilho muito espalhado)
- Use o **Light Path** node para isolar componentes específicos

Este exemplo mostra como o modelo moderno do Blender (Principled BSDF) incorpora e expande os conceitos originais do modelo de Phong.