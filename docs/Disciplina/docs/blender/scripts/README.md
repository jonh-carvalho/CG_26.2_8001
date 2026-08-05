Blender 4.5 - scripts para exercícios de animação e transformações 3D

Esta pasta contém scripts Python que usam a API `bpy` do Blender 4.5. Eles implementam os exercícios básicos:

01_prepare_scene.py         - limpa a cena
02_cube_transform.py        - cria um cubo e aplica transformações
03_cube_animation_translation.py - anima translação do cubo
04_linear_interpolation.py  - ajusta interpolação para LINEAR
05_rotation_scale_animation.py - anima rotação e escala
06_generate_spheres.py      - gera 50 esferas aleatórias
07_materials_per_height.py  - aplica materiais baseados em altura
08_parenting_hierarchy.py   - demonstra parent/child e animação do parent
09_render_sequence.py       - renderiza a animação (PNG sequence)
10_export_gltf.py           - exporta a cena para GLB (glTF)

Como executar (Windows, cmd.exe):

Substitua o caminho do blender e o caminho do script conforme seu sistema.

"C:\\Program Files\\Blender Foundation\\Blender 4.5\\blender.exe" --background --python "c:\\caminho\\para\\scripts\\02_cube_transform.py"

Ou, abra o Blender, vá em Scripting -> New Text -> Open o script e pressione Run Script.

Notas:
- Muitos operadores `bpy.ops` funcionam apenas no contexto correto; prefira testar scripts no editor de texto do Blender se der erro em batch.
- Caminhos que usam '//' são relativos ao arquivo .blend; quando você executa em background sem .blend salvo, eles se relacionam ao diretório corrente.
