Com base no **enunciado da AP1**, o objetivo desse roteiro é a **construção de uma cena-conceito 3D estática no Blender 4.5 LTS**, destacando a palavra **Ibmec**, três objetos autorais, organização técnica (coleções, nomes, transformações) e o enquadramento de câmera.

---

### Roteiro Passo a Passo na Interface do Blender 4.5 LTS

#### **Passo 1: Organização e Gestão da Cena no Outliner (10 min)**

1. **Criar a Coleção da AP1:**
   * No painel **Outliner** (canto superior direito), clique com o botão direito e escolha **New Collection**.
   * Renomeie para `AP1_Ibmec_Conceito`.
2. **Criação e Conversão do Texto Principal:**
   * Pressione **`Shift + A`** > **Text**.
   * Pressione **`Tab`** para entrar no Edit Mode, apague o texto e digite `Ibmec`.
   * Volte ao Object Mode (**`Tab`**), vá no painel de propriedades do texto (ícone `a` verde à direita) e, em **Geometry > Extrude**, adicione `0.1 m` de relevo.
   * Clique com o **Botão Direito (RMB)** sobre o texto na Viewport 3D e escolha **Convert To > Mesh** (transformando o texto em malha poligonal).
3. **Resetar Transformações:**
   * Pressione **`Ctrl + A`** > **All Transforms** para congelar a escala `1.0` e a rotação `0.0`.

---

#### **Passo 2: Modelagem Manual dos 3 Objetos Autorais Rápidos (20 min)**
*(Cobre os Requisitos 4 e 6 da AP1: Três objetos autorais e duas técnicas de modelagem além de escala)*

Os alunos devem criar 3 objetos simples na cena usando a interface e identificar cada um no Outliner com nomes claros (ex: `Obj_Podio`, `Obj_Portal`, `Obj_Trofeu`):

* **Objeto 1: Pódio/Plataforma (Modelagem Poligonal — Extrude e Bevel)**
  1. **`Shift + A`** > **Mesh > Cube**. Pressione **`G`**, **`S`** para posicionar na base.
  2. Pressione **`Tab`** (Edit Mode) > tecla **`3`** (seleção de faces). Clique na face superior.
  3. Pressione **`I`** (Inset) e arraste para dentro; pressione **`E`** (Extrude) para puxar para cima.
  4. Pressione **`Ctrl + B`** (Bevel) e mova o mouse para chanfrar as arestas.

* **Objeto 2: Portal de Inovação (Uso de Modificadores — Solidify e Bevel)**
  1. **`Shift + A`** > **Mesh > Cylinder**.
  2. Pressione **`Tab`** (Edit Mode), selecione as faces frontal e traseira e pressione **`X` > Faces** (para deixar o cilindro oco como um anel).
  3. Volte ao Object Mode (**`Tab`**). No painel de propriedades à direita, vá no ícone da **Chave Inglesa (Modifier Properties)**.
  4. Clique em **Add Modifier > Generate > Solidify** e ajuste a espessura (*Thickness*) para `0.15 m`.
  5. Adicione um segundo modificador: **Add Modifier > Generate > Bevel** para suavizar as quinas.

* **Objeto 3: Troféu / Marco Tecnológico (Modelagem por Curva de Revolução)**
  1. **`Shift + A`** > **Curve > Bezier**.
  2. Pressione **`Tab`** (Edit Mode), ajuste os pontos e manipuladores (*handles*) com **`G`**, **`R`**, **`S`** para formar a metade do perfil de uma taça/troféu.
  3. No Object Mode, vá na aba de modificadores e adicione o modificador **Screw** no eixo **Z**.

---

#### **Passo 3: Enquadramento, Câmera e Configuração do Projeto (10 min)**
*(Cobre os Requisitos 3, 5, 7 e 8 da AP1: Destaque da palavra, Câmera e Linha do Tempo de 360 frames)*

1. **Configuração da Câmera Principal:**
   * Pressione **`Shift + A`** > **Camera**. Renomeie no Outliner para `Cam_Principal_AP1`.
   * Pressione **`Numpad 0`** para entrar na visão da câmera.
   * Ajuste a visão desejada na Viewport 3D e pressione **`Ctrl + Alt + Numpad 0`** (Alinha a câmera à visão atual da tela).
   * Nas propriedades da Câmera (ícone de câmera verde) > **Viewport Display > Composition Guides**, marque **Thirds** (Regra dos Terços) para ajudar na composição intencional.
2. **Configuração dos 360 Frames (15 segundos a 24 fps):**
   * Vá no painel **Output Properties** (ícone de impressora no canto direito).
   * Em **Frame Rate**, defina **`24 fps`**.
   * Na linha do tempo inferior (*Timeline*), ajuste o **Start** para `1` e o **End** para **`360`** (totalizando exatamente 15 segundos).

---

### Checklist de Autoavaliação para os Alunos (Tabela de Verificação)

Imprima ou projete esta tabela durante a aula para que cada aluno valide seu próprio arquivo `.blend` antes da entrega final:

| Requisito da AP1 | Ação na Interface do Blender 4.5 LTS | Status |
| :--- | :--- | :---: |
| **1. Versão do Software** | Salvo no formato oficial Blender 4.5 LTS (`.blend`). | [ ] |
| **2. Estrutura de Coleções** | Coleção `AP1_Ibmec_Conceito` criada no Outliner com tudo dentro. | [ ] |
| **3. Destaque da Palavra** | A palavra **Ibmec** está legível e em posição de destaque na câmera. | [ ] |
| **4. Três Objetos Autorais** | 3 objetos criados e renomeados no Outliner (ex: `Obj_Podio`, etc.). | [ ] |
| **5. Transformações Limpas** | `Ctrl + A > All Transforms` aplicado nos objetos principais. | [ ] |
| **6. Técnicas de Modelagem** | Usou pelo menos 2 recursos além de escala (Extrude, Bevel, Modifiers, Curvas). | [ ] |
| **7. Câmera Configurada** | Câmera principal posicionada e enquadrada na composição. | [ ] |
| **8. Configuração de Tempo** | Timeline definida de `1` a `360` frames a `24 fps` (15 segundos). | [ ] |
| **9. Nomenclatura do Arquivo** | Salvo como `AP1_NomeSobrenome.blend`. | [ ] |

---

### Atalhos Essenciais da Interface para Projetar no Quadro

* **Navegação:** `MMB` (Girar visão), `Shift + MMB` (Pan/Mover visão), `Numpad 1` (Vista Frontal), `Numpad 3` (Lateral), `Numpad 7` (Superior), `Numpad 0` (Vista da Câmera).
* **Modos e Seleção:** `Tab` (Alterne entre Object Mode e Edit Mode), `1 / 2 / 3` no Edit Mode (Vértice, Aresta, Face), `A` (Selecionar tudo).
* **Transformações Básicas:** `G` (Mover), `R` (Rotacionar), `S` (Escalar) — seguidos de `X`, `Y` ou `Z` para travar no eixo desejado.
* **Ferramentas de Modelagem:** `E` (Extrusão), `I` (Inset/Inserir face), `Ctrl + B` (Bevel/Chanfro), `Ctrl + R` (Loop Cut/Corte em anel).
* **Organização:** `M` (Mover objeto selecionado para uma Coleção).
