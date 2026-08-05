# **AS - Avaliação Suplementar**

## **Prazo de Entrega: Segunda - 01/12/2025**

**Envio pelo GitHub no mesmo repositório das ACs, AP1 e AP2**

**Entrega e Documentação**

- Arquivo `.blend` da cena completa
- Pelo menos 2 renders finais (diferentes ângulos e momentos da animação)
- Um **Vídeo da animação** renderizado (formato .mp4 ou .avi, mínimo 5 segundos / 120 frames a 24fps)
- Breve documento (PDF ou MD) explicando:
    - O conceito e tema da cena interna criada
    - As escolhas de materiais e propriedades PBR aplicadas
    - O sistema de iluminação implementado (tipos de luzes e posicionamento)
    - A trajetória e conceito da animação de câmera
    - Desafios encontrados e soluções aplicadas
    - Referências visuais utilizadas

---

## **Objetivo**

Criar uma cena interna (interior) cinematográfica que demonstre domínio avançado de iluminação, materiais PBR e animação de câmera. A cena deve destacar objetos com diferentes propriedades materiais através de um sistema de iluminação profissional e movimento de câmera que valorize a composição e narrativa visual.

## **Introdução**

Nas avaliações anteriores, você desenvolveu habilidades em modelagem, materiais, texturas e iluminação básica. Na **AS**, você focará em técnicas avançadas de iluminação de interiores, criação de materiais realistas diversos e cinematografia através de movimento de câmera:

### **Iluminação de Interiores**

A iluminação de ambientes internos requer técnicas específicas para criar atmosfera e realismo. Você trabalhará com:

- **Three-Point Lighting**: Sistema clássico de iluminação (key, fill, rim/back light)
- **Luzes de Área**: Para iluminação suave e natural de ambientes
- **Luzes Pontuais e Spot**: Para destacar objetos específicos e criar drama
- **Iluminação Ambiente**: HDRI ou luz ambiente para preencher sombras
- **Temperatura de Cor**: Uso de luzes quentes e frias para criar atmosfera
- **Sombras e Contraste**: Controle de sombras para criar profundidade e drama

### **Materiais PBR Avançados**

Materiais diversos e realistas são essenciais para criar cenas convincentes. Você trabalhará com:

- **Materiais Dielétricos**: Plástico, madeira, tecido, cerâmica (Metallic = 0)
- **Materiais Metálicos**: Metal, aço, cobre, ouro (Metallic = 1)
- **Materiais Transparentes**: Vidro, água, acrílico (Transmission)
- **Propriedades PBR**: Roughness, Specular, IOR, Subsurface Scattering
- **Texturas e Mapas**: Difuso, normal, roughness, metallic, emissivo
- **Materiais Emissivos**: Objetos que emitem luz (lâmpadas, telas, etc.)

### **Animação de Câmera Cinematográfica**

O movimento de câmera é fundamental para contar histórias visuais. Você trabalhará com:

- **Tipos de Movimento**: Dolly (movimento linear), Pan (rotação), Tilt (inclinação), Tracking (seguimento)
- **Curvas de Animação**: Uso do Graph Editor para movimentos suaves e naturais
- **Composição em Movimento**: Manter regras de composição durante o movimento
- **Profundidade de Campo**: Foco seletivo para guiar a atenção
- **Velocidade e Ritmo**: Controlar a velocidade do movimento para criar atmosfera

---

## **Descrição da Avaliação:**

Você criará uma **cena interna completa** (interior) que demonstre diferentes materiais através de um sistema de iluminação profissional e movimento de câmera cinematográfico.

### **Cenário**

A cena interna deve incluir:

1. **Ambiente Interno**:
   - Um espaço fechado (sala, cozinha, escritório, estúdio, loja, etc.)
   - Paredes, piso e teto (ou elementos que definam o espaço)
   - Decoração e objetos que compõem o ambiente
   - Atmosfera e tema claramente definidos

2. **Objetos com Destaque Material**:
   - **Pelo menos 3 objetos principais** que serão destacados na cena
   - Cada objeto deve ter um **material diferente e distinto**:
     - Exemplo 1: Objeto metálico (ouro, prata, cobre, aço)
     - Exemplo 2: Objeto dielétrico (madeira, plástico, cerâmica, tecido)
     - Exemplo 3: Objeto transparente/translúcido (vidro, cristal, acrílico)
   - Os objetos devem ser posicionados estrategicamente para serem valorizados pela iluminação e câmera
   - Materiais devem demonstrar propriedades PBR realistas (roughness, metallic, specular, etc.)

3. **Sistema de Iluminação**:
   - **Mínimo de 3 luzes diferentes** (pode ter mais)
   - Tipos de luzes variados (Sun, Area, Point, Spot)
   - Sistema deve criar atmosfera e destacar os objetos principais
   - Uso adequado de temperatura de cor (luzes quentes/frias)
   - Sombras bem configuradas para criar profundidade
   - Opcional: HDRI para iluminação ambiente adicional

4. **Animação de Câmera**:
   - Câmera deve se mover durante toda a animação (mínimo 10 segundos)
   - Movimento deve ser suave e cinematográfico
   - A trajetória deve revelar o ambiente e destacar os objetos principais
   - Uso de diferentes tipos de movimento (dolly, pan, tracking, etc.)
   - Composição deve ser mantida durante o movimento
   - Opcional: Depth of Field para foco seletivo

### **Temas Sugeridos**

- **Estúdio de Fotografia**: Objetos iluminados profissionalmente
- **Sala de Estar Moderna**: Diferentes materiais em mobiliário e decoração
- **Cozinha Contemporânea**: Metais, madeira e vidro
- **Escritório Minimalista**: Materiais diversos em ambiente clean
- **Loja de Joias**: Destaque para materiais preciosos e vidro
- **Galeria de Arte**: Iluminação focada em objetos expostos
- **Laboratório**: Materiais diversos em ambiente técnico

**Importante**: O tema é livre, desde que seja uma cena interna e atenda aos requisitos técnicos.

### **Requisitos Técnicos**

- **Ambiente**:
  - Cena completamente interna (interior)
  - Espaço claramente definido (paredes, limites visíveis)
  - Decoração e objetos que compõem o ambiente

- **Materiais**:
  - **Mínimo 3 objetos principais** com materiais diferentes e distintos
  - Cada material deve demonstrar propriedades PBR adequadas:
    - Metallic: 0 (dielétrico) ou 1 (metálico)
    - Roughness: valores apropriados ao material
    - Specular: ajustado conforme necessário
    - Transmission: para materiais transparentes (se aplicável)
  - Pelo menos 1 material com textura (difuso, normal, ou roughness map)
  - Materiais devem ser visualmente distintos e realistas

- **Iluminação**:
  - **Mínimo 3 luzes diferentes** (tipos variados)
  - Sistema deve criar atmosfera adequada ao tema
  - Uso de diferentes temperaturas de cor
  - Sombras configuradas adequadamente
  - Iluminação deve destacar os objetos principais

- **Animação de Câmera**:
  - Animação mínima de 10 segundos (240 frames a 24fps)
  - Câmera deve se mover durante toda a animação
  - Movimento suave (usar Graph Editor)
  - Trajetória deve revelar o ambiente e objetos
  - Pelo menos 2 tipos diferentes de movimento (ex: dolly + pan)

- **Renderização**:
  - Utilizar Cycles ou Eevee como engine
  - Resolução mínima: 1920x1080 (Full HD)
  - Renderizar vídeo final (.mp4 ou .avi)
  - Duração mínima: 10 segundos (240 frames a 24fps)
  - Opcional: Compositing para ajustes finais (color grading, bloom, etc.)

---

## **Recursos e Referências**

### **Iluminação de Interiores**

- [Interior Lighting in Blender](https://www.youtube.com/results?search_query=blender+interior+lighting+tutorial)
- [Three-Point Lighting Setup](https://www.youtube.com/results?search_query=blender+three+point+lighting)
- [HDRI Lighting Tutorial](https://www.youtube.com/results?search_query=blender+hdri+lighting)
- [Cinematic Lighting Techniques](https://www.youtube.com/results?search_query=blender+cinematic+lighting)
- [Color Temperature in Blender](https://www.youtube.com/results?search_query=blender+color+temperature)

### **Materiais PBR Avançados**

- [PBR Material Guide](https://www.youtube.com/results?search_query=blender+pbr+material+guide)
- [Creating Realistic Materials](https://www.youtube.com/results?search_query=blender+realistic+materials)
- [Metal Materials Tutorial](https://www.youtube.com/results?search_query=blender+metal+material)
- [Glass Material Tutorial](https://www.youtube.com/results?search_query=blender+glass+material)
- [Wood Material Tutorial](https://www.youtube.com/results?search_query=blender+wood+material)
- Introdução a Materiais: `docs/Disciplina/docs/aula12/03_Materiais.md`

### **Animação de Câmera**

- [Camera Animation in Blender](https://www.youtube.com/results?search_query=blender+camera+animation)
- [Cinematic Camera Movement](https://www.youtube.com/results?search_query=blender+cinematic+camera)
- [Camera Tracking Tutorial](https://www.youtube.com/results?search_query=blender+camera+tracking)
- [Depth of Field Tutorial](https://www.youtube.com/results?search_query=blender+depth+of+field)
- [Graph Editor for Camera](https://www.youtube.com/results?search_query=blender+graph+editor+camera)

### **Composição e Cinematografia**

- [Composition Rules in 3D](https://www.youtube.com/results?search_query=3d+composition+rules)
- [Rule of Thirds in Blender](https://www.youtube.com/results?search_query=blender+rule+of+thirds)
- [Cinematography Basics](https://www.youtube.com/results?search_query=cinematography+basics)
- [Camera Framing Techniques](https://www.youtube.com/results?search_query=camera+framing+techniques)

### **Texturas e Assets**

- [Poly Haven](https://polyhaven.com/) - HDRI e texturas PBR gratuitas
- [Texture Haven](https://texturehaven.com/) - Texturas gratuitas
- [CC0 Textures](https://cc0textures.com/) - Texturas CC0
- [Blender Kit](https://www.blenderkit.com/) - Modelos e materiais prontos

### **Tutoriais Complementares**

- [Complete Interior Scene Tutorial](https://www.youtube.com/results?search_query=blender+interior+scene+tutorial)
- [Professional Material Workflow](https://www.youtube.com/results?search_query=blender+professional+material+workflow)
- [Advanced Lighting Techniques](https://www.youtube.com/results?search_query=blender+advanced+lighting)
- [Camera Animation Masterclass](https://www.youtube.com/results?search_query=blender+camera+animation+masterclass)

---

## **Critérios de Correção**

### **Ambiente e Composição**

- **Cena Interna**: Ambiente claramente definido como interior
- **Composição**: Enquadramento e disposição de elementos bem planejados
- **Decoração**: Objetos e elementos que compõem o ambiente de forma coerente
- **Tema e Atmosfera**: Tema claro e atmosfera adequada

### **Materiais**

- **Diversidade**: Pelo menos 3 objetos com materiais distintos e bem diferenciados
- **Propriedades PBR**: Uso correto de parâmetros (Metallic, Roughness, Specular, etc.)
- **Realismo**: Materiais convincentes e realistas
- **Texturas**: Aplicação adequada de texturas quando necessário
- **Destaque**: Objetos são claramente destacados na cena

### **Iluminação**

- **Sistema Completo**: Mínimo 3 luzes diferentes bem implementadas
- **Atmosfera**: Iluminação cria atmosfera adequada ao tema
- **Destaque de Objetos**: Luzes destacam adequadamente os objetos principais
- **Temperatura de Cor**: Uso adequado de luzes quentes e frias
- **Sombras**: Sombras bem configuradas criam profundidade
- **Qualidade Técnica**: Intensidade, ângulo e tipo de luzes adequados

### **Animação de Câmera**

- **Movimento Contínuo**: Câmera se move durante toda a animação
- **Suavidade**: Movimento fluido e natural (uso adequado do Graph Editor)
- **Trajetória**: Movimento revela ambiente e objetos de forma interessante
- **Tipos de Movimento**: Pelo menos 2 tipos diferentes de movimento
- **Composição**: Regras de composição mantidas durante o movimento
- **Narrativa Visual**: Movimento contribui para contar a história da cena

### **Renderização e Qualidade**

- **Resolução**: Renderização em 50% do Full HD (1920x1080)
- **Qualidade Visual**: Renderização com aspecto profissional
- **Duração**: Mínimo 5 segundos de animação
- **Formato**: Vídeo renderizado corretamente (.mp4 ou .avi)

### **Entrega e Documentação**

- Arquivo `.blend` da cena completa e funcional
- Pelo menos 2 renders finais (diferentes ângulos/momentos)
- **Vídeo da animação** renderizado (formato .mkv, .mp4 ou .avi, mínimo 5 segundos)
- Documentação clara explicando:
  - Conceito e tema da cena
  - Escolhas de materiais e propriedades PBR
  - Sistema de iluminação implementado
  - Trajetória e conceito da animação de câmera
  - Desafios e soluções
  - Referências utilizadas

## **Dicas para o Desenvolvimento**

1. **Planeje a cena primeiro**: Faça um esboço ou referência visual do ambiente desejado
2. **Comece pela estrutura**: Modele ou importe a estrutura básica do ambiente (paredes, piso, teto)
3. **Posicione os objetos principais**: Coloque os 3 objetos de destaque em posições estratégicas
4. **Iluminação em camadas**: Adicione luzes uma de cada vez, testando cada adição
5. **Use referências reais**: Observe fotos de interiores reais para entender iluminação natural
6. **Teste materiais isoladamente**: Crie materiais em esferas de teste antes de aplicar nos objetos
7. **Anime a câmera progressivamente**: Comece com movimento simples, adicione complexidade depois
8. **Use o Graph Editor**: Sempre suavize curvas de animação para movimentos naturais
9. **Renderize testes frequentes**: Faça renders de teste em baixa resolução para ajustar rapidamente
10. **Mantenha foco**: A câmera deve guiar o olhar para os objetos principais
11. **Atenção às sombras**: Sombras bem configuradas fazem enorme diferença no realismo
12. **Temperatura de cor**: Misture luzes quentes (laranja/amarelo) e frias (azul) para criar atmosfera
13. **Profundidade de campo**: Use Depth of Field para criar foco seletivo e guiar atenção
14. **Organize a cena**: Mantenha objetos, materiais e luzes organizados e nomeados

## **Exemplos de Combinações de Materiais**

- **Ouro + Madeira + Vidro**: Objeto dourado, móvel de madeira, vaso de vidro
- **Aço + Tecido + Cerâmica**: Estrutura metálica, almofadas, vaso de cerâmica
- **Cobre + Mármore + Acrílico**: Objeto de cobre, superfície de mármore, objeto de acrílico
- **Prata + Couro + Cristal**: Objeto prateado, móvel de couro, objeto de cristal

**Lembre-se**: Os materiais devem ser visualmente distintos e demonstrar propriedades PBR adequadas. A iluminação e câmera devem valorizar cada material de forma clara.

