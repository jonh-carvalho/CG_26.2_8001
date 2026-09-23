<!--
Roteiro de referência para a AP1. O aluno pode adaptar a composição, desde que
preserve os requisitos da avaliação e identifique as próprias decisões.
-->

# Roteiro prático — “Ibmec: Portal de Ideias”

## Proposta

Criar uma cena 3D em que a palavra **Ibmec** aparece no centro de um portal
geométrico. A câmera começa diante de uma composição ainda incompleta; durante
os 15 segundos planejados, três objetos autorais sugerem conhecimento,
conexão e inovação. No quadro final, o portal está organizado e a marca está
legível como o elemento principal.

Esta proposta é um ponto de partida. O aluno pode substituir os objetos, mas
deve manter exatamente três objetos autorais identificados no relatório.

## Os três objetos autorais

Os objetos abaixo são simples o bastante para serem construídos a partir de
primitivas, mas permitem demonstrar edição e modificadores:

1. **Objeto_A — Livro_Ideias**: um livro aberto, feito com dois blocos finos e uma lombada. Representa conhecimento e pode receber uma animação de abertura	na AP2.
2. **Objeto_B — Ponte_Conexao**: uma pequena ponte curva ligando o livro ao	portal. Representa passagem e conexão. Pode ser construída com uma curva com bevel ou com blocos repetidos ao longo de uma trajetória.
3. **Objeto_C — Esfera_Inovacao**: uma esfera central com três anéis inclinados. Representa inovação e movimento. Use modificador Bevel ou Subdivision apenas se isso ajudar a controlar a forma; a esfera e os anéis continuam sendo um único objeto autoral composto.

O texto `Ibmec`, o portal, o piso, a câmera e as luzes são elementos da cena, mas não entram na contagem dos três objetos autorais.

## Resultado esperado da cena

No enquadramento principal, o portal ocupa a região central e o texto `Ibmec` fica em primeiro plano visual, grande, horizontal e sem ficar escondido pelos objetos. O livro aparece à esquerda, a ponte conduz o olhar até o portal e a esfera fica à direita ou acima do eixo da composição. Deixe espaço livre entre os objetos para que cada um possa ser identificado nas capturas.

Uma composição possível, olhando de frente para a câmera:

```text
							  Esfera_Inovacao
										o
		  Livro_Ideias  ===== Ponte_Conexao =====  [ PORTAL ]
																	Ibmec
```

## Roteiro visual dos 15 segundos

Use **24 fps**, com `Frame Start = 1` e `Frame End = 360`. A animação não é
obrigatória na AP1; os momentos abaixo funcionam como planejamento para a AP2.

| Momento | Frames | O que o espectador deve perceber | Planejamento para a AP2 |
|---|---:|---|---|
| Início | 1–96 (0–4 s) | Livro, ponte e esfera estão separados; o portal aparece parcialmente. | Câmera faz uma aproximação suave e o livro abre levemente. |
| Construção | 97–240 (4–10 s) | A ponte conduz a esfera até o centro e o portal passa a enquadrar a marca. | Animar a esfera pela ponte e a rotação dos anéis. |
| Destaque | 241–312 (10–13 s) | `Ibmec` está totalmente legível e domina a composição. | Texto surge ou ganha escala; câmera estabiliza no enquadramento principal. |
| Encerramento | 313–360 (13–15 s) | A cena termina organizada, com os três objetos ainda reconhecíveis. | Pequeno movimento de câmera ou rotação contínua da esfera, sem cobrir o texto. |

## Construção guiada no Blender 4.5 LTS

### 1. Configuração inicial

1. Abra o Blender **4.5 LTS** e salve imediatamente como
	`AP1_NomeSobrenome.blend`.
2. Na cena, crie uma coleção chamada `AP1_Ibmec_Conceito`.
3. Mova para essa coleção todos os elementos criados neste roteiro. Se desejar,
	crie dentro dela as subcoleções `Marca`, `Objetos_Autorais`, `Cenario` e
	`Camera_Luzes`.
4. Em `Output Properties`, defina `24 fps`, quadro inicial `1` e quadro final
	`360`.
5. Trabalhe inicialmente em vista frontal ou em uma vista de câmera que permita
	comparar a legibilidade da palavra durante todo o processo.

### 2. Piso e portal

1. Adicione um plano para o piso e nomeie-o `Aux_Piso`. Faça uma escala ampla no eixo X e aplique a escala com `Ctrl+A > Scale`.
    - Na Collection `Cenario`, o plano pode ser usado como referência de escala e perspectiva. Não é necessário detalhar ou texturizar nesta etapa.
    - O que faz o Ctrl+A > Scale é aplicar a escala do objeto, garantindo que transformações futuras (como extrusão ou bevel) funcionem corretamente e que o objeto se comporte de forma previsível em relação a modificadores e iluminação.
2. Para o portal, adicione um cubo, nomeie-o `Portal_Moldura` e use `Tab` para
	entrar no Edit Mode.
    - o CUBO deve estar frontalmente posicionado em relação à câmera, com a face frontal voltada para o espectador.
        - Rotacionar o cubo 90° no eixo X ou Y pode ser necessário para alinhar a face frontal com a câmera.
    - Faça um `Inset` na face frontal e depois um `Extrude` para dentro, criando uma abertura. Remova a face central ou modele duas colunas e uma travessa
	para deixar o texto visível.
    - Aplique um pequeno `Bevel` nas arestas. Esses passos demonstram inset,
	extrusão e bevel sem depender de escala simples de primitivas.

### 3. Palavra principal

1. Use `Add > Text`, altere o conteúdo para `Ibmec` e nomeie o objeto como
	`Marca_Ibmec`.
2. Em `Object Data Properties > Geometry`, ajuste `Extrude` para criar volume e
	use um `Bevel Depth` pequeno para suavizar as bordas.
3. Gire o texto para ficar de frente para a câmera e posicione-o no centro do
	portal. Ajuste apenas o necessário para preservar a leitura da marca.
4. Se converter o texto para malha, faça isso apenas depois de conferir a
	ortografia e a proporção: `Object > Convert > Mesh`. A conversão não é
	obrigatória para a AP1.

### 4. Modelagem dos três objetos autorais

#### Objeto A — Livro_Ideias

1. Adicione um cubo e nomeie-o `Livro_Ideias_Capa_Esquerda`. Ajuste a escala
	para formar uma capa fina e aplique a escala.
2. Duplique-o para formar `Livro_Ideias_Capa_Direita`; crie uma lombada estreita
	com outro cubo ou una as partes com `Ctrl+J` depois de ajustar a posição.
3. Adicione algumas páginas com um bloco menor ou use `Inset` nas capas. O
	conjunto deve ser claramente um livro aberto, mesmo em viewport solid.
4. Mantenha o conjunto dentro de uma coleção ou use o nome-base
	`Objeto_A_Livro_Ideias` nos objetos que o compõem.

#### Objeto B — Ponte_Conexao

1. Crie uma curva Bezier e nomeie-a `Objeto_B_Ponte_Conexao`.
2. Edite os pontos da curva para ligar a região do livro ao portal. Em
	`Object Data Properties > Geometry`, aumente `Bevel Depth` para dar volume.
3. Se preferir uma ponte modular, crie um bloco, aplique `Bevel` e duplique os
	módulos ao longo da curva. Una os módulos ao final para manter a organização.
4. Confira na câmera se a ponte conduz o olhar sem atravessar ou esconder
	`Marca_Ibmec`.

#### Objeto C — Esfera_Inovacao

1. Adicione uma UV Sphere e nomeie-a `Objeto_C_Esfera_Inovacao`.
2. Crie três toros ou curvas circulares ao redor da esfera, inclinando-os em
	eixos diferentes. Una-os à esfera com `Ctrl+J` somente quando desejar tratar
	o conjunto como um objeto autoral único.
3. Aplique `Shade Auto Smooth` ou um `Bevel` discreto, sem apagar a leitura dos
	anéis. Posicione a esfera no fim da ponte ou em uma posição elevada.

### 5. Transformações e organização

Verifique no painel `Item` que cada objeto recebeu transformações intencionais.
Registre no relatório exemplos como:

- translação do livro para a esquerda e da esfera para o final da ponte;
- rotação dos anéis da esfera e da câmera;
- escala do texto e do portal para estabelecer hierarquia visual;
- aplicação de escala antes de usar bevel ou extrusão, quando necessário.

Use nomes coerentes no Outliner e evite deixar objetos como `Cube.001` ou
`BezierCurve` sem identificação.

### 6. Câmera principal

1. Crie ou selecione uma câmera e nomeie-a `Camera_Principal`.
2. Posicione-a em uma vista de três quartos, com o texto ocupando o centro do
	enquadramento e os três objetos visíveis.
3. Use `Numpad 0` para conferir a câmera. Ajuste a distância focal ou a posição
	antes de alterar excessivamente a escala dos objetos.
4. Deixe a câmera pronta para a AP2. Não é necessário inserir keyframes na AP1.

## Checklist de conferência

- [ ] O arquivo usa Blender 4.5 LTS e foi salvo como `AP1_NomeSobrenome.blend`.
- [ ] Existe a coleção `AP1_Ibmec_Conceito`.
- [ ] `Marca_Ibmec` está grande, legível e em destaque na câmera principal.
- [ ] Existem exatamente três objetos autorais identificados: livro, ponte e esfera.
- [ ] Foram usados pelo menos dois recursos além de escala, como extrusão,
		inset, bevel, curva ou composição de malhas.
- [ ] `Camera_Principal` está configurada e mostra a composição completa.
- [ ] A cena está configurada para 24 fps e 360 frames.
- [ ] O storyboard contém início, construção/destaque e encerramento.
- [ ] O relatório explica o conceito, os três objetos, as técnicas e o plano da AP2.

## Capturas e relatório

Entregue uma captura do enquadramento principal em Solid ou Material Preview e
três capturas adicionais que permitam identificar o livro, a ponte e a esfera,
além da palavra `Ibmec`. No relatório, use os nomes do Outliner e descreva em
uma ou duas frases a função de cada objeto.

Para a AP2, a evolução mais direta é animar a câmera, abrir o livro, mover a
esfera pela ponte, girar seus anéis e finalizar a cena com materiais e
iluminação. A ideia e a organização da AP1 devem permanecer reconhecíveis.
