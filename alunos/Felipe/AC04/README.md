# AC04 — Preparação de Cena 3D (Projeção, Câmeras e Matrizes)

## Aluno
Felipe Ultramar

## Disciplina
Computação Gráfica

## Ferramenta Utilizada
Blender 4.5 LTS

---

# 1. Introdução

O objetivo desta atividade foi preparar uma cena 3D básica utilizando o Blender 4.5 LTS, aplicando conceitos fundamentais de computação gráfica relacionados a transformações geométricas, posicionamento de câmera e projeções geométricas.

A atividade serviu como preparação para a próxima etapa do projeto, focada em iluminação e animação. Foram utilizados os conceitos de sistema de coordenadas, matrizes Model, View e Projection (MVP), além da organização da cena utilizando coleções.

---

# 2. Organização Inicial da Cena

Inicialmente, a cena padrão do Blender foi organizada através da criação de coleções no Outliner para separar os elementos do projeto.

As coleções criadas foram:

- Mesa_e_Objetos
- Camera
- Luzes

Os objetos também foram renomeados corretamente para facilitar a organização e identificação durante o desenvolvimento da cena.

## Objetos utilizados

- Mesa
- Livro
- Copo
- Lapis
- Camera

---

# 3. Modelagem Básica da Cena

A cena foi construída utilizando primitivas geométricas simples do Blender.

## Mesa

A mesa foi criada utilizando um Plane e escalada nos eixos X e Y para formar uma superfície retangular semelhante a uma mesa de estudos.

### Transformações principais

- Escala no eixo X
- Escala no eixo Y

---

## Livro

O livro foi criado a partir de um Cube, que recebeu escala reduzida no eixo Z para ficar achatado.

Também foi reposicionado sobre a mesa.

### Valores finais do Livro

#### Location

- X = -1
- Y = 0.5
- Z = 0.12

#### Rotation

- X = 0°
- Y = 0°
- Z = 0°

#### Scale

- X = 1.400
- Y = 0.900
- Z = 0.100

---

## Copo

O copo foi criado utilizando um Cylinder, ajustando a escala para deixá-lo mais alto e fino.

### Valores finais do Copo

#### Location

- X = 1.12
- Y = 0
- Z = 0.5

#### Rotation

- X = 0°
- Y = 0°
- Z = 0°

#### Scale

- X = 0.350
- Y = 0.350
- Z = 0.525

---

## Lápis

O lápis também foi criado com um Cylinder, porém utilizando escala reduzida e alongamento no eixo Z.

Depois disso, foram aplicadas rotações para posicioná-lo diagonalmente sobre o livro.

### Valores finais do Lápis

#### Location

- X = 0
- Y = 0
- Z = 0.25

#### Rotation

- X = -35°
- Y = 90°
- Z = 0°

#### Scale

- X = 0.120
- Y = 0.120
- Z = 0.264

---

# 4. Transformações Geométricas e Matriz Model

Cada objeto da cena recebeu transformações geométricas compostas por:

- Translação
- Rotação
- Escala

Essas transformações representam a matriz Model de cada objeto.

A matriz Model é responsável por converter as coordenadas locais do objeto para coordenadas no espaço do mundo. Dessa forma, cada objeto pode ser posicionado corretamente na cena 3D.

No livro, por exemplo, foi aplicada uma redução de escala no eixo Z para criar o formato achatado. O lápis recebeu rotações para ficar deitado diagonalmente sobre o livro. O copo recebeu escalas para adquirir um formato mais estreito e alto.

---

# 5. Configuração da Câmera e Matriz View

A câmera da cena foi renomeada para `Camera_Principal` e posicionada em uma visão superior inclinada da mesa.

O enquadramento foi ajustado para permitir a visualização dos principais objetos da cena, mantendo espaço livre para futuras expansões na próxima atividade.

## Configurações da câmera

### Location

- X = 0.017
- Y = -8.606
- Z = 5.169

### Rotation

- X = 60°
- Y = 0°
- Z = 0°

### Lens

- 40 mm

A matriz View representa a transformação das coordenadas do mundo para o sistema de referência da câmera. Isso significa que todos os objetos da cena passam a ser visualizados a partir da posição e orientação da câmera.

---

# 6. Projeção Geométrica e Matriz Projection

Foram produzidas duas versões da cena:

- Projeção Perspectiva
- Projeção Ortográfica

---

## Projeção Perspectiva

Na projeção perspectiva, objetos mais distantes aparentam ser menores, criando maior sensação de profundidade e realismo.

Essa projeção é mais próxima da forma como o olho humano percebe o ambiente.

---

## Projeção Ortográfica

Na projeção ortográfica, não existe redução de tamanho causada pela distância.

Os objetos mantêm proporções constantes independentemente da profundidade da cena.

Essa projeção é muito utilizada em projetos técnicos e engenharia.

---

## Matriz Projection

A matriz Projection é responsável por transformar a visualização da câmera em um espaço de projeção adequado para a renderização final da imagem.

Dependendo do tipo de projeção escolhido, a matriz pode produzir:

- efeito de perspectiva;
- ou projeção ortográfica sem profundidade visual.

---

# 7. Composição MVP (Model → View → Projection)

Utilizando o objeto Livro como exemplo, o fluxo conceitual da pipeline MVP ocorre da seguinte forma:

Inicialmente, o objeto possui coordenadas locais próprias.

A matriz Model aplica escala, rotação e translação ao objeto, posicionando-o corretamente sobre a mesa no espaço do mundo.

Em seguida, a matriz View transforma as coordenadas do mundo para o sistema de referência da câmera.

Por fim, a matriz Projection converte essas informações para o espaço de projeção, gerando a imagem final renderizada na tela.

---

# 8. Conclusão

A atividade permitiu compreender os fundamentos geométricos envolvidos na construção de uma cena 3D no Blender.

Foram aplicados conceitos importantes de transformações geométricas, posicionamento de câmera e projeções, além da compreensão conceitual da pipeline MVP utilizada em computação gráfica.

A cena criada servirá como base para futuras atividades envolvendo iluminação, materiais e animação.
