## 1. Planejamento e Conceituação
* **Definição de Requisitos:** Determine a finalidade da animação (jogos, cinema, etc.), os movimentos que o modelo precisa executar e quem irá animá-lo.
* **Posição na Produção:** Compreenda o rigging como a ponte entre a etapa de modelagem e a fase de *posing* e animação.

### 2. Preparação da Malha (Modelo 3D)
* **Topologia e Pose de Referência:** Garanta que a malha tenha loops de arestas suficientes nas articulações para dobrar sem colapsar e que o modelo esteja em uma pose neutra.
* **Alinhamento e Escala:** Verifique a simetria, resete a escala e a rotação da malha, e ajuste a sua origem antes de criar o esqueleto.

### 3. Construção do Esqueleto (*Armature* e *Bones*)
* **Criação dos Ossos:** Adicione o objeto *Armature* (em *Object Mode*) e posicione as extremidades (*Head* e *Tail*) dos ossos no modo *Edit Mode*, ajustando o alinhamento dos eixos (*Roll*).
* **Hierarquia:** Estabeleça relações de parentesco (*Parent*) e conexões entre ossos pais e filhos.
* **Organização com Bone Collections:** Utilize as **Bone Collections** do Blender 4.5 para organizar e agrupar ossos por função ou região do corpo.

### 4. Configuração de Controles e Restrições (*Constraints*)
* **Divisão de Funções:** Distinga ossos de deformação (*Deform bones*), ossos de controle (*Control bones*) e auxiliares (*Helper bones*).
* **Sistemas FK e IK:**
  * **FK (*Forward Kinematics*):** Configure para obter controle direto das rotações ao longo de uma cadeia (ex.: braço ou rabo).
  * **IK (*Inverse Kinematics*):** Aplique restrições IK com alvos para posicionar facilmente extremidades como pés e mãos.
* **Formas de Controle (*Custom Shapes*):** Substitua a visualização padrão de ossos por formas geométricas personalizadas para facilitar a seleção pelo animador.

### 5. Associação da Malha e Ajuste de Pesos (*Skinning*)
* **Vínculo:** Associe a malha ao esqueleto usando o **Armature Modifier** e crie a correspondência de vértices via **Vertex Groups**.
* **Weight Painting:** No modo *Weight Paint Mode*, ajuste as influências (*weights*) das articulações (como ombros, cotovelos e joelhos) para evitar deformações estranhas e estiramentos.

### 6. Teste e Validação
* **Ajustes no *Pose Mode*:** Manipule os controles em posições e movimentos extremos para testar limites de deformação e praticidade dos controles.
* **Revisão Iterativa:** Corrija falhas de peso ou posição de ossos reveladas pelos testes.

Para aplicar o roteiro de rigging de forma prática e sem complicações, a melhor atividade introdutória é o **Rigging de um Cilindro Articulado** (como um dedo ou braço mecânico simples). Esse exercício passa por todas as etapas fundamentais sem a complexidade de um personagem completo.

---

### Prática Guiada: Rigging de um Cilindro Articulado

**Objetivo:** Criar um tubo simples de dois segmentos e montar um esqueleto de 2 ossos para entender como a malha responde às rotações e ao peso da articulação.

#### **Etapa 1: Planejamento**
* **Meta:** Fazer com que um cilindro dobre suavemente no ponto médio, simulando uma junta ou articulação de dedo/braço.

#### **Etapa 2: Preparação da Malha**
1. No **Object Mode**, adicione um cilindro: **`Shift + A` > Mesh > Cylinder**.
2. Escale o cilindro no eixo Z para deixá-lo alongado (**`S` > `Z`**).
3. Entre no **Edit Mode** (**`Tab`**) e adicione **3 Loop Cuts** horizontais exatamente na metade do cilindro (**`Ctrl + R`**, use a roda do mouse para 3 cortes): *essa densidade de arestas no centro previne que a malha colapse ou achate ao dobrar*.
4. Volte ao **Object Mode** e aplique a escala/transformações: **`Ctrl + A` > All Transforms** (garante que a escala esteja em `1.0`).

#### **Etapa 3: Construção do Esqueleto (*Armature*)**
1. Adicione um osso básico: **`Shift + A` > Armature**.
2. Na aba de propriedades do esqueleto (*Object Data Properties* - ícone do boneco verde), em **Viewport Display**, marque a opção **In Front** (para enxergar o osso dentro do cilindro).
3. Entre no **Edit Mode** do esqueleto:
   * Posicione a base do primeiro osso na parte inferior do cilindro e a ponta no centro (onde estão os loop cuts).
   * Selecione a ponta superior e pressione **`E`** (**Extrude**) puxando o segundo osso até o topo do cilindro.
4. Renomeie os ossos no painel *Bone Properties*: `Bone_Base` e `Bone_Ponta`.

#### **Etapa 4: Configuração de Controles**
* Para esta prática inicial, utilizaremos a hierarquia FK padrão (onde o osso da ponta é filho do osso da base).

#### **Etapa 5: Associação da Malha e Ajuste de Pesos (*Skinning*)**
1. No **Object Mode**, selecione primeiro a **malha do cilindro** e, em seguida, mantenha **`Shift`** pressionado e selecione o **esqueleto**.
2. Pressione **`Ctrl + P`** e selecione **With Automatic Weights**.
3. Selecione apenas a malha e mude para o **Weight Paint Mode** na lista suspensa do canto superior esquerdo:
   * Selecione `Bone_Ponta` para ver a influência dos pesos (vermelho indica 100% de controle, azul indica 0%). Note o gradiente suave na região central.

#### **Etapa 6: Teste e Validação**
1. Selecione a armature e entre no **Pose Mode** (**`Ctrl + Tab`**).
2. Selecione `Bone_Ponta` e pressione **`R`** para rotacionar.
3. Observe como a articulação do cilindro dobra e confirme se a deformação da malha permanece natural.

---

### Passo a Passo: Configurando IK no Cilindro Articulado

#### **Passo 1: Criar os Ossos de Controle (*IK Target* e *Pole Target*)**
1. Selecione a **Armature** e entre no **Edit Mode** (**`Tab`**).
2. **Criar o osso de ponta (*IK Target*):**
   * Selecione a junta do topo do osso `Bone_Ponta`.
   * Pressione **`E`** (**Extrude**) e puxe um novo osso curto para cima.
   * Com o novo osso selecionado, pressione **`Alt + P`** e escolha **Clear Parent** (para soltá-lo da hierarquia).
   * No painel *Bone Properties*, renomeie-o para **`IK_Target`** e **desmarque** a caixa **Deform** (pois ele servirá apenas de controle, não para deformar a malha).
3. **Criar o osso da junta/joelho (*Pole Target*):**
   * Selecione a junta central (entre a base e a ponta).
   * Pressione **`E`** e extrude um osso para a frente.
   * Pressione **`Alt + P`** > **Clear Parent** e posicione-o um pouco afastado à frente da articulação.
   * Renomeie-o para **`IK_Pole`** e **desmarque** a caixa **Deform**.

#### **Passo 2: Aplicar a Restrição *Inverse Kinematics***
1. Mude para o **Pose Mode** (**`Ctrl + Tab`**).
2. Selecione o osso **`Bone_Ponta`** (o osso da ponta da cadeia principal).
3. Na barra lateral de propriedades (à direita), acesse a aba **Bone Constraint Properties** (ícone de um osso com anéis).
4. Clique em **Add Bone Constraint** e selecione **Inverse Kinematics**.

#### **Passo 3: Configurar os Parâmetros da IK**
No painel da constraint no `Bone_Ponta`, preencha as opções:
* **Target:** Selecione a sua **Armature**.
* **Bone:** Escolha o osso **`IK_Target`**.
* **Pole Target:** Selecione a sua **Armature**.
* **Bone:** Escolha o osso **`IK_Pole`**.
* **Chain Length:** Mude o valor para **`2`** *(crucial: isso limita a ação da IK aos 2 ossos da articulação, sem afetar a base do rig)*.

#### **Passo 4: Ajustar a Orientação (*Pole Angle*)**
Se o cilindro torcer ou girar de lado ao conectar o *Pole Target*:
* Ajuste o valor de **Pole Angle** no card da constraint (geralmente ajustando para `90°`, `-90°` ou `180°`) até que a junta volte à posição neutra virada para frente.

#### **Passo 5: Testar o Funcionamento**
* Selecione o osso **`IK_Target`** e pressione **`G`** para movê-lo: veja os dois ossos dobrando automaticamente para acompanhar a ponta.
* Selecione o osso **`IK_Pole`** e mova-o para redirecionar para onde a articulação aponta.
