Aqui está o **roteiro prático do módulo 3.2 — Transparência e Refração (Vidro e Água)** para o Blender 4.5 LTS:

---

### **Roteiro — Fase 3: Modelos Avançados**
#### **3.2 Materiais Especiais — Transparência e Refração (Vidro e Água)**

---

##### **1. Fundamentação Teórica**
Materiais translúcidos e transparentes permitem que a luz atravesse a sua estrutura interna, sofrendo o fenômeno da **refração** (desvio da trajetória do raio luminoso ao mudar de meio físico).

* **Transmission (Transmissão):** Controla a quantidade de luz que passa através da superfície. Em materiais 100% transparentes, o valor é **`1.0`**.
* **IOR (Index of Refraction / Índice de Refração):** Define a intensidade do desvio da luz ao entrar no objeto.
  * **Ar:** `1.000` (sem desvio)
  * **Água:** `1.333`
  * **Vidro Comum:** `1.450` a `1.520`
  * **Diamante:** `2.417`

---

##### **2. Passo a Passo de Execução no Blender 4.5 LTS**

###### **Passo A: Criar Material de Vidro Límpido**
1. **Adicionar Objeto:** Pressione **`Shift + A` > Mesh > Monkey** (a *Suzanne* é ideal para observar a refração devido à sua geometria complexa) e aplique **Shade Smooth**.
2. **Criar Material:** No **Shader Editor**, crie um material e nomeie como **`PBR_Glass`**.
3. **Ajustes no nó `Principled BSDF`:**
   * **`Base Color`:** Branco puro (`FFFFFF`) para vidro transparente incolor.
   * **`Metallic`:** **`0.0`** (dielétrico).
   * **`Roughness`:** **`0.0`** (superfície perfeitamente lisa/brilhante).
   * **`Transmission Weight`:** Aumente para **`1.0`** (torna a estrutura totalmente transmissiva).
   * **`IOR`:** Defina como **`1.450`** (ou `1.500`).

###### **Passo B: Criar Material de Água**
1. Selecione um objeto e crie um material chamado **`PBR_Water`**.
2. **Ajustes no nó `Principled BSDF`:**
   * **`Base Color`:** Azul-piscina extremamente claro ou branco neutro.
   * **`Metallic`:** **`0.0`**.
   * **`Roughness`:** **`0.0`**.
   * **`Transmission Weight`:** **`1.0`**.
   * **`IOR`:** Defina exatamente como **`1.333`**.

---

##### **3. Configurações de Motor de Render (Cycles vs. EEVEE)**

* **No Cycles (Fisicamente Preciso):** A transparência e a refração funcionam **automaticamente** ao ajustar o `Transmission` e o `IOR`.
* **No EEVEE (Renderização em Tempo Real):**
  1. Vá em **Properties > Render Properties** e ative a opção **Raytracing / Screen Space Refractions**.
  2. Vá em **Properties > Material Properties > Settings** do material e marque a caixa **Screen Space Refraction**.

---

##### **4. Tabela de Referência Rápida de IOR**

| Material | Valor de IOR Recomendado | Roughness Indicado |
| :--- | :--- | :--- |
| **Água** | `1.333` | `0.00` |
| **Gelo** | `1.309` | `0.05` - `0.15` |
| **Vidro Comum** | `1.450` - `1.500` | `0.00` |
| **Vidro Jateado / Fosco** | `1.450` | `0.25` - `0.40` |
| **Acrílico / Cristal** | `1.491` | `0.00` |
| **Diamante** | `2.417` | `0.00` |

---

🔍 **Sugestão:** Gostaria de montar um checklist da **Fase 4 (Iluminação de Estúdio com 3 Pontos)** para destacar as sombras e reflexos nesses materiais que você criou?