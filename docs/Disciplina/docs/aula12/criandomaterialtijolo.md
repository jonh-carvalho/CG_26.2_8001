# Exercício 2: Criando um Material de Tijolos - Passo a Passo Detalhado

## Passo 1: Baixar uma Textura de Tijolos

### Opção 1: Sites de Texturas Gratuitas
1. **Acesse um site de texturas:**
   - [Textures.com](https://www.textures.com)
   - [CC0 Textures](https://cc0textures.com)
   - [Poly Haven](https://polyhaven.com)

2. **Busque por texturas de tijolos:**
   - Digite "bricks" ou "tijolos" na barra de pesquisa
   - Escolha uma textura de sua preferência
   - Procure por versões "Diffuse" ou "Albedo"

3. **Faça o download:**
   - Selecione uma resolução adequada (1024x1024 ou 2048x2048)
   - Baixe o arquivo em formato PNG ou JPG
   - Salve em uma pasta de fácil acesso

### Opção 2: Criar sua Própria Textura
```python
# Exemplo usando Python com Pillow (opcional)
from PIL import Image, ImageDraw
import random

# Criar uma textura básica de tijolos
width, height = 512, 512
img = Image.new('RGB', (width, height), color='red')
draw = ImageDraw.Draw(img)

# Desenhar padrão de tijolos
for y in range(0, height, 64):
    for x in range(0, width, 128):
        offset = 0 if (y // 64) % 2 == 0 else 64
        draw.rectangle([x+offset, y, x+offset+120, y+60], fill='brown', outline='black')

img.save('brick_texture.png')
```

## Passo 2: Aplicar ao Node Diffuse no Blender

### Configuração Básica do Material:
1. **Abra o Blender e crie um novo projeto**
2. **Selecione o objeto padrão (Cube) ou crie um novo:**
   - `Shift + A` → Mesh → Cube (ou Plane)

3. **Abra o Shader Editor:**
   - Mude o workspace para "Shading"
   - Ou pression `N` para abrir o painel lateral

4. **Crie e configure os nodes:**
```python
# Estrutura básica do material (visualmente no Shader Editor)
# [Texture Coordinate] → [Mapping] → [Image Texture] → [Diffuse BSDF] → [Material Output]
```

### Passos Visuais no Shader Editor:
1. **Delete o node Principled BSDF padrão** (Delete ou X)
2. **Adicione os nodes necessários:**
   - `Shift + A` → Texture → Image Texture
   - `Shift + A` → Vector → Mapping
   - `Shift + A` → Shader → Diffuse BSDF
   - `Shift + A` → Input → Texture Coordinate

3. **Conecte os nodes na seguinte ordem:**
```
Texture Coordinate [UV] → Mapping [Vector] → Image Texture [Vector]
Image Texture [Color] → Diffuse BSDF [Color]
Diffuse BSDF [BSDF] → Material Output [Surface]
```

4. **Carregue a textura:**
   - No node "Image Texture", clique em "Open"
   - Navegue até onde salvou a textura de tijolos
   - Selecione o arquivo e clique em "Open Image"

## Passo 3: Ajustar o Mapping (Scale: 2.0, 2.0, 2.0)

### Configuração do Node Mapping:
1. **Selecione o node Mapping** no Shader Editor
2. **No painel de propriedades do node Mapping:**
   - Localize a seção "Scale"
   - Altere os valores X, Y, Z para 2.0
   - Ou digite `2.0` em cada campo

### Ajustes Adicionais Recomendados:
```python
# Valores sugeridos para melhor visualização:
Mapping Node:
- Scale: (2.0, 2.0, 2.0)
- Rotation: (0.0, 0.0, 0.0)  # Mantenha padrão
- Location: (0.0, 0.0, 0.0)  # Mantenha padrão

Image Texture Node:
- Color Space: sRGB
- Extension: Repeat
- Interpolation: Smart ou Linear
```

### Alternativa via Python Script (Opcional):
```python
import bpy

# Acessar o material ativo
mat = bpy.context.object.active_material
nodes = mat.node_tree.nodes

# Encontrar o node Mapping
mapping_node = None
for node in nodes:
    if node.type == 'MAPPING':
        mapping_node = node
        break

# Ajustar escala
if mapping_node:
    mapping_node.inputs['Scale'].default_value = (2.0, 2.0, 2.0)
```

## Passo 4: Renderizar e Observar

### Preparação para Render:
1. **Ajuste a iluminação da cena:**
   - `Shift + A` → Light → Sun ou Area Light
   - Posicione a luz para iluminar bem o objeto

2. **Ajuste a câmera:**
   - Selecione a câmera e posicione para ter boa visão do objeto
   - Pressione `0` no teclado numérico para visão da câmera

3. **Configure as configurações de render:**
   - No painel de propriedades, clique no ícone da câmera
   - Render Engine: Eevee (mais rápido) ou Cycles (mais realista)
   - Resolution: 1920x1080 ou menor para teste rápido

### Executar a Renderização:
1. **Visualização rápida:**
   - Pressione `Z` e selecione "Rendered" para visualização em tempo real

2. **Renderização final:**
   - Pressione `F12` ou clique em Render → Render Image

3. **Observações importantes:**
   - Verifique se os tijolos estão com escala adequada
   - Observe a repetição do padrão (não deve ter seams visíveis)
   - Confirme que as cores estão realistas

### Salvando o Resultado:
1. **Após a renderização:**
   - Na janela de render, clique em "Image" → "Save As"
   - Escolha formato (PNG recomendado)
   - Salve em local desejado

## Dicas Extras para Melhor Resultado:

### Otimização do Material:
```python
# Adicione estes nodes para melhor qualidade:
- [Bump Node] entre Image Texture e Diffuse BSDF para adicionar relevo
- [RGB Curves] para ajustar contraste e cores
- [ColorRamp] para controle mais preciso das cores
```

### Configuração de UV:
1. **Se o objeto for complexo:**
   - Edite Mode → Selecionar todas as faces → U → Unwrap
   - Ajuste manualmente se necessário

### Troubleshooting Comum:
- **Textura não aparece:** Verifique o caminho do arquivo
- **Escala errada:** Ajuste valores no node Mapping
- **Cores escuras:** Aumente a iluminação da cena
- **Padrão distorcido:** Verifique o UV Mapping do objeto

