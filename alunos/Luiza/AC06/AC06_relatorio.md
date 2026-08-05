# Relatório Técnico — AC06 Luiza Conrado


## Objetivo da cena

A cena representa uma **mesa de estudo noturna**, composta por mesa, livro, lápis, copo, abajur, câmera e iluminação. O arquivo também inclui animação por keyframes, atendendo ao foco da atividade AC06: uso de linha do tempo, interpolação e renderização de vídeo no Blender.


## Estrutura dos objetos

| Objeto | Tipo | Dados vinculados | Localização XYZ | Escala XYZ | Animação |
|---|---|---|---|---|---|
| Abajur_Base | MESH | Cilindro.001 | (-3.642, -1.1, 0.08) | (0.3, 0.3, 0.06) | — |
| Abajur_Cupula | MESH | Cubo.004 | (-3.63, -1.084, 1.057) | (0.441, 0.441, 0.441) | — |
| Abajur_Haste | MESH | Cilindro.002 | (-3.654, -1.094, 0.738) | (-0.102, -0.102, -0.634) | — |
| Camera | CAMERA | Camera | (6.629, -6.876, 5.298) | (1, 1, 1) | CameraAction |
| Copo | MESH | Cilindro.004 | (1.3, 0.6, 0.244) | (0.243, 0.243, 0.219) | — |
| Lapis | MESH | Cilindro | (-0.799, 0.3, 0.25) | (0.05, 0.05, 0.2) | LapisAction |
| Light | LIGHT | Light | (4.076, 1.005, 5.904) | (1, 1, 1) | — |
| Livro | MESH | Cubo | (-1.2, 0.3, 0.08) | (1.4, 0.9, 0.08) | — |
| Luz_Abajur | LIGHT | Ponto | (-3.719, -1.077, 1.396) | (1, 1, 1) | — |
| Mesa | MESH | Cubo.001 | (0, 0, 0) | (5, 2.5, 0.03) | — |
| Mesa.001 | MESH | Cubo.002 | (0, 0, -1.5) | (0.5, 0.5, 1.5) | — |
| Mesa.002 | MESH | Cubo.003 | (0, 0, -3) | (-2, -1, -0.012) | — |


## Câmera e enquadramento

A câmera está posicionada em `[6.629, -6.876, 5.298]` com lente de **35 mm**. Ela possui ação própria chamada `CameraAction`, com keyframes entre os frames **1 e 239**.

Pontos positivos:

- Existe câmera ativa configurada na cena.
- A câmera está animada, o que ajuda a demonstrar domínio de keyframes.
- O movimento ocorre no começo da animação, criando introdução para a cena.

Ponto de melhoria:

- A câmera tem keyframes de rotação e escala que não alteram valores de forma significativa. Para deixar o Graph Editor mais limpo, seria melhor manter apenas os canais que realmente mudam, principalmente localização.

## Animação

| Ação | Frames usados | F-curves | Keyframes | Canais animados |
|---|---:|---:|---:|---|
| CameraAction | 1–239 | 9 | 18 | location[0,1,2], rotation_euler[0,1,2], scale[0,1,2] |
| LapisAction | 241–470 | 9 | 18 | location[0,1,2], rotation_euler[0,1,2], scale[0,1,2] |

### Descrição das ações

#### `CameraAction`

A câmera se movimenta do frame **1** ao **239**. A animação altera principalmente a posição da câmera:

- Eixo X: 6.629 → 5.723
- Eixo Y: -6.876 → -7.160
- Eixo Z: 5.298 → 6.261

Isso cria um movimento suave de câmera, adequado para apresentar a cena.

#### `LapisAction`

O objeto `Lapis` é animado entre os frames **241** e **470**. A principal alteração ocorre no eixo X:

- Eixo X: -0.799 → -2.241
- Eixos Y e Z permanecem praticamente constantes

A animação do lápis complementa o movimento da câmera e mostra uso de keyframes em objeto de cena.


## Conclusão

O arquivo atende bem à proposta da AC06 por apresentar uma cena completa de mesa de estudo com câmera, iluminação, materiais e animações por keyframes. A cena possui boa base técnica e está pronta para ser documentada no GitHub. Os principais ajustes recomendados são de organização: renomear materiais, corrigir o caminho de saída do render, limpar canais de animação redundantes e conferir a versão do Blender exigida pela atividade.

**Avaliação final:** projeto funcional e coerente, com boa implementação para entrega acadêmica. Com pequenos ajustes de organização e render final, o repositório ficará mais claro e profissional.
