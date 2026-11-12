---
marp: true
theme: gaia
---

## **Introdução a Rigging**

### Planejamento e criação com Blender 4.5 LTS

- Compreender o papel do rig no processo de animação.
- Identificar as decisões que orientam a construção de uma estrutura articulada.
- Conhecer os componentes de um rig e sua relação com a malha.
- Entender as etapas de criação, teste e revisão no Blender.

---

### **O que é rigging?**

Rigging é o processo de criar uma estrutura de controle para posicionar e animar um personagem ou objeto.

- Um **esqueleto** organiza articulações, pivôs e relações entre partes.
- **Controles** tornam as ações importantes acessíveis ao animador.
- A ligação entre esqueleto e malha permite que as transformações deformem o modelo.
- O rig transforma um modelo estático em um sistema reutilizável de pose e movimento.

Rigging é mais do que criar ossos: envolve planejar, construir, associar, controlar e testar.

---

### **Onde o rig se encaixa na produção?**

**Objetivo e design → modelo → rig → posing e animação → revisão → entrega**

- O desenho e o movimento pretendido orientam a estrutura do rig.
- A topologia e as proporções da malha influenciam as deformações.
- A estrutura de ossos, controles e pesos determina o que pode ser animado.
- Os testes revelam problemas que podem exigir ajustes no modelo ou no rig.

As etapas são interdependentes: é melhor avaliar o rig em poses variadas do que apenas na pose neutra.

---

### **Planejar antes de construir**

Antes de criar a estrutura, defina:

- **Uso:** será animado para cinema, jogo, visualização ou outro contexto?
- **Ações:** que movimentos o personagem ou objeto precisa realizar?
- **Escopo:** quais partes precisam deformar ou receber controles?
- **Usuário do rig:** quem vai animar e que nível de controle é adequado?
- **Restrições de produção:** prazo, desempenho, reutilização e compatibilidade de exportação.
- **Critério de qualidade:** quais poses e movimentos o rig deve suportar?

Um rig deve atender às necessidades do projeto sem adicionar controles desnecessários.

---

### **Preparação do modelo**

Um bom rig começa com uma malha adequada à deformação:

- A topologia deve permitir que articulações dobrem sem colapsar.
- A pose de referência e a orientação do modelo devem ser consistentes.
- Simetria pode facilitar a criação, mas deve ser verificada onde houver diferenças.
- A escala, a origem e a orientação precisam ser consideradas antes da associação.
- Partes que não deformam, como acessórios rígidos, podem exigir outra estratégia de ligação.

Ajustes de modelagem podem ser necessários depois dos primeiros testes de deformação.

---

### **Armature e bones**

- **Armature:** objeto do Blender que contém a estrutura de ossos.
- **Bone:** elemento que define uma articulação, um segmento e seus eixos locais.
- **Head e Tail:** extremidades que estabelecem a posição e a direção do osso.
- **Roll:** orientação dos eixos locais do osso; influencia rotações e controles.
- **Parent:** relação hierárquica que transmite transformações do pai para os filhos.
- **Connected:** opção que mantém o início do osso filho conectado à extremidade do pai.

Parenting e conexão são conceitos relacionados, mas não idênticos.

---

### **Modos e estado do esqueleto no Blender**

- **Object Mode:** posiciona e organiza o objeto Armature na cena.
- **Edit Mode:** define a estrutura e a posição dos ossos na pose de referência.
- **Pose Mode:** transforma os ossos para criar poses e controlar a animação.
- **Rest Position:** exibe a configuração de referência do esqueleto.
- **Pose Position:** exibe o resultado das transformações de pose.

Planejar a pose de referência é importante porque ela serve de base para a deformação da malha.

---

### **Hierarquia e organização**

A hierarquia representa como as partes se relacionam:

- Um osso pai pode controlar um ou mais ossos filhos.
- A cadeia deve refletir as relações necessárias para o movimento.
- A orientação local dos ossos precisa ser coerente com as articulações.
- Nomes consistentes e coleções de ossos facilitam leitura e manutenção.
- Separar ossos de deformação dos ossos de controle ajuda a organizar rigs mais complexos.

No Blender 4.5, **Bone Collections** organizam os ossos do Armature; elas substituem o sistema antigo de Bone Layers.

---

### **Ossos de deformação e controles**

- **Deform bones:** transmitem influência à malha e produzem deformações.
- **Control bones:** são manipulados pelo animador para mover ou orientar partes do rig.
- **Helper bones:** auxiliam na distribuição do movimento ou na qualidade da deformação.
- **Custom Shapes:** formas visuais opcionais que tornam os controles mais fáceis de selecionar.

Em rigs simples, um mesmo osso pode cumprir mais de uma função. Em rigs maiores, separar funções pode tornar o sistema mais claro e previsível.

---

### **FK e IK: duas formas de controlar cadeias**

- **FK (Forward Kinematics):** a transformação dos ossos é conduzida da hierarquia, do pai em direção aos filhos.
- **IK (Inverse Kinematics):** um alvo e parâmetros da cadeia orientam o cálculo das articulações anteriores.
- **FK** oferece controle direto das rotações ao longo da cadeia.
- **IK** facilita posicionar a extremidade de uma cadeia, como mão ou pé.

Não há um método universalmente melhor: a escolha depende da ação e do tipo de controle desejado.

---

### **Constraints e controles**

Constraints podem relacionar ossos e objetos para implementar comportamentos do rig:

- Orientar ou limitar a transformação de um osso.
- Usar um alvo para controlar uma cadeia com IK.
- Copiar ou combinar transformações entre controles e ossos de deformação.
- Fazer um controle influenciar uma parte específica do esqueleto.

Cada constraint deve ter um papel definido. Hierarquia, alvo, espaço de transformação e ordem de avaliação afetam o resultado.

---

### **Associar a malha ao esqueleto**

O vínculo da malha ao Armature permite que as transformações dos ossos afetem seus vértices:

- O **Armature Modifier** avalia a deformação da malha usando o esqueleto.
- **Vertex Groups** associam vértices a grupos nomeados que correspondem a ossos.
- Os **pesos** definem quanto cada osso influencia os vértices.
- Um vértice pode ser influenciado por mais de um osso, distribuindo a deformação.
- Os pesos podem ser criados automaticamente e depois revisados e ajustados.

A associação automática é um ponto de partida, não uma garantia de deformação final correta.

---

### **Skinning e Weight Painting**

Skinning é o processo de associar a malha ao esqueleto e definir como ela se deforma.

- No **Weight Paint Mode**, cores visualizam a influência dos grupos de vértices.
- Pesos baixos indicam menor influência; pesos altos, maior influência.
- As transições de peso afetam áreas como ombros, cotovelos, quadris e joelhos.
- A pintura deve ser avaliada com os ossos em diferentes posições.
- A qualidade depende tanto dos pesos quanto da topologia e da posição dos ossos.

Uma distribuição de pesos adequada reduz estiramentos, interseções e colapsos indesejados.

---

### **Fluxo de criação de um rig**

1. **Definir requisitos:** ações, nível de controle e destino do personagem.
2. **Preparar o modelo:** revisar pose de referência, topologia, escala e organização.
3. **Construir o esqueleto:** posicionar e orientar os ossos essenciais.
4. **Organizar a hierarquia:** estabelecer relações entre ossos e coleções.
5. **Criar controles:** adicionar IK, constraints e formas de controle quando necessários.
6. **Associar e ajustar a malha:** configurar Armature Modifier, grupos e pesos.
7. **Testar e revisar:** avaliar deformações, controles e poses extremas.

O processo é iterativo: testes podem indicar ajustes em qualquer etapa.

---

### **Testar o rig**

Não basta verificar se os ossos se movem. Avalie:

- Poses extremas e transições entre elas.
- Deformação em articulações e áreas de contato.
- Comportamento de mãos, pés, cabeça e partes secundárias.
- Facilidade de selecionar e entender os controles.
- Coerência da hierarquia e ausência de dependências confusas.
- Desempenho e compatibilidade com o fluxo de produção.

Um teste em movimento pode revelar problemas que não aparecem em uma pose estática.

---

### **Recursos do Blender 4.5 LTS**

- **Armature e Bone Properties:** estrutura, relações e propriedades dos ossos.
- **Pose Mode:** manipulação do rig e criação de poses.
- **Bone Collections:** organização dos ossos por função ou região.
- **Constraints:** relações, limites e controles entre objetos ou ossos.
- **Armature Modifier e Vertex Groups:** deformação e associação da malha.
- **Weight Paint Mode:** visualização e edição dos pesos.
- **Dope Sheet e Action Editor:** organização da animação dos controles.

O Blender fornece os componentes do fluxo; a estrutura do rig depende do personagem e das necessidades da produção.

---

### **Automação e rigs reutilizáveis**

- Ferramentas de auto-rigging podem acelerar a geração de estruturas comuns.
- O **Rigify** permite trabalhar com metarigs e gerar rigs, quando a extensão estiver instalada e habilitada.
- A automação reduz trabalho repetitivo, mas não substitui a validação de ossos, controles e pesos.
- A escolha entre um rig manual, gerado ou híbrido depende do escopo e do nível de personalização.

Considere a manutenção, a compatibilidade e a experiência de quem usará o rig.

---

### **Rigging além de personagens**

Os mesmos conceitos podem ser aplicados a:

- Objetos articulados, máquinas e mecanismos.
- Props que precisam ser segurados ou conectados a personagens.
- Caudas, tentáculos e cadeias flexíveis.
- Controles faciais combinando ossos e shape keys.
- Sistemas reutilizáveis para personagens de um mesmo projeto.

A estrutura deve corresponder ao movimento e à forma do elemento, não necessariamente à anatomia humana.

---

### **Síntese: do requisito ao rig validado**

**Ações e destino → modelo e pose de referência → esqueleto e hierarquia → controles → associação e pesos → testes e revisão**

- Planejar o rig a partir das ações que precisa suportar.
- Construir uma hierarquia compreensível e adequada ao modelo.
- Distinguir ossos de deformação, controles e auxiliares quando isso beneficiar o projeto.
- Avaliar pesos e deformações em poses variadas.
- Usar os recursos do Blender 4.5 LTS para organizar, controlar e testar o sistema.
