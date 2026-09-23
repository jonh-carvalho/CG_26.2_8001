Exemplo preenchido do **Relatório Curto** e da **Storyboard** para a **AP1**. Este modelo serve de guia prático e inspirador para entenderem como estruturar a narrativa, justificar as escolhas de modelagem e atender rigorosamente a todos os requisitos técnicos exigidos nas diretrizes da avaliação.


#  Relatório Técnico e Planejamento Visual: “Ibmec em 15 segundos”

**Aluno(a):** Lucas Andrade Silva  
**Matrícula:** 2023081234  
**Curso / Turma:** Ciência da Computação / Computação Gráfica  
**Versão do Software:** Blender 4.5 LTS  
**Nome do Arquivo .blend:** `AP1_LucasSilva.blend`  

## PARTE 1: RELATÓRIO CURTO

### 1. Título da Peça e Conceito Geral
* **Título da Peça:** *Ibmec: O Portal do Futuro e da Inovação*
* **Conceito Visual:** A composição estática representa um ambiente de descoberta acadêmica e tecnológica, fundamentado nos pilares de solidez, futuridade e empreendedorismo. A cena constrói a ideia de um "portal de conhecimento" no qual a marca é o centro de atração e transformação, conectando a base acadêmica sólida ao mercado do futuro.

### 2. Narrativa e Destaque da Marca Ibmec
* **Apresentação da Marca:** A palavra **Ibmec** foi posicionada no centro geométrico da cena sobre uma plataforma em pódio, servindo como ponto focal de convergência da composição e mantendo total legibilidade e integridade visual de seu estilo e proporção.
* **Ideia de Transformação:** A cena sugere que a marca **Ibmec** surge a partir da ativação de um portal circular de inovação ao seu redor. Na animação futura da AP2, os anéis geométricos irão girar e se alinhar, projetando feixes de energia e revelando a marca com solidez e impacto visual.

### 3. Os Três Objetos Autorais
A composição contém **exatamente três objetos autorais** desenvolvidos a partir do zero no Blender, devidamente identificados e justificados:

1. **Objeto Autoral 1:** `Obj_PodioFuturista`
   * **Função na Cena:** Plataforma poligonal em degraus que eleva a palavra **Ibmec**, simbolizando a base sólida do conhecimento e a ascensão profissional do estudante.
   * **Modo de Construção:** Modelado do zero a partir de uma primitiva de cubo com aplicação de extrusões (*Extrude*), inserção de faces (*Inset*) e chanfros (*Bevel*) nas arestas.

2. **Objeto Autoral 2:** `Obj_PortalInovacao`
   * **Função na Cena:** Estrutura anelar externa que emoldura a palavra, representando a passagem para o futuro, a tecnologia e a inovação aberta.
   * **Modo de Construção:** Construído a partir de um cilindro oco combinado com os modificadores *Solidify* (para dar espessura de malha) e *Bevel* (para suavização das quinas).

3. **Objeto Autoral 3:** `Obj_TrofeuMarco`
   * **Função na Cena:** Um marco geométrico posicionado na lateral do pódio, representando a conquista, a liderança e o espírito empreendedor.
   * **Modo de Construção:** Gerado a partir do desenho autoral de uma curva paramétrica de Bézier e aplicação do modificador de revolução *Screw* ao longo do eixo vertical.

---

### 4. Técnicas de Modelagem e Transformações Geométricas
* **Técnicas de Modelagem Utilizadas:** Foram aplicados recursos de **extrusão (*Extrude*)**, **inserção de faces (*Inset*)**, **chanframento de arestas (*Bevel*)**, **modelagem por curvas paramétricas de Bézier** e os **modificadores *Solidify* e *Screw***.
* **Transformações Geométricas:** Aplicou-se translação, rotação e escala conscientes em todos os elementos para garantir o equilíbrio visual da regra dos terços. Todas as transformações foram congeladas (`Ctrl + A > All Transforms`), mantendo a escala padronizada em `1.0` e rotações zeradas.

---

### 5. Organização Técnica da Cena
* **Estrutura de Coleções:** Todos os elementos da cena estão rigorosamente agrupados dentro da coleção principal denominada **`AP1_Ibmec_Conceito`** no Outliner.
* **Configuração da Câmera:** A câmera principal (`Cam_Principal_AP1`) foi posicionada com um enquadramento frontal em perspectiva, focando diretamente na marca.
* **Linha do Tempo Planejada:** A duração da cena foi definida na *Timeline* para **360 frames** a **24 fps**, totalizando exatamente **15 segundos**.

---

### 6. Plano Resumido para a AP2 (Evolução da Cena)
Para a segunda etapa do projeto (AP2), estão planejadas as seguintes etapas:
* **Animação por Keyframes:** Animação de rotação contínua do anel `Obj_PortalInovacao` (360° em 15 segundos) e movimento suave de subida (*truck-up*) da câmera `Cam_Principal_AP1`.
* **Iluminação e Materiais:** Aplicação de material metálico escovado no pódio, material emissivo de néon no portal e iluminação de três pontos (*Three-Point Lighting*).
* **Renderização Final:** Exportação do vídeo final de 15 segundos renderizado pelo motor **Eevee**.

---

## PARTE 2: STORYBOARD (PLANEJAMENTO AUDIOVISUAL DE 15 SEGUNDOS)

A storyboard a seguir divide a narrativa de 15 segundos em **três momentos principais**:

```
+-----------------------------------------------------------------------------------+
| QUADRO 1: ABERTURA E SURGIMENTO DO PORTAL (0s a 3s | Frames 1 a 72)               |
+-----------------------------------------------------------------------------------+
| [Imagem do Viewport em Solid Mode exibindo o enquadramento amplo e inicial]       |
|                                                                                   |
| • Ação/Movimento: A câmera inicia aproximando-se lentamente do cenário.          |
| • Elementos em Destaque: O pódio `Obj_PodioFuturista` e a base da marca surgem.   |
| • Foco do Áudio/Visual: Estabelecimento do espaço 3D e da atmosfera da cena.     |
+-----------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------+
| QUADRO 2: ATIVAÇÃO E REVELAÇÃO DA MARCA (3s a 10s | Frames 73 a 240)              |
+-----------------------------------------------------------------------------------+
| [Imagem do Viewport destacando o portal e a palavra Ibmec centralizada]           |
|                                                                                   |
| • Ação/Movimento: O anel `Obj_PortalInovacao` completa sua rotação rápida.        |
| • Elementos em Destaque: A palavra Ibmec atinge o centro do enquadramento.        |
| • Foco do Áudio/Visual: Clímax visual com iluminação focada na palavra principal.  |
+-----------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------+
| QUADRO 3: FIXAÇÃO E ENCERRAMENTO (10s a 15s | Frames 241 a 360)                   |
+-----------------------------------------------------------------------------------+
| [Imagem do Viewport no enquadramento final estático e perfeitamente legível]      |
|                                                                                   |
| • Ação/Movimento: A câmera desacelera até travar na posição final.                |
| • Elementos em Destaque: A palavra Ibmec permanece em destaque total e estática.  |
| • Foco do Áudio/Visual: Encerramento elegante garantindo a leitura limpa da marca.|
+-----------------------------------------------------------------------------------+
```
