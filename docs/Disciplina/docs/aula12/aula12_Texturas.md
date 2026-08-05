# Texturas em Computação Gráfica: Guia Introdutório com Blender

## 1. O que são Texturas?

**Texturas** são imagens 2D aplicadas sobre superfícies 3D para dar realismo e detalhes aos objetos. Elas simulam características como cor, rugosidade, reflexão e relevo.

### Tipos Básicos de Texturas:

- **Diffuse/Albedo**: Cor base do material
- **Normal**: Simula detalhes de relevo
- **Specular**: Controla reflexões
- **Roughness**: Define a rugosidade
- **Displacement**: Cria geometria real

## 2. Configuração Básica no Blender

### Exercício 1: Primeira Textura

```python
# Passos no Blender:
1. Adicione um cubo (Shift + A → Mesh → Cube)
2. No Shader Editor, crie um novo material
3. Adicione um node "Image Texture"
4. Carregue uma imagem
5. Conecte ao node "Principled BSDF"
```

## 3. Tipos de Texturas e Aplicações Práticas

### 3.1 Textura Diffuse
**Função**: Define a cor base do objeto

**Exercício 2**: Criando um Material de Tijolos
```python
1. Baixe uma textura de tijolos
2. Aplique ao node Diffuse
3. Ajuste o mapping (Scale: 2.0, 2.0, 2.0)
4. Renderize e observe
```

### 3.2 Textura Normal
**Função**: Simula detalhes de relevo sem alterar a geometria

**Exercício 3**: Adicionando Relevo a uma Parede
```python
1. Adicione um node Normal Map
2. Conecte entre Image Texture e Normal input
3. Use uma textura normal de concreto
4. Ajuste a força (Strength: 2.0)
```

### 3.3 Textura Roughness
**Função**: Controla como a luz se espalha na superfície

**Exercício 4**: Criando Metal Desgastado
```python
1. Texture Diffuse: metal base
2. Texture Roughness: preto e branco (preto = liso, branco = áspero)
3. Texture Normal: arranhões e imperfeições
```

## 4. Node Setup Completo

### Exemplo: Material Realista de Madeira

```
[Wood Diffuse Texture] → [Color] → [Principled BSDF] → [Surface]
[Wood Normal Texture] → [Normal Map] → [Normal] → [Principled BSDF]
[Wood Roughness Texture] → [Roughness] → [Principled BSDF]
[Mapping Node] → [All Textures]
[Texture Coordinate] → [Mapping Node]
```

## 5. Exercícios Práticos

### Exercício 5: Planeta Terra
```python
Objetivo: Criar um planeta realista

Materiais necessários:
- Textura diffuse do planeta
- Textura de nuvens (com transparência)
- Textura de emissão para cidades noturnas

Setup:
1. Esfera como base
2. Duas materials: superfície e nuvens
3. Usar Transparency para nuvens
4. Animação de rotação
```

### Exercício 6: Material de Sci-Fi
```python
Objetivo: Criar material futurista

Características:
- Padrões emissivos
- Superfície metálica
- Detalhes em relevo
- Efeitos de energia

Técnicas:
- UV Mapping para controle preciso
- Nodes de emissão
- Texturas procedural
```

### Exercício 7: Personagem Stylized
```python
Objetivo: Texturizar personagem cartoon

Passos:
1. UV Unwrapping do modelo
2. Pintura base no Texture Paint mode
3. Adicionar sombras e highlights
4. Textura normal para detalhes
```

## 6. Técnicas Avançadas

### 6.1 UV Mapping
```python
# Exercício: Mapeando uma Garrafa
1. Selecione a garrafa
2. Entrar em Edit Mode (Tab)
3. Selecionar bordas para marca como seams
4. Unwrap (U → Unwrap)
5. Ajustar no UV Editor
```

### 6.2 Procedural Textures
```python
# Exercício: Criando Mármore Procedural
Nodes:
[Noise Texture] → [ColorRamp] → [Diffuse]
[Wave Texture] → [MixRGB] → [Normal]
```

### 6.3 PBR Materials
```python
# Exercício: Material PBR Completo
Texturas:
- Albedo (cor)
- Normal (relevo)
- Roughness (rugosidade)
- Metallic (metalicidade)
- AO (oclusão ambiental)
```

## 7. Dicas Importantes

### Otimização:
- Use texturas em resoluções apropriadas
- Compacte UV maps eficientemente
- Reuse materiais quando possível

### Qualidade:
- Sempre use texturas em alta resolução para close-ups
- Combine texturas painted e procedural
- Teste em diferentes condições de iluminação

## 8. Projeto Final: Cena Completa

**Objetivo**: Criar uma cena com múltiplos materiais texturizados

**Elementos obrigatórios**:
- 1 objeto orgânico (planta, personagem)
- 1 objeto inorgânico (vaso, construção)
- 1 material procedural
- 1 material PBR completo
- Iluminação adequada

## 9. Recursos para Praticar

### Texturas Gratuitas:
- Poly Haven
- Texture Haven
- CC0 Textures

### Tutoriais Recomendados:
- "Blender Beginner Texture Tutorial"
- "PBR Texturing Guide"
- "UV Unwrapping Masterclass"

## 10. Solução de Problemas Comuns

### Problema: Textura distorcida
**Solução**: Revisar UV mapping e ajustar seams

### Problema: Baixa resolução
**Solução**: Usar texturas higher-res ou UDIMs

### Problema: Performance ruim
**Solução**: Otimizar resolução e usar texture baking
