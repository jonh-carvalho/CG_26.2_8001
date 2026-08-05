# Relatório AC04 - Preparação de Cena 3D no Blender

## 1. Transformações Aplicadas — Model

Na cena criada no Blender, os objetos principais foram modelados a partir de formas geométricas simples, como plano, cubo e cilindro. Para montar a mesa de estudo, foram aplicadas transformações de **escala**, **rotação** e **translação**.

A mesa foi criada a partir de um plano e recebeu escala nos eixos X e Y para formar uma superfície maior. O livro foi criado a partir de um cubo, sendo achatado no eixo Z, posicionado sobre a mesa e levemente rotacionado no eixo Z. O copo foi criado com um cilindro, escalado para ficar mais alto e fino, e depois posicionado ao lado do livro. O lápis também foi criado com um cilindro, sendo alongado, reduzido em espessura, rotacionado para ficar deitado e colocado sobre o livro.

As transformações aproximadas utilizadas foram:

| Objeto | Translação | Rotação | Escala |
|---|---|---|---|
| Mesa | X: 0, Y: 0, Z: 0 | X: 0°, Y: 0°, Z: 0° | X: 5, Y: 2.5, Z: 1 |
| Livro | X: -1.2, Y: 0.3, Z: 0.08 | X: 0°, Y: 0°, Z: 8° | X: 1.4, Y: 0.9, Z: 0.08 |
| Copo | X: 1.3, Y: 0.6, Z: 0.9 | X: 0°, Y: 0°, Z: 0° | X: 0.35, Y: 0.35, Z: 0.9 |
| Lápis | X: -1.2, Y: 0.3, Z: 0.25 | X: 0°, Y: 90°, Z: 30° | X: 0.08, Y: 0.08, Z: 1.3 |

Essas operações compõem a **matriz Model** de cada objeto. A matriz Model é responsável por transformar as coordenadas locais do objeto para o espaço do mundo, definindo sua posição, orientação e tamanho dentro da cena 3D.

---

## 2. Configuração da Câmera — View

A câmera principal da cena foi renomeada como `Camera_Principal` e posicionada em uma vista levemente superior da mesa. O objetivo foi criar um enquadramento que mostrasse claramente os objetos principais da cena: mesa, livro, copo e lápis.

A configuração aproximada da câmera foi:

```text
Location: X = 0, Y = -7, Z = 5
Rotation: X = 60°, Y = 0°, Z = 0°
Lens: 35 mm
```

Essa posição permite visualizar a mesa de cima e de frente, mantendo a composição organizada e facilitando a percepção espacial dos objetos.

A **matriz View** representa a transformação do espaço do mundo para o espaço da câmera. Em outras palavras, ela define como a cena será vista a partir da posição e orientação da câmera. Enquanto a matriz Model posiciona cada objeto no mundo, a matriz View define o ponto de vista usado para observar esses objetos.

---

## 3. Comparação entre Projeções — Projection

Foram geradas duas versões da mesma cena: uma usando **projeção perspectiva** e outra usando **projeção ortográfica**.

Na **projeção perspectiva**, os objetos mais próximos da câmera parecem maiores, enquanto os objetos mais distantes parecem menores. Isso cria uma sensação mais natural de profundidade, parecida com a forma como enxergamos o mundo real.

Na **projeção ortográfica**, os objetos mantêm o mesmo tamanho aparente independentemente da distância em relação à câmera. Por isso, a cena fica com aparência mais plana e técnica, sem o efeito visual de profundidade da perspectiva.

| Projeção | Característica | Resultado |
|---|---|---|
| Perspectiva | Objetos distantes parecem menores | Maior sensação de profundidade |
| Ortográfica | Objetos mantêm o mesmo tamanho aparente | Visual mais plano e técnico |

A **matriz Projection** é responsável por converter a cena vista pela câmera em uma imagem 2D. Quando a câmera está em perspectiva, essa matriz aplica o efeito de profundidade. Quando a câmera está em modo ortográfico, ela preserva os tamanhos aparentes dos objetos.

---

## 4. Composição MVP

A composição **MVP** representa a sequência:

```text
Model → View → Projection
```

Para explicar essa sequência, foi escolhido o objeto **Livro**.

Inicialmente, o livro existe em seu próprio sistema de coordenadas locais, como um cubo criado no Blender. Nesse momento, ele ainda não possui a aparência nem a posição final desejada.

Em seguida, a **matriz Model** aplica as transformações de escala, rotação e translação. Com isso, o cubo é achatado para parecer um livro, rotacionado levemente no eixo Z e posicionado sobre a mesa no espaço do mundo.

Depois, a **matriz View** transforma a cena de acordo com o ponto de vista da `Camera_Principal`. Isso significa que o livro passa a ser interpretado em relação à posição e à orientação da câmera.

Por fim, a **matriz Projection** converte essa visualização 3D em uma imagem 2D, usando projeção perspectiva ou ortográfica.

A sequência conceitual pode ser representada assim:

```text
Coordenadas locais do livro
        ↓
Matriz Model
        ↓
Livro no espaço do mundo
        ↓
Matriz View
        ↓
Livro no espaço da câmera
        ↓
Matriz Projection
        ↓
Imagem final renderizada
```

Assim, a pipeline MVP mostra como um objeto 3D passa do seu espaço local até a imagem final renderizada.
