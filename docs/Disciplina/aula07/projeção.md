# Câmeras e Matrizes de Transformação em Computação Gráfica

## Objetivos

- Compreender o papel da câmera virtual em ambientes 3D.
- Entender e implementar as matrizes Model, View e Projection.
- Relacionar esses conceitos com a renderização de objetos 3D.
- Explorar interatividade com movimentação de câmera e manipulação de cena.

## Conteúdo Programático

### Introdução à Câmera Virtual

- O que é uma câmera em computação gráfica?

Uma câmera em computação gráfica é uma abstração matemática que define o ponto de vista a partir do qual a cena 3D será projetada para a tela 2D. Ela determina o que será visível, o enquadramento e a perspectiva da cena, simulando o funcionamento de uma câmera fotográfica ou de vídeo no mundo real.

- Diferença entre câmera real e virtual.

Uma câmera real é um dispositivo físico que captura a luz refletida pelos objetos do mundo, formando imagens em sensores ou filmes. Já a câmera virtual, em computação gráfica, é uma construção matemática usada para definir o ponto de vista e a projeção da cena 3D para o plano 2D da tela. Enquanto a câmera real depende de propriedades ópticas e físicas, a câmera virtual é controlada por parâmetros matemáticos, como posição, direção e campo de visão, permitindo flexibilidade total na manipulação da visualização da cena.

- **Parâmetros principais da câmera virtual:**

    - **Posição:** define onde a câmera está localizada no espaço 3D.
    - **Direção (ou alvo):** indica para onde a câmera está apontando.
    - **Vetor up:** determina a orientação "para cima" da câmera, controlando a inclinação da imagem.

Esses parâmetros são essenciais para construir a matriz de visualização (View), que transforma as coordenadas da cena do sistema de mundo para o sistema de câmera.

### O que é Matriz Model?

A Matriz Model é uma matriz de transformação 4x4 que define a posição, orientação e escala de um objeto individual dentro do espaço de mundo da cena 3D. Ela é aplicada aos vértices de um objeto para transformá-los de suas coordenadas locais (ou de objeto) para as coordenadas de mundo. Em outras palavras, a Matriz Model "coloca" o objeto na cena.

- **Transformações:**
    - **Translação:** move o objeto para uma nova posição.
    - **Rotação:** gira o objeto em torno de um eixo.
    - **Escala:** altera o tamanho do objeto.

- Exemplos de transformações: translação, rotação, escala.
- Implementação prática usando bibliotecas como GLM.

###  Matriz View

- Definição: responsável por posicionar e orientar a câmera.
- Conceito de “lookAt” (posição da câmera, alvo, vetor up).
- Efeito da matriz View na visualização da cena.

### Matriz Projection

- Diferença entre projeção ortográfica e perspectiva.
- Parâmetros da projeção perspectiva: fovy, aspect, near, far.
- Como a matriz Projection afeta a percepção de profundidade.

### Pipeline Gráfico e Shaders

- Breve revisão do pipeline programável.
- Como as matrizes são enviadas para a GPU (uniforms).
- Vertex e Fragment Shaders: papel das matrizes no cálculo da posição dos vértices.

### Exemplo Prático

- Renderização de dois cubos com movimentação de câmera.
- Uso das teclas WASD para movimentação e mouse para orientação.
- Alteração de cores das faces dos cubos.

### Atividade Proposta

- Modificar o código para incluir outros objetos 3D (esfera, pirâmide).
- Explorar diferentes parâmetros de projeção e observar os efeitos.

### Recursos Didáticos

- Slides explicativos sobre cada matriz.
- Notebooks interativos (exemplo: Aula6.Ex1 - Câmeras - Matrizes Model, View, e Projection.ipynb).
- Códigos-fonte comentados.
- Demonstrações ao vivo.

### Avaliação

Exercício prático de implementação e modificação da cena.
Discussão em grupo sobre aplicações dos conceitos em jogos, simulações e visualização científica.

### Atividade Extra: Explorando Matrizes no Blender

Proponha aos alunos a criação de uma cena simples no Blender, utilizando cubos, esferas e pirâmides. Oriente-os a:

- Manipular a posição, rotação e escala dos objetos usando as ferramentas de transformação do Blender.
- Alterar a posição e orientação da câmera para observar como a visualização da cena muda.
- Comparar o funcionamento das matrizes Model, View e Projection no Blender com o que foi estudado em código.
- Exportar imagens ou vídeos mostrando diferentes enquadramentos e perspectivas.

Essa atividade permite relacionar conceitos matemáticos com ferramentas gráficas profissionais, reforçando o entendimento prático das matrizes de transformação.


### Exemplo com Python e Blender 4.5

A seguir, um exemplo simples de como manipular objetos e a câmera usando Python no Blender 4.5:

```python
import bpy
from mathutils import Vector

# Limpa a cena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Adiciona um cubo, uma esfera e uma pirâmide
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
bpy.ops.mesh.primitive_uv_sphere_add(location=(2, 0, 0))
bpy.ops.mesh.primitive_cone_add(location=(-2, 0, 0))

# Move e rotaciona o cubo (Matriz Model)
cube = bpy.context.scene.objects["Cube"]
cube.location = Vector((0, 1, 0))
cube.rotation_euler = (0.5, 0.5, 0)

# Cria uma câmera e posiciona (Matriz View)
bpy.ops.object.camera_add(location=(0, -5, 2))
camera = bpy.context.scene.objects["Camera"]
camera.rotation_euler = (1.1, 0, 0)

# Define parâmetros de projeção (Matriz Projection)
camera.data.type = 'PERSP'
camera.data.lens = 35  # campo de visão

# Define a câmera ativa
bpy.context.scene.camera = camera

# Renderiza uma imagem
bpy.context.scene.render.filepath = "/tmp/exemplo_blender.png"
bpy.ops.render.render(write_still=True)
```

Esse exemplo mostra como aplicar transformações de posição, rotação e escala (Model), configurar a câmera (View) e ajustar a projeção (Projection) diretamente via script Python no Blender. O resultado é uma imagem renderizada com diferentes objetos e enquadramento de câmera.

