## **Modelos de Iluminação no Blender**

#### **Objetivo do Roteiro**

Compreender e aplicar progressivamente diferentes modelos de iluminação, do mais simples ao mais complexo.

---

#### **FASE 1: CONFIGURAÇÃO INICIAL** 

##### 1.1 Preparação da Cena

```
- Nova cena (Ctrl + N)
- Adicionar: Esfera, Cubo, Plano como base
- Luz solar básica (Sun light)
- Câmera em posição favorável
```

##### 1.2 Interface Essencial
```
- Shader Editor (abrir nova janela)
- Viewport Shading → Rendered
- Properties → Material Properties
```

---

#### **FASE 2: MODELOS BÁSICOS** (45 minutos)

##### 2.1 **Modelo Lambert** (15 min)
##### Teoria:

No Blender, um material "Lambert Sphere" se refere a um objeto esférico com um
shader (sombreador) Lambertiano, que simula superfícies foscas com reflexão difusa ideal. Esse tipo de material não possui brilho ou reflexos especulares intensos, e sua aparência muda suavemente conforme a luz incide em diferentes ângulos. 
Em vez de um único nó chamado "Lambert", a reflexão difusa em motores de renderização modernos como o Cycles e o Eevee é controlada pelo nó Principled BSDF ou pelo nó Diffuse BSDF
```
- Apenas componente difusa
- Superfícies perfeitamente mate
- I = k_d * (N·L)
```

##### Prática no Blender:

```
# Configuração Lambert
1. Novo material "Lambert_Sphere"
2. BSDF Principled → Roughness = 1.0
3. Specular = 0.0
4. Cor: Azul médio
```

##### Método com o nó Principled BSDF 
A maneira mais moderna e simples de obter um material com características Lambertianas é usando o nó Principled BSDF, que é o material padrão em Blender:

```
- Adicione uma esfera na sua cena: Adicionar > Malha > UV Sphere.
- Suavize a malha para ter um visual mais suave: - Com a esfera selecionada, clique com o botão direito e escolha Shade Smooth.
- Crie um novo material: Vá para a área de trabalho Shading ou acesse o Editor de Shader e clique em Novo para criar um material.
```

```
Ajuste o material:

- No nó Principled BSDF, defina a propriedade Roughness (rugosidade) para um valor de 1.0. Isso remove qualquer brilho especular, garantindo uma reflexão puramente difusa (Lambertiana).
- Mude a Base Color (cor base) para a cor desejada.
- Configure a iluminação: Adicione uma fonte de luz, como um Sun (Sol), para iluminar a esfera e visualizar o efeito
```

##### Método com o nó Diffuse BSDF:
```

Para um controle mais básico, você pode usar diretamente o nó Diffuse BSDF: 

- Siga os passos 1 e 2 acima para criar e suavizar a esfera.
- Crie um novo material no Editor de Shader.
- Delete o nó Principled BSDF padrão.
- Adicione o nó Diffuse BSDF: Pressione Shift + A > Shader > Diffuse BSDF.

Conecte e ajuste:

- Ligue a saída BSDF do nó Diffuse BSDF na entrada Surface do nó Material Output.
- Defina a Color desejada no nó Diffuse BSDF. O valor padrão de Roughness 0.0 já proporciona a reflexão Lambertiana padrão.
- Configure a iluminação, como no método anterior
```

##### Exercício:
- Compare esfera Lambert vs esfera padrão
- Observe ausência de brilho

---

#### 2.2 **Modelo Phong** (15 min)
##### Teoria:

```
- Componentes: Ambiente + Difusa + Especular
- Brilho concentrado
- I = k_a + k_d*(N·L) + k_s*(R·V)^n
```

##### Prática no Blender:

```
1. Novo material "Phong_Sphere"
2. BSDF Principled → Roughness = 0.2
3. Specular = 0.5
4. Cor: Vermelho
```

##### Exercício:

- Ajuste Roughness (0.0 → 1.0)
- Observe mudança no brilho

#### 2.3 **Modelo Blinn-Phong** (15 min)
##### Teoria:

- Melhoria do Phong (half-vector)
- Mais eficiente computacionalmente
- Menos artefatos em ângulos rasos

##### Prática no Blender:

```
- O Blender usa Blinn-Phong internamente no Principled
1. Material "BlinnPhong_Sphere"
2. Roughness = 0.1
3. Specular = 0.8
4. Cor: Verde
```

##### Exercício:

- Compare Phong vs Blinn-Phong visualmente
- Gire a luz para ver diferenças

---

#### **FASE 3: MODELOS AVANÇADOS** (1 hora)

#### 3.1 **Introdução ao PBR** (30 min)
##### Teoria Physically Based Rendering:

```
- Baseado em propriedades físicas
- Conservação de energia
- Dois parâmetros principais: Metalness e Roughness
```

##### Prática no Blender - Materiais Dielétricos:

```
- Plástico Branco
1. Base Color: Branco (hex FFFFFF)
2. Roughness: 0.4
3. Specular: 0.5
4. Metallic: 0.0
```

##### Prática no Blender - Materiais Metálicos:
```
- Ouro
1. Base Color: Amarelo escuro (hex FFDD00)
2. Roughness: 0.2
3. Specular: 1.0
4. Metallic: 1.0
```

##### Exercício:
- Crie 4 esferas: plástico, metal, vidro, madeira
- Compare com diferentes ângulos de luz

#### 3.2 **Materiais Especiais** (30 min)

##### Vidro (Refração):
```
1. Base Color: Branco
2. Roughness: 0.0
3. Transmission: 1.0
4. IOR: 1.45 (valor padrão vidro)
```

##### Materiais Emissivos:
```
1. Base Color: Ciano
2. Emission: Cor branca
3. Emission Strength: 5.0
```

##### Exercício:
- Crie uma cena com vidro refratando luz
- Adicione objeto emissivo como fonte de luz

---

#### **FASE 4: TÉCNICAS COMPLEMENTARES** (30 minutos)

##### 4.1 **Iluminação HDRI** (15 min)
```
# Configuração HDRI
1. World Properties → Surface → Color
2. Escolher "Environment Texture"
3. Carregar HDRI (baixar gratuitamente do Poly Haven)
4. Strength: 1.0
```

##### 4.2 **Three-Point Lighting** (15 min)
```
- Iluminação profissional
1. Key Light: Principal (Sun, intensity 3)
2. Fill Light: Preenchimento (Point, intensity 1)
3. Back Light: Contorno (Spot, intensity 2)
```

---

#### **PROJETO FINAL: GALERIA DE MATERIAIS** (30 minutos)

##### Crie uma cena com 6 esferas demonstrando:

| **Esfera** | **Configuração** | **Modelo** |
|------------|------------------|------------|
| 1 | Roughness=1.0, Specular=0.0 | Lambert |
| 2 | Roughness=0.3, Specular=0.5 | Phong |
| 3 | Metallic=0.0, Roughness=0.1 | Blinn-Phong |
| 4 | Metallic=1.0, Roughness=0.2 | PBR Metal |
| 5 | Transmission=1.0, Roughness=0.0 | Refração |
| 6 | Emission Strength=10.0 | Emissivo |

##### Configurações da Cena:
- Plano como superfície
- HDRI para iluminação ambiente
- Three-point lighting adicional
- Render final (F12)

---

#### **RECURSOS ADICIONAIS**

##### Atalhos do Blender Essenciais:

```
Z → Menu Viewport Shading
Shift + Z → Alternar Rendered View
F12 → Render
M → Atribuir material
```

##### Nodes para Próximos Passos:

- **Mix Shader**: Combinar materiais
- **Fresnel**: Efeito de borda brilhante
- **Noise Texture**: Adicionar rugosidade
- **Bump/Normal Map**: Detalhes de superfície

##### Prática Recomendada:
1. **Dia 1**: Fases 1-2 (modelos básicos)
2. **Dia 2**: Fase 3 (PBR e materiais especiais)
3. **Dia 3**: Fase 4 + Projeto Final

