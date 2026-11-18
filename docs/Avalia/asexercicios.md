# Lista de Exercícios — Computação Gráfica

Esta lista revisa os conteúdos trabalhados nas ACs, AP1 e AP2. Cada assunto contém cinco questões: uma fácil, duas intermediárias e duas elaboradas.

## 1. Transformações

### Questão 1 — Transformações básicas de um objeto

**Nível:** Fácil

Abra o Blender e crie um cubo. Posicione-o em `(2, 0, 1)`, escale-o para `(1.5, 1, 0.5)` e rotacione-o em 45° no eixo Z.

**Entregue:** arquivo `.blend` e captura mostrando os valores de localização, rotação e escala.

### Questão 2 — Transformação de um polígono

**Nível:** Intermediário

Dado um triângulo com vértices `A(1, 1)`, `B(3, 1)` e `C(2, 4)`, calcule suas novas coordenadas após uma escala de `2` no eixo X, `0,5` no eixo Y e uma translação de `(-1, 2)`. Represente o triângulo original e o transformado no Blender ou em uma figura gerada.

**Entregue:** cálculos, coordenadas finais e imagem comparativa.

### Questão 3 — Transformações em espaço local e global

**Nível:** Intermediário

Crie um cubo filho de um objeto vazio. Aplique uma rotação ao objeto pai e, depois, uma translação ao cubo. Compare o resultado das transformações em espaço global e local.

**Entregue:** arquivo `.blend` e explicação da influência da hierarquia sobre as transformações.

### Questão 4 — Composição ordenada de transformações

**Nível:** Elaborado

Crie um retângulo com vértices `A(1, 1)`, `B(5, 1)`, `C(5, 3)` e `D(1, 3)`. Aplique:

1. translação de `(-2, 3)`;
2. escala de `1,5` em X e `0,5` em Y;
3. rotação de 90° no sentido anti-horário;
4. reflexão em relação ao eixo Y.

Calcule cada etapa separadamente e demonstre no Blender por meio de cópias da figura.

**Entregue:** cálculos, arquivo `.blend` e imagem com todas as etapas identificadas.

### Questão 5 — Automação de transformações com Python

**Nível:** Elaborado

Escreva um script Python para o Blender que crie cinco objetos formando uma composição. O script deve aplicar translação, rotação e escala aos objetos, utilizar `math.radians()` e converter coordenadas locais em uma disposição coerente.

**Entregue:** script `.py`, arquivo `.blend` gerado e explicação da ordem de aplicação das transformações.

---

## 2. Imagem

### Questão 1 — Resolução e proporção

**Nível:** Fácil

Calcule a quantidade de pixels das resoluções `640 × 480`, `1280 × 720` e `1920 × 1080`. Identifique a razão de aspecto de cada imagem.

**Entregue:** cálculos e explicação da diferença entre resolução e quantidade de pixels.

### Questão 2 — Imagem matricial e vetorial

**Nível:** Intermediário

Produza o mesmo símbolo em formato matricial e vetorial. Compare o resultado ao ampliar cada imagem em 400%.

**Entregue:** as duas imagens e um parágrafo comparando definição, pixels, curvas e casos de uso.

### Questão 3 — Manipulação de pixels

**Nível:** Intermediário

Utilizando Python, carregue uma imagem colorida, converta-a para escala de cinza e gere uma terceira versão reduzindo seu brilho em 30%.

**Entregue:** código, as três imagens e explicação da operação aplicada aos pixels.

### Questão 4 — Amostragem e quantização

**Nível:** Elaborado

Realize experimentos com diferentes resoluções espaciais e quantidades de cores em uma imagem fotográfica. Compare, por exemplo, versões com `256`, `128` e `64` pixels no maior lado e com paletas de `256`, `32` e `8` cores.

**Entregue:** tabela com tamanho dos arquivos, imagens comparativas e análise dos efeitos de redução de resolução e quantização.

### Questão 5 — Processamento e análise de imagem

**Nível:** Elaborado

Desenvolva um pequeno programa que receba uma imagem e produza: histograma dos canais RGB, versão em tons de cinza, filtro de detecção de bordas e relatório com resolução, profundidade estimada e formato.

**Entregue:** código, arquivos gerados e relatório interpretando os resultados.

---

## 3. Definições de Cor

### Questão 1 — Conversão RGB

**Nível:** Fácil

Explique os três canais do modelo RGB e converta as cores hexadecimal `#FF0000`, `#00FF00`, `#0000FF` e `#808080` para seus valores RGB de 0 a 255.

**Entregue:** tabela e breve explicação da mistura aditiva de luz.

### Questão 2 — Profundidade de cor

**Nível:** Intermediário

Compare imagens com profundidades de 1, 4, 8 e 24 bits por pixel. Calcule quantas cores cada configuração pode representar sem considerar transparência.

**Entregue:** tabela e exemplos visuais que demonstrem o surgimento de posterização.

### Questão 3 — RGB, HSV e HSL

**Nível:** Intermediário

Converta a cor RGB `(64, 128, 192)` para aproximações em HSV e HSL. Explique qual modelo é mais intuitivo para selecionar uma variação mais clara, mais saturada ou de outra matiz.

**Entregue:** cálculos, valores aproximados e exemplos de ajustes.

### Questão 4 — Harmonias cromáticas

**Nível:** Elaborado

Crie três paletas de cinco cores para um mesmo tema: uma análoga, uma complementar e uma triádica. Aplique as paletas a três versões da mesma cena simples no Blender.

**Entregue:** três renders, códigos das cores e justificativa para contraste, hierarquia visual e atmosfera.

### Questão 5 — Gerenciamento de cor em uma cena 3D

**Nível:** Elaborado

Monte uma cena com superfícies claras, médias e escuras e altere sua iluminação entre condições quentes, frias e neutras. Compare os mesmos materiais em pelo menos dois espaços ou configurações de transformação de cor disponíveis no Blender.

**Entregue:** arquivo `.blend`, renders comparativos e análise da influência do espaço de cor, exposição e iluminação sobre as cores percebidas.

---

## 4. Modelagem

### Questão 1 — Modelagem por primitivas

**Nível:** Fácil

Construa um objeto reconhecível usando apenas cubos, cilindros e esferas, sem modificar seus vértices. Aplique escala, rotação e localização de forma intencional.

**Entregue:** arquivo `.blend` e duas capturas em ângulos diferentes.

### Questão 2 — Mesa de estudos

**Nível:** Intermediário

Modele uma mesa de estudos com livro, luminária e um objeto autoral. Use pelo menos duas técnicas além da escala de primitivas, como extrusão, *inset*, *bevel*, curvas ou modificadores.

**Entregue:** arquivo `.blend`, render pela câmera e descrição das técnicas utilizadas.

### Questão 3 — Modelagem de um objeto orgânico

**Nível:** Intermediário

Modele uma fruta, folha ou objeto de superfície orgânica a partir de uma esfera ou outra primitiva. Utilize edição proporcional, subdivisão, deformações ou esculturas simples.

**Entregue:** arquivo `.blend`, visualizações sólida e com material, além de explicação das operações aplicadas.

### Questão 4 — Topologia e modificadores

**Nível:** Elaborado

Modele um objeto mecânico contendo orifícios, cantos arredondados e partes simétricas. Organize a topologia para evitar distorções ao usar Mirror, Bevel e Subdivision Surface.

**Entregue:** arquivo `.blend`, capturas em vista sólida e *wireframe*, além de comentário sobre faces não desejadas, polígonos irregulares e densidade da malha.

### Questão 5 — Cena-conceito autoral

**Nível:** Elaborado

Crie uma cena autoral em que a palavra “Ibmec” ou outro título escolhido seja o elemento principal. Inclua exatamente três objetos autorais, uma câmera principal e um storyboard de três momentos.

**Entregue:** arquivo `.blend`, quatro imagens, storyboard e relatório sobre conceito, composição, técnicas de modelagem e hierarquia dos objetos.

---

## 5. PBR

### Questão 1 — Parâmetros de um material

**Nível:** Fácil

Explique as funções de `Base Color`, `Roughness` e `Metallic` no `Principled BSDF`. Configure três esferas usando valores diferentes de rugosidade.

**Entregue:** captura do `Shader Editor`, render das três esferas e comentário sobre os reflexos.

### Questão 2 — Material metálico e dielétrico

**Nível:** Intermediário

Crie um material semelhante a aço e outro semelhante a cerâmica. Ajuste corretamente `Metallic` e `Roughness` e compare a resposta de ambos à mesma fonte de luz.

**Entregue:** arquivo `.blend`, render e justificativa dos parâmetros.

### Questão 3 — Material transparente

**Nível:** Intermediário

Modele um recipiente de vidro ou acrílico usando espessura física. Configure transmissão, IOR e rugosidade de modo que o material continue legível e transparente.

**Entregue:** arquivo `.blend`, render com fundo e captura dos parâmetros do material.

### Questão 4 — Biblioteca de materiais

**Nível:** Elaborado

Crie seis materiais coerentes com um mesmo ambiente: madeira, tecido, plástico, metal, cerâmica e vidro. Use nomes claros e apresente cada material na mesma geometria e iluminação.

**Entregue:** arquivo `.blend`, prancha comparativa e tabela com os principais parâmetros de cada material.

### Questão 5 — Materiais avançados e diagnóstico

**Nível:** Elaborado

Monte uma cena com materiais metálico, dielétrico, translúcido e emissivo. Produza três versões de iluminação e identifique qualquer resultado incoerente, como metal escurecido sem ambiente refletido, vidro opaco ou reflexos excessivos. Corrija o problema e documente as decisões.

**Entregue:** arquivo final, renders antes e depois, captura dos nós e relatório técnico.

---

## 6. Texturas

### Questão 1 — Aplicação de uma textura

**Nível:** Fácil

Aplique uma imagem como cor de um material em um plano e ajuste a escala para evitar repetição excessiva ou distorção.

**Entregue:** arquivo `.blend`, captura do `Shader Editor` e render.

### Questão 2 — Mapa UV de um cubo

**Nível:** Intermediário

Crie um mapa UV para um cubo e aplique uma textura numerada ou quadriculada. Reduza as distorções escolhendo uma projeção adequada e ajustando as ilhas UV.

**Entregue:** captura do `UV Editor`, captura do modelo renderizado e explicação da projeção usada.

### Questão 3 — Cor, rugosidade e normal

**Nível:** Intermediário

Monte um material com três mapas: `Base Color`, `Roughness` e `Normal`. Configure os mapas de dados como `Non-Color` e encaminhe a normal pelo nó `Normal Map`.

**Entregue:** captura completa do `Shader Editor`, render e identificação das entradas de cada mapa.

### Questão 4 — Corrigir distorções em um objeto complexo

**Nível:** Elaborado

Modele um objeto com faces curvas e planas, como uma garrafa, e prepare seu UV. Dê tratamento distinto às áreas relevantes para evitar esticamentos e variações inadequadas de escala.

**Entregue:** arquivo `.blend`, captura do UV, render texturizado e relatório descrevendo costuras e ajustes.

### Questão 5 — Pipeline completo de texturização

**Nível:** Elaborado

Texturize três objetos autorais usando, ao menos, duas texturas de imagem. Em um dos materiais, utilize mapa de cor, rugosidade e normal; no outro, use textura procedural ou um conjunto diferente. Os recursos devem permanecer disponíveis ao reabrir o arquivo.

**Entregue:** arquivo `.blend` com recursos empacotados ou caminhos relativos, render, capturas dos mapas UV e nós, além das fontes e licenças utilizadas.

---

## 7. Iluminação

### Questão 1 — Identificação de luzes

**Nível:** Fácil

Ilumine uma esfera usando, separadamente, uma luz Point, Sun, Spot e Area. Compare direção, queda e suavidade das sombras.

**Entregue:** quatro renders e uma tabela comparativa.

### Questão 2 — Luz principal e preenchimento

**Nível:** Intermediário

Configure duas luzes para revelar forma, material e separação entre um objeto e seu fundo. Ajuste a luz principal para produzir áreas iluminadas e sombras claras; use a luz de preenchimento para suavizar as regiões escuras sem eliminar todo o contraste.

**Entregue:** arquivo `.blend`, dois renders comparando a cena com uma e duas luzes.

### Questão 3 — Três pontos

**Nível:** Intermediário

Crie uma configuração de três pontos com luz principal, preenchimento e recorte. Varie a posição das luzes para destacar o volume de uma escultura simples.

**Entregue:** diagrama das luzes, arquivo `.blend` e render final.

### Questão 4 — Iluminação para materiais distintos

**Nível:** Elaborado

Ilumine três objetos com materiais metálico, dielétrico e transparente. As configurações devem tornar os três materiais reconhecíveis, evitando sombras excessivamente duras e reflexos sem forma.

**Entregue:** arquivo `.blend`, três renders de ângulos distintos e relatório sobre posição, intensidade, tamanho, cor e função de cada luz.

### Questão 5 — Iluminação cinematográfica de um interior

**Nível:** Elaborado

Ilumine uma cena interna utilizando pelo menos três funções luminosas, temperaturas de cor contrastantes e uma fonte motivada, como luminária, janela ou tela. Faça a luz orientar a atenção durante uma sequência de câmera.

**Entregue:** arquivo `.blend`, três renders, um clipe curto e explicação da atmosfera, contraste, sombras e escolhas de temperatura de cor.

---

## 8. Animação

### Questão 1 — Primeiro movimento

**Nível:** Fácil

Anime a posição de um cubo da esquerda para a direita em 48 frames, inserindo *keyframes* no início e no fim. Compare as visualizações linear e suavizada.

**Entregue:** arquivo `.blend` ou vídeo curto e captura dos dois *keyframes*.

### Questão 2 — Interpolação

**Nível:** Intermediário

Anime um objeto percorrendo três posições. Gere uma versão com interpolação linear e outra Bezier, sem alterar os *keyframes*.

**Entregue:** dois vídeos e captura do `Graph Editor` explicando as diferenças de velocidade.

### Questão 3 — Animação de câmera

**Nível:** Intermediário

Crie uma cena simples e anime a câmera combinando movimento de posição com um *pan* ou *tilt*. A trajetória deve manter o objeto principal dentro do enquadramento.

**Entregue:** arquivo `.blend`, vídeo de 5 segundos e captura da trajetória ou dos canais no `Graph Editor`.

### Questão 4 — Timing e narrativa

**Nível:** Elaborado

Produza uma animação de 8 segundos, a 24 fps, com início, desenvolvimento e encerramento. Anime a câmera e pelo menos dois objetos relacionados à ação. Utilize o `Graph Editor` para controlar aceleração, desaceleração e pausas.

**Entregue:** arquivo `.blend`, vídeo, storyboard de três momentos e captura das curvas de animação.

### Questão 5 — Peça audiovisual de 15 segundos

**Nível:** Elaborado

Desenvolva uma peça autoral de 360 frames a 24 fps. Inclua animação da câmera, de um título e de ao menos um objeto principal. O movimento deve preservar a legibilidade do título e seguir o planejamento de um storyboard.

**Entregue:** arquivo `.blend`, vídeo completo, storyboard atualizado e relatório sobre timing, interpolação, propriedades animadas e desafios.

---

## 9. Renderização

### Questão 1 — Configuração básica de render

**Nível:** Fácil

Renderize um objeto usando resolução `1280 × 720`, formato PNG e 50% de escala. Identifique motor, resolução, formato e destino da saída.

**Entregue:** arquivo `.blend` e imagem renderizada.

### Questão 2 — Eevee e Cycles

**Nível:** Intermediário

Renderize a mesma cena em Eevee e Cycles, mantendo câmera, materiais e iluminação. Compare tempo de execução, sombras, reflexos e aparência dos materiais.

**Entregue:** dois renders, configuração utilizada e tabela comparativa.

### Questão 3 — Amostragem e qualidade

**Nível:** Intermediário

Produza três renders da mesma cena alterando apenas a quantidade de amostras. Compare ruído, qualidade e tempo de renderização e proponha uma configuração equilibrada.

**Entregue:** três imagens, tempo de cada render e justificativa da configuração escolhida.

### Questão 4 — Teste e exportação de animação

**Nível:** Elaborado

Configure uma animação de 10 segundos a 24 fps e realize um teste curto antes do render completo. Exporte o resultado em `.mp4` H.264 e revise se o vídeo apresenta duração, taxa de quadros e enquadramento corretos.

**Entregue:** arquivo `.blend`, vídeo final, ao menos um quadro renderizado e relatório das configurações de saída.

### Questão 5 — Render final de projeto integrado

**Nível:** Elaborado

Finalize uma animação de 15 segundos contendo modelagem autoral, materiais PBR, texturas, iluminação e movimento de câmera. Os recursos externos devem estar empacotados ou usar caminhos relativos funcionais. Faça render de teste, render final e revisão integral do vídeo.

**Entregue:** arquivo `.blend`, vídeo de 15 segundos em H.264, dois renders de momentos diferentes e relatório sobre motor, amostragem, resolução, tempo, materiais, iluminação e correções realizadas.

---

## Critérios gerais

| Critério | O que será verificado |
|---|---|
| Correção técnica | Cálculos, configurações, cálculos de cor, objetos e arquivos funcionais |
| Clareza visual | Legibilidade, composição, hierarquia e qualidade das imagens |
| Fundamentação | Explicação coerente das escolhas e dos conceitos aplicados |
| Organização | Arquivos, objetos, coleções, materiais, texturas e luzes identificáveis |
| Documentação | Registro dos parâmetros, fontes, licenças, dificuldades e soluções |
