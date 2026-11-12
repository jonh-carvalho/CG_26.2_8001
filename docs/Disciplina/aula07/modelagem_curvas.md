Para construir um objeto tridimensional simples (como uma **Taça de Vinho** ou um **Vaso**) usando curvas interativas no **Blender 4.5 LTS** via mouse e interface gráfica, aplicamos o conceito de **varredura rotacional (superfície de revolução)**. Nesse método, desenha-se metade do perfil 2D do objeto usando uma curva paramétrica de Bézier e faz-se a rotação de 360° em torno do eixo central.

---

### 🍷 Roteiro Passo a Passo no Blender 4.5 LTS

#### **Passo 1: Preparação da Cena e Vista 2D**
1. Abre o **Blender 4.5 LTS**.
2. Clique no cubo padrão da cena com o **Botão Esquerdo do Mouse (LMB)** e pressione `X` (ou a tecla `Delete`) para apagá-lo.
3. Alterne para a vista frontal plana pressionando a tecla **`Numpad 1`** (ou clicando no círculo verde `-Y` no Gizmo de navegação no canto superior direito).

---

#### **Passo 2: Inserção da Curva de Bézier**
1. Pressione **`Shift + A`** para abrir o menu de adição > passe o mouse em **Curve** > clique em **Bezier**.
2. Com a curva selecionada, pressione a tecla **`Tab`** para entrar no **Edit Mode** (Modo de Edição).
3. Pressione **`A`** para selecionar os pontos padrão e pressione **`X` > Vertices** para apagar o segmento padrão e começar do zero.

---

#### **Passo 3: Desenho do Perfil (Curva Geratriz)**
1. Na barra de ferramentas à esquerda da Viewport 3D, clique na ferramenta **Draw** (ícone de caneta/curva).
2. Com o mouse, clique e arraste na tela desenhando metade da taça (do centro da base até a borda superior):
   - **Base:** Clique perto do eixo vertical central verde (\\(Z\\)).
   - **Haste:** Arraste para cima criando uma linha fina.
   - **Bojo:** Faça a curvatura do copo subindo até a borda.
3. Para fazer ajustes finos nos pontos e manipuladores (*handles*):
   - Alterne para a ferramenta **Select** (tecla `W`).
   - Clique em qualquer ponto de controle com o **LMB** e pressione **`G`** para mover com o mouse.
   - Clique na extremidade da haste e pressione **`S`** para rotacionar/escalar a tangente e controlar a suavidade da curva.

---

#### **Passo 4: Aplicação da Varredura Rotacional (Screw Modifier)**
1. Pressione **`Tab`** para voltar ao **Object Mode** (Modo de Objeto).
2. No painel de propriedades à direita, clique no ícone de chave inglesa (**Modifier Properties**).
3. Clique em **Add Modifier** > vá na aba **Generate** > selecione **Screw**.
4. Nas configurações do modificador **Screw**:
   - Verifique se o **Axis** está definido em **`Z`** (eixo de rotação).
   - Aumente o campo **Steps Viewport** para **`32`** ou **`64`** para tornar a superfície perfeitamente arredondada.

---

#### **Passo 5: Dar Espessura de Vidro ao Objeto**
1. No mesmo painel de modificadores, clique em **Add Modifier** > **Generate** > **Solidify**.
2. Ajuste o parâmetro **Thickness** para `0.02 m` (2 cm) para criar a parede de vidro interna do recipiente.
3. Na Viewport 3D, clique com o **Botão Direito do Mouse (RMB)** sobre a taça e selecione **Shade Smooth** para suavizar as sombras.

---

### 🎥 Demonstrações Parecidas no YouTube

Para acompanhar esse fluxo de trabalho em vídeo, você pode pesquisar no YouTube pelos seguintes termos e tutoriais recomendados:

*   **Termos de busca diretos:**
    *   `Blender Bezier Curve Screw Modifier Glass`
    *   `Modelagem com curvas Blender vaso taça`
*   **Vídeos de referência:**
    *   **Canal Grant Abbitt / CG Boost:** Tutoriais intitulados *"Blender Curve Modeling for Beginners"* mostram exatamente o desenho de perfis 2D com *handles* de Bézier e a rotação com o modificador *Screw*.
    *   **Canal Blender Brasil / Luan3D:** Busque por *"Modelando vaso/garrafa com curvas no Blender"*, que demonstra a interação prática com a interface em português.
