# **AP2**
## **Prazo de Entrega: 19/12/2025**

## Objetivo 

Evoluir a cena desenvolvida na AP1, aplicando modelos de iluminação, texturas, materiais e animação para criar um ambiente visualmente realista, dinâmico e interativo.

## **Introdução**

Na **AP1**, você desenvolveu uma cena básica no Blender contendo dois terrenos separados por um lago, com uma ponte conectando-os e objetos que utilizam essa ponte. Agora, na **AP2**, vamos aprimorar essa cena aplicando conceitos fundamentais de renderização realista:

### **Modelos de Iluminação**

A iluminação é essencial para criar profundidade e realismo em cenas 3D. Nesta avaliação, você trabalhará com dois modelos principais:

- **Phong Shading**: Modelo clássico que simula reflexão especular, difusa e ambiente. É importante entender este modelo fundamental antes de partir para técnicas mais avançadas.

- **PBR (Physically Based Rendering) com Principled BSDF**: Modelo moderno que simula o comportamento físico real da luz ao interagir com diferentes materiais. O shader Principled BSDF do Blender combina múltiplas propriedades físicas em um único nó, permitindo criar materiais realistas com base em princípios físicos.

### **Texturas e Materiais**

Texturas e materiais transformam objetos simples em elementos convincentes. Você utilizará:

- Aplicar texturas UV em diferentes objetos da cena
- Combinar mapas de textura (difuso, normal, roughness, metallic)
- Criar materiais procedurais
- Ajustar propriedades físicas dos materiais (metalicidade, rugosidade, subsurface scattering)

### **Animação e Jogos**

A animação dá vida à cena, transformando elementos estáticos em uma experiência dinâmica e interativa. Nesta avaliação, você aplicará conceitos de:

- **Animação por Keyframes**: Definir pontos-chave de movimento ao longo do tempo
- **Transformações Animadas**: Animar posição, rotação e escala de objetos
- **Timeline e Interpolação**: Controlar a velocidade e suavidade dos movimentos

#### Se a opção for jogo.

- **Interatividade Básica**: Criar elementos que simulam comportamento de jogos (câmera em primeira pessoa, objetos que se movem em loop, etc.) 
- **Física Simples:** Aplicar física básica para simular gravidade e colisões


---

## **Descrição da Avaliação:**
 
Você criará pelo menos uma sequência animada que dê vida à sua cena, como um personagem/objeto atravessando a ponte, água com movimento, ou uma câmera cinemática que percorre a cena.

## Cenário

Partindo da cena desenvolvida na AP1, você deverá:

1. **Aprimorar a Iluminação da Cena**:

   - Configurar um sistema de iluminação que valorize os elementos da cena
   - Aplicar diferentes tipos de luzes (sol, point lights, área lights)
   - Ajustar a temperatura de cor e intensidade para criar atmosfera

2. **Aplicar Materiais com Phong e PBR**:

   - **Ponte**: Aplicar textura de madeira ou pedra com propriedades PBR realistas
   - **Terrenos**: Criar materiais para relva, terra ou pedras
   - **Água do Lago**: Implementar material realista de água com reflexão, refração e transparência
   - **Objetos Importados**: Aplicar materiais adequados a cada objeto da cena

3. **Trabalhar com Texturas**:
   
   - Aplicar texturas UV em pelo menos 3 objetos diferentes
   - Utilizar mapas de normal, roughness e/ou metallic para adicionar detalhes
   - Criar pelo menos um material (usando nodes)


4. **Implementar Animação**:

   - Criar pelo menos uma animação usando keyframes (mínimo 5 segundos / 120 frames a 24fps)
   - Animar/Controlar pelo menos um objeto atravessando a ponte ou interagindo com a cena
   - Animar a câmera para criar um tour cinemático pela cena
   - Opcional: Adicionar movimento à água do lago usando shaders animados ou simulação

## Requisitos Técnicos

- Utilizar o Cycles ou Eevee como engine de renderização
- Aplicar pelo menos 5 materiais diferentes com propriedades distintas
- Incluir pelo menos um material com textura de normal map
- Demonstrar compreensão dos parâmetros do Principled BSDF (Metallic, Roughness, Specular, etc.)
- Criar uma animação de no mínimo 5 segundos (120  frames a 24fps)
- Utilizar pelo menos 3 propriedades animadas (location, rotation, scale, etc.)
- Renderizar a animação final em formato de vídeo (.mp4 ou .avi) ou sequência de imagens

## Recursos e Referências

### Modelos de Iluminação
- Aula 12 - Modelos de Iluminação: `docs/Disciplina/aula12/aula12_ModeloIluminação.md.md`
- Comparação entre modelos: `docs/Disciplina/aula12/02_Comparação.md`

### Texturas e Materiais
- Aula 12 - Texturas: `docs/Disciplina/aula12/aula12_Texturas.md`
- Materiais: `docs/Disciplina/aula12/03_Materiais.md`
- UV Wrapping: `docs/Disciplina/aula12/04_UVWraping.md`
- Tutorial criando material tijolo: `docs/Disciplina/aula12/criandomaterialtijolo.md`

### Sites para Texturas
- [Poly Haven](https://polyhaven.com/) - Texturas PBR gratuitas
- [Texture Haven](https://texturehaven.com/)
- [CC0 Textures](https://cc0textures.com/)
- [Blender Kit](https://www.blenderkit.com/) - Materiais prontos

### Tutoriais Complementares
- [Blender - Principled BSDF Explained](https://www.youtube.com/results?search_query=blender+principled+bsdf+tutorial)
- [Water Material in Blender](https://www.youtube.com/results?search_query=realistic+water+blender)
- [PBR Texturing Workflow](https://www.youtube.com/results?search_query=blender+pbr+texturing)

### Animação e Jogos
- Introdução à Animação: `docs/Disciplina/docs/files/animação.md`
- [Blender Animation Basics](https://www.youtube.com/results?search_query=blender+animation+tutorial+beginner)
- [Keyframe Animation in Blender](https://www.youtube.com/results?search_query=blender+keyframe+animation)
- [Camera Animation Tutorial](https://www.youtube.com/results?search_query=blender+camera+animation)

## Critérios de Correção

### Iluminação (25 pontos)
- **Sistema de iluminação adequado**: Uso correto de diferentes tipos de luzes (10 pts)
- **Atmosfera e composição**: Iluminação cria atmosfera e destaca elementos importantes (10 pts)
- **Configurações técnicas**: Intensidade, temperatura de cor e sombras bem ajustadas (5 pts)

### Materiais e Shaders (25 pontos)
- **Aplicação do Principled BSDF**: Uso correto dos parâmetros (Metallic, Roughness, etc.) (15 pts)
- **Diversidade de materiais**: Pelo menos 5 materiais diferentes com propriedades distintas (10 pts)
- **Material de água**: Água com reflexão, refração e transparência realistas (10 pts)

### Texturas (25 pontos)
- **UV Unwrapping**: Mapeamento UV correto e sem distorções (8 pts)
- **Aplicação de texturas**: Texturas bem aplicadas em pelo menos 3 objetos (10 pts)
- **Mapas adicionais**: Uso de normal maps, roughness maps ou outros (7 pts)

### Animação (25 pontos)
- **Implementação de keyframes**: Uso correto de keyframes e timeline (8 pts)
- **Qualidade da animação**: Movimento suave e natural, sem saltos bruscos (7 pts)
- **Criatividade**: Animação criativa que adiciona narrativa à cena (5 pts)


### Entrega e Documentação
- Arquivo `.blend` da cena completa
- Pelo menos 2 renders finais  (diferentes ângulos)
- **Vídeo da animação** renderizado (formato .mp4 ou .avi, mínimo 3 segundos)
- Breve documento (PDF ou MD) explicando:
  - As escolhas de materiais e texturas
  - O conceito da animação criada
  - Desafios encontrados e soluções aplicadas

## Dicas para o Desenvolvimento

1. **Comece pela iluminação**: Uma boa iluminação pode fazer materiais simples parecerem incríveis
2. **Não exagere**: Materiais realistas geralmente têm valores sutis, não extremos
3. **Use referências**: Observe fotos reais para entender como materiais se comportam com luz
4. **Teste renderizações**: Faça renders de teste frequentemente para ajustar os materiais
5. **Organize seus nodes**: Um node editor organizado facilita ajustes e correções
6. **Aproveite materiais procedurais**: Para terrenos e elementos naturais, materiais procedurais podem ser mais eficientes
7. **Planeje a animação**: Faça um storyboard simples antes de começar a animar
8. **Use o Graph Editor**: Ajuste as curvas de interpolação para movimentos mais naturais
9. **Teste a animação**: Reproduza frequentemente para verificar se o movimento está fluido
10. **Renderize em baixa qualidade primeiro**: Teste a animação em baixa resolução antes do render final



