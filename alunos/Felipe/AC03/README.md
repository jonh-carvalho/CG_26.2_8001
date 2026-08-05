## Descrição da Atividade

Na atividade, foi desenvolvida uma cena no Blender chamada **"Parque Geométrico"**, composta por objetos 2D e 3D.

Nos objetos 2D (plano XY), foram aplicadas transformações de **translação**, **rotação no eixo Z** e **escala**, permitindo movimentação e alteração de tamanho dentro do plano.

Nos objetos 3D, foram utilizadas transformações de **translação**, **rotação em múltiplos eixos (X, Y e Z)** e **escala não uniforme**, explorando o comportamento dos sólidos no espaço tridimensional.

Parte da construção da cena foi realizada manualmente utilizando a interface do Blender, com as ferramentas **G (move)**, **R (rotate)** e **S (scale)**.

Além disso, foi desenvolvido um **script em Python**, responsável por criar objetos automaticamente e aplicar transformações como posição, rotação e escala, utilizando a função `math.radians()` para conversão de ângulos.

Também foi criada uma **animação simples**, utilizando keyframes no frame inicial e final para um objeto 2D e um objeto 3D.

## Questões Teóricas

### 1. Explique a diferença entre translação, rotação e escala em computação gráfica.

Translação é o deslocamento de um objeto de uma posição para outra no espaço. Rotação é o giro do objeto em torno de um eixo. Escala é a alteração do tamanho do objeto, podendo ser uniforme ou diferente em cada eixo.

---

### 2. Qual é a diferença entre transformar um objeto no espaço local e no espaço global?

No espaço global, as transformações são aplicadas com base nos eixos fixos da cena (X, Y e Z do mundo). No espaço local, as transformações são aplicadas em relação à orientação do próprio objeto, que pode estar rotacionado.

---

### 3. Em uma cena 3D, por que rotações em eixos diferentes podem gerar resultados visuais distintos?

Porque cada eixo representa uma direção diferente no espaço tridimensional. Rotacionar em X, Y ou Z altera a orientação do objeto de formas distintas, resultando em movimentos visuais diferentes.

---

### 4. No Blender, por que usar `math.radians()` ao definir `rotation_euler` por script?

Porque o Blender trabalha com valores em radianos para rotações. A função `math.radians()` é utilizada para converter valores em graus para radianos, facilitando a definição das rotações no código.

---

### 5. Dê um exemplo prático de quando vale mais a pena usar Python em vez de transformar manualmente pela interface.

O uso de Python é mais eficiente quando é necessário criar vários objetos ou aplicar transformações repetitivas. Por exemplo, ao gerar múltiplos objetos com posições e rotações específicas, o script automatiza o processo e reduz o tempo de trabalho.
