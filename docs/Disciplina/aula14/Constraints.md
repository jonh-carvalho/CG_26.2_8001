---
marp: true
theme: gaia
---

## **Introdução a Constraints**

### Planejamento e criação com Blender 4.5 LTS

- Compreender como constraints definem relações e regras entre elementos da cena.
- Identificar decisões de planejamento antes de adicionar uma constraint.
- Reconhecer os principais tipos e aplicações no Blender.
- Avaliar como constraints se combinam com hierarquias, keyframes e simulações.

---

### **O que é uma constraint?**

Uma constraint é uma regra que influencia a transformação ou o comportamento de um objeto ou osso, com base em valores, alvos ou relações definidos na cena.

- Pode controlar posição, rotação, escala, orientação ou relação com outro elemento.
- É avaliada pelo Blender durante a atualização da cena.
- Pode ser ajustada sem alterar diretamente a geometria do objeto.
- É útil para automatizar relações que seriam trabalhosas ou inconsistentes de animar manualmente.

> Uma constraint não é, por si só, uma simulação física.

---

### **Por que usar constraints?**

- **Consistência:** manter uma relação entre elementos ao longo da animação.
- **Controle:** restringir transformações ou orientar um elemento a partir de outro.
- **Reutilização:** criar controles que podem ser ajustados sem refazer todos os keyframes.
- **Coordenação:** relacionar objetos, câmeras, luzes e ossos de um rig.
- **Eficiência:** reduzir animação repetitiva e facilitar mudanças no projeto.

O benefício depende de uma relação clara e de uma estrutura bem planejada.

---

### **Constraints, parenting, keyframes e física**

- **Keyframes:** registram valores em instantes e descrevem mudanças no tempo.
- **Parenting:** estabelece uma hierarquia em que um elemento herda transformações do pai.
- **Constraints:** aplicam regras e relações avaliadas na cena; podem depender de alvos ou propriedades.
- **Simulações:** calculam comportamento segundo parâmetros e condições físicas.
- **Rigid Body Constraint:** conecta ou limita corpos rígidos dentro do sistema de física.

Esses recursos podem ser combinados, mas resolvem problemas diferentes. Escolha pelo comportamento desejado, não apenas pelo nome da ferramenta.

---

### **Planejar antes de criar**

Defina primeiro:

- **Intenção:** qual relação ou comportamento deve ser automatizado?
- **Elemento controlado (Owner):** qual objeto ou osso receberá a constraint?
- **Alvo (Target):** de que objeto, osso ou dado virá a referência, se necessário?
- **Propriedade afetada:** posição, rotação, escala, orientação, trajetória ou outra relação?
- **Grau de controle:** o comportamento é fixo, animável ou parcialmente influenciado?
- **Critério de sucesso:** como saber se a relação funciona em todos os momentos relevantes?

Um planejamento claro evita dependências desnecessárias e facilita a revisão.

---

### **Owner, Target e Subtarget**

- **Owner:** objeto ou osso ao qual a constraint está aplicada.
- **Target:** elemento usado como referência por constraints que dependem de um alvo.
- **Subtarget:** osso ou elemento específico dentro do objeto-alvo, quando aplicável.
- **Influence:** controla quanto a constraint participa do resultado, quando esse controle está disponível.

Exemplo conceitual: uma câmera pode usar um objeto como alvo para orientar sua direção. A câmera é o Owner; o objeto observado é o Target.

---

### **Como escolher uma família de constraints**

Pense no resultado pretendido:

- **Copiar ou limitar transformações:** manter valores iguais ou dentro de limites.
- **Orientar ou mirar:** direcionar um objeto ou osso para um alvo.
- **Seguir uma trajetória:** relacionar a posição ou orientação a uma curva.
- **Criar uma relação hierárquica ajustável:** vincular transformações com possibilidade de compensação.
- **Controlar deformações ou relações de rig:** mapear valores e coordenar partes articuladas.

A mesma cena pode exigir mais de uma constraint, mas cada uma deve ter uma função compreensível.

---

### **Exemplos de constraints no Blender**

- **Copy Location / Copy Rotation / Copy Scale:** copiar componentes de transformação.
- **Copy Transforms:** copiar a transformação de um alvo.
- **Limit Location / Limit Rotation / Limit Scale:** restringir valores ou eixos.
- **Track To / Damped Track / Locked Track:** orientar um elemento em relação a um alvo.
- **Child Of:** estabelecer uma relação semelhante à de uma hierarquia, com controle de influência e compensação.
- **Follow Path:** relacionar o movimento a uma curva.
- **Transform:** mapear valores de transformação de uma faixa de entrada para uma faixa de saída.

Os nomes e opções específicos dependem do tipo de constraint e de ela estar em um objeto ou osso.

---

### **Constraints de objetos e de ossos**

- **Constraints de objeto** afetam a transformação avaliada do objeto na cena.
- **Constraints de osso** atuam sobre ossos, geralmente como parte de um rig.
- Restrições em ossos podem usar outros ossos como alvos e coordenar cadeias articuladas.
- **Inverse Kinematics (IK)** é uma constraint usada para calcular a pose de uma cadeia a partir de um alvo e de parâmetros do rig.
- A escolha entre objeto e osso depende de qual elemento precisa ser controlado.

Uma constraint não substitui o planejamento do rig: hierarquia, pivôs e controles continuam importantes.

---

### **Transformações, eixos e espaços**

O resultado depende de como o Blender interpreta a transformação:

- **Eixos:** escolha quais componentes devem ser afetados ou ignorados.
- **Espaço do Owner e do Target:** determina como as transformações são interpretadas.
- **Espaços comuns:** World, Local e, em rigs, espaços relacionados à pose.
- **Offsets:** preservam ou ajustam diferenças entre a transformação original e a relação aplicada.
- **Ordem:** constraints são avaliadas em sequência; uma pode alterar o resultado usado pela seguinte.

Confirme os espaços e a ordem sempre que o comportamento parecer inesperado.

---

### **Influência e animação**

- A influência permite combinar o efeito da constraint com a transformação base, quando disponível.
- Ela pode ser constante ou animada para fazer uma relação entrar ou sair gradualmente.
- Mudanças de influência podem representar, por exemplo, a transição de um objeto entre estar preso a um controle e mover-se livremente.
- A animação pode também alterar propriedades do alvo ou os parâmetros da própria constraint.

Planeje a transição para evitar saltos, mudanças involuntárias ou perda de controle.

---

### **Dependências e ordem de avaliação**

Constraints criam relações de dependência entre elementos:

- Um objeto controlado pode depender de um alvo.
- O alvo pode, por sua vez, depender de outro objeto ou osso.
- A ordem das constraints afeta a transformação final.
- Relações circulares podem produzir avisos ou resultados inesperados.
- Dependências longas tornam a cena mais difícil de compreender e depurar.

Prefira uma estrutura simples, com dependências claras e sem ciclos.

---

### **Fluxo de planejamento e criação**

1. **Descrever o comportamento** em termos visuais: o que deve seguir, mirar, copiar ou limitar?
2. **Escolher Owner e Target** e organizar previamente a hierarquia necessária.
3. **Selecionar a constraint** que corresponde à relação pretendida.
4. **Definir eixos, espaços, offsets e influência** conforme o resultado desejado.
5. **Combinar com keyframes ou controles** quando a relação precisar variar no tempo.
6. **Revisar a cena em diferentes poses e momentos**, inclusive os casos extremos.
7. **Simplificar e documentar a estrutura** para facilitar ajustes futuros.

---

### **No Blender 4.5 LTS**

As constraints de objetos e ossos são configuradas no contexto de **Constraints** das propriedades do elemento selecionado:

- O **Constraint Stack** mostra a sequência de constraints aplicada ao Owner.
- Os campos de **Target** e **Subtarget** definem referências externas, quando necessárias.
- Os parâmetros exibidos variam conforme a constraint selecionada.
- Controles de eixos, espaços, offsets e influência ajustam o comportamento quando disponíveis.
- A visualização da cena e a reprodução da animação ajudam a avaliar o resultado ao longo do tempo.

O Blender oferece constraints de transformação, tracking, relacionamento, modificação e motion tracking; a disponibilidade depende do contexto de objeto, osso e dados da cena.

---

### **Constraints e simulação física**

É importante distinguir conceitos com nomes semelhantes:

- **Object Constraints:** regras aplicadas a objetos ou ossos, avaliadas no sistema de dependências da cena.
- **Rigid Body Constraint:** restrição física entre corpos rígidos, como uma articulação ou um elo.
- **Rigid Body, Cloth e outros sistemas físicos:** simulam comportamento segundo propriedades, colisões e forças.
- **Keyframes:** podem definir condições iniciais, controles ou movimentos combinados com uma simulação.

Uma produção pode combinar esses recursos, mas simulação, constraint de objeto e constraint de corpo rígido não são sinônimos.

---

### **Revisão: a relação está funcionando?**

Verifique:

- O Owner correto está sendo afetado?
- O Target e o Subtarget correspondem ao elemento esperado?
- Os eixos e espaços produzem o comportamento pretendido?
- A ordem da pilha está adequada?
- A relação funciona em diferentes posições, poses e quadros?
- Existem saltos, ciclos de dependência ou controles difíceis de ajustar?
- A constraint realmente simplifica a cena em vez de adicionar complexidade?

---

### **Aplicações em produção**

- **Câmera observando um alvo:** orientação vinculada a um personagem ou objeto.
- **Objeto preso a um controle:** vínculo ajustável durante uma animação.
- **Elemento percorrendo uma curva:** movimento relacionado a uma trajetória.
- **Rig de personagem:** controle de membros e coordenação de ossos.
- **Limites de movimento:** evitar rotações ou deslocamentos fora da faixa permitida.
- **Relações entre controles:** conectar valores para criar sistemas de animação consistentes.

São exemplos de intenção; a configuração adequada depende da estrutura e do resultado desejado.

---

### **Síntese**

**Intenção → Owner e Target → tipo de relação → espaços e parâmetros → ordem e animação → revisão**

- Constraints descrevem relações, não substituem o planejamento da cena.
- A escolha depende do comportamento que se deseja automatizar.
- Hierarquia, eixos, espaços, influência e ordem afetam o resultado.
- Separar constraints de objeto, constraints físicas e simulações evita confusão.
- No Blender 4.5 LTS, a pilha e as propriedades permitem inspecionar e ajustar essas relações.
