### Modelagem

#### Introdução

- Apresentar a interface do Blender focada no workspace de modelagem.
- Explicar conceitos básicos: objeto 3D, malha, vértices, arestas e faces.

#### Passo 1: Configuração Inicial
- Criar um novo projeto e configurar a cena básica.
- Introdução às primitivas geométricas básicas (cubo, esfera, cilindro).

#### Passo 2: Edição Básica de Geometria

- Introduzir o modo de edição (Edit Mode).
- Exercício: Selecionar vértices, arestas e faces.
- Ferramentas básicas: mover, escalar, rotacionar.
  
#### Passo 3: Transformações e Modificadores

- Mostrar extrusão, subdivisão e loop cuts para adicionar detalhes.
- Aplicar modificadores simples (Mirror, Subdivision Surface).

#### Passo 4: Exercício Prático: Modelando uma Ponte Simples

- Criar o perfil base da ponte usando primitivas e extrusão.
- Modelar o corpo principal com controle de largura e altura.
- Adicionar elementos como grades e buracos usando ferramentas de corte.

#### Passo 5: Refinamentos e Detalhes

- Trabalhar com suavização (Shade Smooth).
- Ajustar iluminação simples para visualizar a modelagem.

#### Passo 6: Exportar e Renderizar

- Breve introdução ao render básico da cena.
- Exportar o modelo para formatos comuns (objeto .obj, .fbx).



### Passo 4: Exercício Prático — Comandos e Atalhos

#### 1. Criar perfil base da ponte com primitivas e extrusão
- Adicionar cubo: `Shift + A` > Mesh > Cube
- Escalar cubo (ajustar largura, altura e comprimento):
  - Escalar eixo X: Selecionar cubo, `S` + `X`
  - Escalar eixo Y: `S` + `Y`
  - Escalar eixo Z: `S` + `Z`
- Entrar no modo de edição: `Tab`
- Selecionar face para extrusão: `3` para modo Face, clique direito na face
- Extrusar face para estender: `E`, mover mouse para extrudar, clique esquerdo para confirmar
- Adicionar cortes para controle da forma: `Ctrl + R`, mover o mouse para posicionar o loop cut, clique esquerdo para confirmar, clique esquerdo novamente para fixar posição

#### 2. Modelar corpo principal com controle de largura e altura
- Selecionar vértices, arestas ou faces:
  - Vértice: tecla `1`
  - Aresta: tecla `2`
  - Face: tecla `3`
- Mover seleção: `G` (pressionar X, Y ou Z para restringir eixo)
- Usar ferramenta Mirror (modificador espelho):
  - No painel de propriedades (ícone de chave inglesa) clicar em Add Modifier > Mirror
  - Espelhamento padrão no eixo X
- Usar loop cut para criar segmentos:
  - `Ctrl + R` para adicionar loop cuts
- Ajustar vertices para formar pilares e tabuleiro

#### 3. Adicionar grades e buracos com ferramentas de corte
- Selecionar faces onde criar buracos
- Ativar Knife Tool para cortes personalizados: tecla `K`, clique para iniciar cortes, clique para criar vértices de corte, pressione `Enter` para finalizar
- Apagar faces para criar buracos: selecionar faces > `X` > Faces
- Criar grades com primitivas:
  - Adicionar plano: `Shift + A` > Mesh > Plane (ou cubo muito fino)
  - Escalar e posicionar grades: `S` + eixos, `G` + eixos
- Duplicar elementos para formar grades laterais:
  - Selecionar componente da grade > `Shift + D` para duplicar > mover para posição
- Usar extrude para barras:
  - Selecionar face ou aresta > `E` > mover para extrudar barra

***

Esse detalhamento com comandos e atalhos cobre as etapas práticas para modelar uma ponte simples no Blender, facilitando o aprendizado prático e rápido.

Se desejar, posso fornecer um guia com imagens ilustrativas passo a passo ou links de vídeo para referência visual. Quer?

[1](https://www.youtube.com/watch?v=GIFAJiVPM9U)
[2](https://pt.scribd.com/document/557185667/lista-atalho-Blender)
[3](https://docs.blender.org/manual/pt/dev/advanced/keymap_editing.html)
[4](https://www.tonka3d.com.br/blog/principais-teclas-de-atalhos-do-blender/)
[5](https://nafergo.github.io/manual-livre-blender/principais_atalhos.html)
[6](https://www.reddit.com/r/blender/comments/1ja7yqb/blender_shortcuts_that_changed_my_life_drop_yours/)
[7](https://docs.blender.org/manual/pt/2.92/interface/keymap/blender_default.html)
[8](https://translate.google.com/translate?u=https%3A%2F%2Fstyly.cc%2Ftips%2Fblender-modeling-usefulshortcut%2F&hl=pt&sl=en&tl=pt&client=srp)
[9](https://www.youtube.com/watch?v=KAeVe9XW5eY)
[10](https://www.reddit.com/r/blender/comments/1m07dm5/bridge_edge_loops_shortcut_doesnt_exist/)