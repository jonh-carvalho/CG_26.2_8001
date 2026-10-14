### **Roteiro — Fase 3: Modelos Avançados**
#### **3.1 Introdução ao PBR (Physically Based Rendering) — Materiais Dielétricos e Metálicos**

---

##### **1. Fundamentação Teórica**
O modelo **PBR (Physically Based Rendering)** simula o comportamento da luz de acordo com leis e propriedades físicas reais.
* **Conservação de Energia:** Garante que a superfície de um objeto nunca reflita mais luz do que a quantidade incidente que recebe.
* **Parâmetros Principais:** O fluxo de trabalho PBR baseia-se fundamentalmente nos controles de **Metalness** (Metalicidade) e **Roughness** (Rugosidade).
* **Dielétricos vs. Metálicos:**
  * **Dielétricos (Isolantes/Não-metais):** Possuem `Metallic = 0.0`. Apresentam reflexão difusa combinada com um brilho especular suave e neutro.
  * **Metálicos (Condutores):** Possuem `Metallic = 1.0`. Não possuem reflexão difusa interna; a cor refletida é diretamente influenciada pela cor do próprio metal.

---

##### **2. Passo a Passo de Execução no Blender**

###### **Passo A: Criar Material Dielétrico (Plástico Branco)**
1. **Preparar a Esfera:** Selecione ou adicione uma esfera (**`Shift + A` > Mesh > UV Sphere**) e aplique **Shade Smooth**.
2. **Novo Material:** No **Shader Editor**, crie um material chamado **`Dielectric_Plastic`**.
3. **Configurar o Principled BSDF:**
   * **Base Color:** Defina como **Branco** (código Hex `FFFFFF`).
   * **Roughness:** Defina o valor para **`0.4`**.
   * **Specular:** Ajuste o valor para **`0.5`**.
   * **Metallic:** Mantenha o valor em **`0.0`**.

###### **Passo B: Criar Material Metálico (Ouro)**
1. **Preparar a Esfera:** Adicione uma nova esfera ao lado (**`Shift + A` > Mesh > UV Sphere**) e aplique **Shade Smooth**.
2. **Novo Material:** No **Shader Editor**, crie um material chamado **`Metallic_Gold`**.
3. **Configurar o Principled BSDF:**
   * **Base Color:** Defina como **Amarelo escuro** (código Hex `FFDD00`).
   * **Roughness:** Ajuste para **`0.2`**.
   * **Specular:** Mude o valor para **`1.0`**.
   * **Metallic:** Altere o valor para **`1.0`**.

---

##### **3. Exercício Prático**
* **Criação de Galeria de Teste:** Crie 4 esferas para representar plástico, metal, vidro e madeira.
* **Análise de Luz:** Mova a fonte de luz e altere os ângulos de iluminação para comparar como os materiais metálicos e dielétricos reagem à iluminação da cena.
