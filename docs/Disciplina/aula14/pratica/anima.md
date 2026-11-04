## 1. Planejamento e Fundamentos (*Posing & Timing*)

* **Definição da Ação:** Planeje o movimento antes de inserir quadros-chave (use esboços em papel, gravação de vídeos de referência ou thumbnails rápidos).
* **12 Princípios da Animação:** Identifique quais princípios essenciais serão aplicados na cena (*Squash & Stretch*, *Anticipation*, *Arcs*, *Timing & Spacing*, *Overlapping Action*).
* **Taxa de Quadros (*FPS*):** Defina a taxa de quadros no painel de saída (geralmente **24 fps** para cinema/animação tradicional ou **30/60 fps** para jogos).

### 2. Configuração do Espaço de Trabalho no Blender
* **Organização das Janelas:** Configure a interface com a **3D Viewport**, a **Timeline**, o **Dope Sheet** (para controlar posições dos quadros) e o **Graph Editor** (para ajustar a aceleração das curvas).
* **Modo de Seleção:** Se for animar um rig/personagem, trabalhe no **Pose Mode** (`Ctrl + Tab`). Se for um objeto simples (como uma bola ou câmera), trabalhe no **Object Mode**.
* **Autokeying (*Opcional*):** Decida se usará inserção manual de keyframes (**`I`**) ou a gravação automática (*Auto Keying*).

### 3. Etapa de Blocagem (*Blocking*)
* **Poses Chave (*Key Poses*):** Crie as poses mais importantes do movimento nos quadros principais da linha do tempo.
* **Inserção de Keyframes:** Pressione **`I`** e insira chaves para **Location, Rotation, Scale** ou **K-Slot / Available** para registrar o estado dos controles.
* **Interpolação em *Constant*:** Mude o tipo de interpolação para **Constant** (`T` > *Constant* no Dope Sheet). Isso permite avaliar o *timing* puro e a silhueta das poses sem que o computador crie suavizações automáticas pré-maturas.

### 4. Adição de Intervalos (*Breakdowns & In-Betweens*)
* **Poses Intermediárias (*Breakdowns*):** Adicione chaves nos quadros entre as poses principais para definir a trajetória do movimento (se ele faz um arco para cima, para baixo, etc.).
* **Definição de Arcos:** Ajuste os controles para garantir que braços, cabeças e objetos sigam arcos suaves em vez de trajetórias em linha reta.
* **Deslocamento de Tempos (*Staggering / Overlapping*):** Desloque keyframes de partes secundárias (como cabelo, roupas ou cauda) em 2 ou 3 quadros após a ação principal para criar continuidade realista.

### 5. Polimento no *Graph Editor* (*Splining & Curves*)
* **Transição para *Bezier*:** Mude a interpolação das curvas para **Bezier** (`T` > *Bezier*) para gerar um movimento contínuo.
* **Ajuste de Alças (*Handles*):** No **Graph Editor**, ajuste as alças das curvas para controlar a aceleração e desaceleração (*Ease In / Ease Out*):
  * Curvas inclinadas = velocidade alta.
  * Curvas horizontais/suaves = desaceleração e repouso.
* **Limpeza de Ruídos:** Elimine chaves desnecessárias para evitar trepidações ou sobressaltos indesejados nas trajetórias.

### 6. Validação e Pré-visualização (*Playblast*)
* **Playback em Tempo Real:** Pressione **`Espaço`** para assistir à animação em velocidade real.
* **Geração de Playblast (*Viewport Render*):** Vá em **View > Viewport Render Animation** no menu da 3D Viewport para exportar um vídeo leve e verificar o *timing* sem travamentos de renderização pesada.

---

## Prática Guiada: Animação da Bola Saltando (*Bouncing Ball*)

**Objetivo:** Criar a animação de uma bola quicando e avançando, ajustando as curvas de gravidade e a elasticidade do impacto.

#### **Passo 1: Preparar a Cena**
1. No **Object Mode**, adicione a bola: **`Shift + A` > Mesh > UV Sphere**.
2. Adicione o chão: **`Shift + A` > Mesh > Plane** e dimensione (**`S` > `5`**).
3. Selecione a esfera, suba-a para que fique exatamente sobre a superfície do chão.
4. Na linha do tempo (*Timeline*), ajuste o intervalo de animação para **1 a 40 quadros**.

#### **Passo 2: Blocar a Queda e o Quique (Eixo Z)**
1. **Quadro 1 (Topo inicial):** Posicione a bola no alto (ex.: `Z = 5.0`). Pressione **`I` > Location** para criar o keyframe.
2. **Quadro 10 (Primeiro impacto):** Mova a agulha para o quadro 10, baixe a bola até encostar no chão (`Z = 1.0`) e pressione **`I` > Location**.
3. **Quadro 20 (Segundo ápice):** No quadro 20, suba a bola a uma altura menor que a inicial (`Z = 3.5`) e insira a chave.
4. **Quadro 28 (Segundo impacto):** Baixe a bola até o chão (`Z = 1.0`) e marque o keyframe.
5. **Quadro 35 (Último impulso):** Suba levemente (`Z = 1.5`) e conclua no **Quadro 40** no chão (`Z = 1.0`).

#### **Passo 3: Ajustar a Gravidade no *Graph Editor***
Por padrão, o Blender suaviza todas as entradas e saídas. Vamos ajustar os vetores para dar impacto real ao chão:
1. Abra a janela do **Graph Editor**.
2. Selecione apenas o canal **Z Location**.
3. Selecione as chaves dos quadros de impacto no chão (quadros **10**, **28** e **40**).
4. Pressione **`V`** e escolha **Vector**. As alças mudarão para um formato em "V" bem nítido, fazendo a bola quicar instantaneamente ao tocar o chão sem perder velocidade.
5. As chaves dos pontos mais altos (**1**, **20** e **35**) devem continuar com alças horizontais suaves para simular a perda de velocidade no topo do arco.

#### **Passo 4: Adicionar Deslocamento Horizontal (Eixo X)**
1. No **Quadro 1**, mova a bola para a esquerda (`X = -4.0`) e salve o keyframe de localização.
2. No **Quadro 40**, desloque a bola para a direita (`X = 4.0`) e insira a chave.
3. No **Graph Editor**, selecione a curva **X Location** e mude a interpolação para linear (**`T` > Linear**) para que a velocidade para frente permaneça constante durante os saltos.

#### **Passo 5: Aplicar o *Squash & Stretch* (Deformação por Impacto)**
1. **Um quadro antes do impacto (Quadro 9):** Estique a bola na direção da queda (**`S` > `Z` > `1.2`** e encolha um pouco X e Y). Insira um keyframe em **Scale** (**`I` > Scale**).
2. **No momento do impacto (Quadro 10):** Amasse a bola contra o chão (**`S` > `Z` > `0.7`** e alargue X e Y para **`1.3`**). Salve o keyframe de **Scale**.
3. **Dois quadros após o impacto (Quadro 12):** Estique a bola levemente na subida antes de voltar ao tamanho normal (`1.0, 1.0, 1.0`) no topo do salto.

#### **Passo 6: Playback e Ajustes**
* Pressione **`Espaço`** para rodar a animação. 
* Observe a sensação de peso: se a bola parecer de borracha dura, diminua o *Squash*; se parecer uma bexiga com água, aumente a deformação.

---

Aqui está o guia passo a passo para criar um **rig de bola com *Stretch Bones*** no Blender 4.5. Esse sistema utiliza a restrição *Stretch To* para calcular automaticamente o achatamento (*Squash*) e o esticamento (*Stretch*) com preservação de volume real.

---

## Passo a Passo: Rigging da Bola com *Stretch Bones*

#### **Passo 1: Criar a Estrutura de Ossos (*Armature*)**
1. No **Object Mode**, adicione o esqueleto: **`Shift + A` > Armature**.
2. Na aba **Object Data Properties** (ícone do boneco verde), no painel **Viewport Display**, marque a caixa **In Front** para enxergar os ossos através da esfera.
3. Entre no **Edit Mode** (**`Tab`**):
   * **Osso de Deformação (`Ball_Deform`):** Posicione a base do osso na parte inferior da esfera e a ponta no topo (ele deve atravessar a esfera de baixo para cima).
   * **Osso de Controle Superior (`Stretch_Ctrl`):** Selecione a ponta do `Ball_Deform`, pressione **`E`** (**Extrude**) e puxe um pequeno osso para cima. Com ele selecionado, pressione **`Alt + P` > Clear Parent** para deixá-lo solto.
   * **Osso de Controle Base (`Root_Ctrl`):** Adicione um osso horizontal no chão logo abaixo da esfera para servir de controle principal de movimento da cena.
4. **Ajustar a Hierarquia (Parentesco):**
   * Selecione `Ball_Deform`, depois `Root_Ctrl` e pressione **`Ctrl + P` > Keep Offset**.
   * Selecione `Stretch_Ctrl`, depois `Root_Ctrl` e pressione **`Ctrl + P` > Keep Offset**.
5. No painel **Bone Properties**, desmarque a caixa **Deform** dos ossos `Root_Ctrl` e `Stretch_Ctrl` (apenas o `Ball_Deform` deve deformar a malha).

#### **Passo 2: Configurar a Constraint *Stretch To***
1. Mude para o **Pose Mode** (**`Ctrl + Tab`**).
2. Selecione o osso de deformação **`Ball_Deform`**.
3. Na barra lateral direita, acesse a aba **Bone Constraint Properties** (ícone de um osso com anéis).
4. Clique em **Add Bone Constraint** e selecione **Stretch To**.
5. Configure os seguintes parâmetros:
   * **Target:** Selecione a sua **Armature**.
   * **Bone:** Escolha o osso **`Stretch_Ctrl`**.
   * **Original Length:** Clique no botão **Reset Original Length** para gravar a altura padrão de repouso.
   * **Volume:** Mantenha marcada a opção de preservação de volume em **`XZ`** ou **`Maintain Volume`**.

#### **Passo 3: Parentear a Esfera ao Esqueleto (*Skinning*)**
1. Volte ao **Object Mode**.
2. Selecione a **Esfera** e, mantendo **`Shift`** pressionado, selecione a **Armature**.
3. Pressione **`Ctrl + P`** e escolha **With Automatic Weights**.

#### **Passo 4: Como Utilizar o Rig na Prática**
Entre no **Pose Mode** para testar os controles:
* **Translação da Cena:** Mova o osso **`Root_Ctrl`** (**`G`**) para deslocar a bola inteira pela cena.
* **Elasticidade Automática:** Mova o osso **`Stretch_Ctrl`** para baixo para simular o **Squash** (a bola achata no eixo vertical e ganha largura nos lados automaticamente). Puxe-o para cima para simular o **Stretch** (a bola estica e afina as laterais).

