# Introdução à Animação


A animação é um dos pilares da computação gráfica, permitindo dar vida a objetos, personagens e cenários digitais. Por meio da animação, é possível criar movimentos, transições e efeitos visuais que enriquecem aplicações como jogos, filmes, simulações e interfaces interativas.

## Conceitos Fundamentais

A animação digital consiste em modificar propriedades de objetos ao longo do tempo, como posição, rotação, escala e cor. Para isso, utilizamos transformações geométricas 3D, que são operações matemáticas aplicadas aos vértices dos objetos:

- Translação: Move o objeto de um ponto a outro no espaço.
- Rotação: Gira o objeto em torno de um eixo.
- Escala: Altera o tamanho do objeto.

Essas transformações podem ser combinadas para criar movimentos complexos e realistas.

### Exemplos Iniciais com Blender

Vamos explorar animação com transformações geométricas no Blender, siga estes passos básicos:

- Crie um objeto 3D
- Adicione um cubo, esfera ou qualquer forma básica à cena.
- Aplique uma animação de translação
- Selecione o objeto, pressione I para inserir um quadro-chave (keyframe) de localização no início da linha do tempo. Avance alguns frames, mova o objeto para uma nova posição e insira outro quadro-chave.

- Adicione rotação e escala
Repita o processo para rotacionar ou escalar o objeto, inserindo quadros-chave para cada transformação.

- Visualize a animação
    - Pressione Play para ver o objeto se mover, girar ou mudar de tamanho ao longo do tempo.

Esses exemplos iniciais mostram como as transformações geométricas são a base para criar animações em ambientes 3D. Com o Blender, é possível combinar múltiplas transformações, ajustar curvas de movimento e criar sequências animadas ricas e interativas.

## Animação 3D com Python no Blender 4.4

Abaixo está um exemplo simples de script Python para animar um cubo no Blender 4.4. O cubo será movido, rotacionado e escalado ao longo de 50 frames:

```python
import bpy

# Limpa a cena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Adiciona um cubo
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
cube = bpy.context.active_object

# Define quadros-chave para animação
cube.location = (0, 0, 0)
cube.keyframe_insert(data_path="location", frame=1)
cube.rotation_euler = (0, 0, 0)
cube.keyframe_insert(data_path="rotation_euler", frame=1)
cube.scale = (1, 1, 1)
cube.keyframe_insert(data_path="scale", frame=1)

# Translação, rotação e escala no frame 50
cube.location = (3, 2, 1)
cube.keyframe_insert(data_path="location", frame=50)
cube.rotation_euler = (0, 0, 3.14)  # Rotação de 180 graus no eixo Z
cube.keyframe_insert(data_path="rotation_euler", frame=50)
cube.scale = (2, 0.5, 1)
cube.keyframe_insert(data_path="scale", frame=50)

# Adiciona uma câmera
bpy.ops.object.camera_add(location=(7, -7, 5), rotation=(1.1, 0, 0.8))
camera = bpy.context.active_object
bpy.context.scene.camera = camera

# Adiciona uma luz
bpy.ops.object.light_add(type='POINT', location=(4, -4, 6))
light = bpy.context.active_object
light.data.energy = 1000
```

Esse script pode ser executado no editor de texto do Blender. Ele cria um cubo e anima sua posição, rotação e escala entre os frames 1 e 50, utilizando transformações geométricas 3D.