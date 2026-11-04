---
marp: true
theme: gaia
---

## **Fundamentos de Animação Digital**

- Compreender os princípios básicos da animação digital
- Familiarizar-se com a interface do Blender
- Criar uma animação simples aplicando conceitos de computação gráfica

--- 

### **O que é animação?**

- **Definição:** Uma sequência de imagens estáticas exibidas rapidamente para criar ilusão de movimento
- **História breve**: [Moderna](../files/pixar.pdf)
- **Tipos de animação:**
    - Animação tradicional vs. digital 
    <iframe width="280" height="157" src="https://www.youtube-nocookie.com/embed/z7_15wEHIA4?si=ZoEt5SmIK9nK6Bl1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    - Aplicações na computação: jogos, simulações, interfaces

---

### **Princípios básicos da animação**

#### Keyframes (quadros-chave)
    
> Animação keyframe é uma técnica que define "quadros-chave" ou momentos específicos de uma animação, onde o software preenche automaticamente os quadros intermediários para criar uma transição suave entre eles. Keyframes são usados para controlar a mudança de propriedades de um elemento ao longo do tempo, como sua posição, escala, rotação ou cor. Esta técnica é amplamente utilizada em softwares de edição de vídeo, motion design e no desenvolvimento web (CSS) para criar animações. 

---

#### Interpolação

> A interpolação em animação é o processo automático que preenche os quadros intermediários entre duas poses-chave, criando transições suaves entre elas. Isso permite que a animação pareça fluida e natural, animando propriedades como posição, rotação, escala e efeitos de cor em objetos como gráficos, textos e clipes. Existem diferentes tipos de interpolação, como a linear (velocidade constante) e a Bezier (com controle manual da velocidade), que podem ser ajustadas para obter efeitos específicos. 

---

#### Timeline 
    
> A "timeline de animação" refere-se à linha do tempo visual em softwares de animação para organizar eventos e quadros, ou à propriedade CSS que vincula a animação a um evento de rolagem. Em softwares como o Blender, a timeline é uma barra onde você insere "keyframes" para registrar a posição, rotação ou escala de objetos em quadros específicos, criando assim a animação ao reproduzir os movimentos entre eles.

---    

#### Curvas de animação
    
> Curvas de animação são representações gráficas que mostram como um valor, como posição, rotação ou escala, muda ao longo do tempo para criar movimento suave e realista. Elas são usadas em softwares de animação e design para controlar a "interpolação" entre quadros-chave, permitindo suavizar acelerações e desacelerações de maneira visual e controlável, com opções como interpolação linear, suave ou baseada em curvas de Bézier. 

---

#### Conceitos de FPS (frames por segundo)

> Em animação, FPS é a sigla para Frames Per Second, ou Quadros por Segundo em português. Refere-se à taxa de quadros na qual uma sequência de imagens estáticas é exibida para criar a ilusão de movimento contínuo

---

## **Interface do Blender**

#### **Apresentação da interface**

- Viewport 3D
- Timeline
- Graph Editor
- Properties Panel

---

#### **Primeiros passos**

- Navegação na cena 3D
- Manipulação de objetos básicos
- Sistema de coordenadas e transformações

---

#### **Hands-on - Animação Simples**

##### **Exercício 1: Bola Quicando**

Conceitos computacionais aplicados:

- Sistema de coordenadas
- Interpolação linear
- Física simplificada

---

##### **Passo a passo:**

1. Criar uma esfera (Add → Mesh → UV Sphere)
2. Posicionar no topo da cena (eixo Z)
3. Definir primeiro keyframe (I → Location)
4. Mover para frame 24, posicionar bola no chão
5. Definir segundo keyframe
6. Ajustar curva de animação no Graph Editor
7. Repetir para criar ciclo de quique

---

##### **Exercício 2: Rotação de Objeto**

1. Criar cubo
2. Animar rotação em 360 graus
3. Demonstrar diferentes modos de interpolação


---

### 3. Aprofundar Animação e Jogos

- Rigging e animação de personagens
- Animação com constraints físicas
- Scripting com Python no Blender
- Exportação para engines de jogo

