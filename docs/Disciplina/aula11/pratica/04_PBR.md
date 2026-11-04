Com base na nota selecionada sobre **PBR (Physically Based Rendering)**, aqui está o **roteiro prático de execução** para configurar e visualizar materiais no **Blender 4.5 LTS**:

---

### **Roteiro Prático: Introdução ao PBR no Blender 4.5 LTS**

#### **1. Fundamentação e Princípios Físicos**
* **Conservação de Energia:** Uma superfície jamais reflete mais luz do que recebe. No nó **Principled BSDF** do Blender 4.5, ao ajustar o brilho especular, o software reduz a componente difusa automaticamente para manter o balanço energético físico.
* **Rugosidade (`Roughness`):** Controla as microfacetas microscópicas da superfície. Varia de **`0.0`** (reflexão espelhada/nítida) a **`1.0`** (reflexão totalmente dispersa/difusa).

---

#### **2. Passo a Passo de Execução no Blender 4.5 LTS**

##### **Passo 1: Configuração da Cena e Iluminação**
1. **Adicionar Esferas:** Pressione **`Shift + A` > Mesh > UV Sphere**, crie duas esferas lado a lado e aplique **Shade Smooth** (clique com o botão direito).
2. **Visualização:** Mude a janela para o modo **Rendered View** (**`Shift + Z`** ou pelo menu radial de navegação com a tecla **`Z`**).
3. **Iluminação de Teste:** No painel **World Properties**, certifique-se de ter uma iluminação ambiente ativa (HDRI ou luz do tipo *Sun/Area*) para refletir detalhes nos materiais.

##### **Passo 2: Configuração do Material Dielétrico (Isolante / Plástico)**
1. Selecione a primeira esfera e abra o **Shader Editor**.
2. Crie um novo material e nomeie como **`PBR_Dielectric`**.
3. **Ajuste dos parâmetros no nó `Principled BSDF`:**
   * **`Metallic` = `0.0`**: Define o material como um isolante elétrico (plástico, madeira, cerâmica).
   * **`Base Color`**: Defina a cor desejada (ex.: **Azul**). Em dielétricos, o *Base Color* representa a cor da camada difusa (a cor própria do objeto).
   * **`Specular IOR Level` / `IOR`**: Mantido no valor padrão. A reflexão especular de superfície permanece **incolor (branca)** e reflete entre 2% a 5% da luz incidente.
   * **`Roughness`**: Teste os valores de **`0.1`** (superfície polida/brilhante) até **`0.8`** (superfície fosca).

##### **Passo 3: Configuração do Material Metálico (Condutor / Ouro ou Cobre)**
1. Selecione a segunda esfera e crie um novo material chamado **`PBR_Metallic`**.
2. **Ajuste dos parâmetros no nó `Principled BSDF`:**
   * **`Metallic` = `1.0`**: Elimina a reflexão difusa interna, transformando o objeto em um condutor.
   * **`Base Color`**: Escolha uma cor metálica (ex.: **Amarelo Dourado** ou **Cobre**). Em metais, o *Base Color* passa a ditar a **cor da própria reflexão especular**.
   * **`Roughness`**: Defina **`0.15`** para metal polido ou **`0.5`** para metal escovado.

##### **Passo 4: Experimento Prático da Transição**
1. Na primeira esfera, deslize lentamente o parâmetro **`Metallic`** de **`0.0`** para **`1.0`**.
2. **Observação Esperada:** Note que a iluminação difusa desaparece e a cor do objeto se converte na cor dos reflexos do ambiente. *(Valores intermediários como `0.5` devem ser usados apenas para mapear texturas com desgaste, poeira ou ferrugem sobre metal).*

---

#### **3. Quadro Comparativo de Parâmetros (Blender 4.5 LTS)**

| Propriedade no `Principled BSDF` | Dielétrico (`Metallic = 0.0`) | Metálico (`Metallic = 1.0`) |
| :--- | :--- | :--- |
| **Significado do `Base Color`** | Cor da superfície (difusa) | Cor da reflexão (especular) |
| **Reflexão Difusa** | Presente | Ausente |
| **Cor do Brilho Especular** | Incolor (branca/neutra) | Colorida pelo `Base Color` |
| **Refletância Especular Típica** | Baixa (2% a 5%) | Alta (quase total) |