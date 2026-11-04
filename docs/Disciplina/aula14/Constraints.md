---
marp: true
theme: gaia
---

## Constraints e Simulação Física

- Compreender o conceito de constraints e sua aplicação em animação
- Dominar o uso de simuladores físicos no Blender
- Automatizar movimentos usando princípios físicos reais
- Integrar animação keyframe com simulação física

---

### **Teoria - Constraints Físicas**

**O que são Constraints?**

- Definição: Restrições que automatizam relações entre objetos
- Analogia: "Regras do mundo real" aplicadas a objetos 3D
- Vantagens:
    - Animação mais realista
    - Redução de trabalho manual
    - Possibilidade de simulações complexas

---

### **Tipos de Constraints:**

- **Transform Constraints**: Limitação de movimento/rotação/escala
- **Tracking Constraints**: Seguimento de alvos
- **Relationship Constraints**: Pivot, hinge, spring
- **Simulation Constraints**: Physics, cloth, rigid body

---

### **Constraints de Transformação**

**Constraint "Copy Location"**

Conceito: Objeto A copia posição do Objeto B

- Aplicação: Câmera seguindo personagem

---

### **Passo a passo:**

1. Criar esfera (personagem) e cubo (câmera)
2. Selecionar cubo → Properties → Constraints
3. **Add Constraint → Copy Location**
4. **Target**: Esfera
5. Testar animação da esfera

---

### **Constraint "Track To"**

- Olhar sempre direcionado a alvo
- Aplicação: Olhos seguindo objeto, luzes spotlight

---

### **Constraint "Limit Distance"**

- Manter distância específica entre objetos
- Aplicação: Satélite orbitando planeta

---

### **Simulação Física - Rigid Body**

**Configurando Corpos Rígidos**

Conceitos físicos:
- Massa e inércia
- Colisões e bounding boxes
- Gravidade e forças

---

### **Cenário: Queda de Objetos**

1. **Plano** como chão
2. **Cubo** como objeto que cai
3. **Propriedades Físicas** → **Rigid Body**
      - Tipo: Active (objeto ativo) vs Passive (estático)
4. **Play Animation** para simular física

---

### **Ajustando Parâmetros Físicos:**

- **Mass**: Massa do objeto
- **Friction**: Atrito com superfícies
- **Bounce**: Elasticidade nas colisões
- **Collision Shape**: Forma da colisão (Box, Sphere, Mesh)

---

### **3. Constraints Avançadas e Aplicações**

**Constraint "Child Of"**

- Herança de transformações parentais
- Aplicação: Personagem segurando objeto

---

### **Constraint "IK (Inverse Kinematics)"**

- Alvo define posição final da cadeia
- Aplicação: Pés fixos no chão durante caminhada

---

### **Constraint "Clamp To"**

- Movimento restrito a curva
- Aplicação: Trem em trilhos, planeta em órbita

---

### **Constraint "Transform"**

- Mapear transformações entre objetos
- Aplicação: Controles customizados para animação

---

### **4. Sistema de Partículas com Física**

**Chuva com Gravidade**

1. **Add → Particle System**
2. **Emit From**: Faces ou vértices
3. **Physics Type**: Newtonian
4. **Force Fields**: Gravidade, vento
5. **Ajustar**: Velocidade, vida útil, tamanho

---

### **Cabelo/Erva com Physics**

1. **Particle System → Hair**
2. **Physics → Enable**
3. **Ajustar**: Elasticidade, amortecimento
4. **Forças externas**: Vento, colisões


---

### **5. Simulação de Tecidos (Cloth)**

**Bandeira Ondulando**

Conceitos:

- Malha deformável
- Constraints de vértices
- Forças aerodinâmicas

---

### **Configuração:**

1. **Plano** como tecido
2. **Physics → Cloth**
3. **Vértice fixo**: Selecionar vértice → Pin
4. **Força de vento**: Effector → Wind
5. **Collision**: Objetos que interagem com tecido

---

### **Parâmetros do Cloth:**

- **Quality**: Precisão da simulação
- **Mass**: Massa do tecido
- **Stiffness**: Rigidez do material
- **Damping**: Amortecimento do movimento

---

### **6. Integração com Animação Keyframe**

**Baking de Física para Keyframes**

1. Executar simulação física
2. **Object → Rigid Body → Bake to Keyframes**
3. **Ajustar**: Timing e suavização
4. **Combinação**: Física + animação manual

---

### **Exemplo: Personagem Jogando Bola**

1. Animação manual: Braço arremessando
2. Física: Trajetória da bola após soltar
3. Constraints: Mão segurando bola → soltar no frame X

---

### **7. Conceitos de Computação Aplicados**

**Algoritmos de Simulação**
Pseudocódigo - Verlet Integration (física de partículas)

```python
def verlet_integration(position, old_position, acceleration, dt):
    new_position = 2 * position - old_position + acceleration * dt * dt
    old_position = position
    return new_position, old_position
```

---

### **Estruturas de Dados**

- **Constraint Graph**: Grafo de dependências entre objetos
- **Collision Matrix**: Detecção de colisões
- **Force Accumulator**: Soma de forças aplicadas

---

### **Otimização**

- **Time Stepping**: Subdivisão do tempo para estabilidade
- **Broad/Narrow Phase**: Detecção eficiente de colisões
- **Spatial Partitioning**: Octrees para otimização espacial

---

### **8. Exercícios Práticos**

**Exercício 1: Pêndulo Duplo**

- Constraints: Hinge (pivô)
- Física: Gravidade e inércia
- Visualização: Curva caótica do movimento

---

### **Exercício 2: Dominó em Cadeia**

- Rigid Body com colisões
- Constraints de posição inicial
- Efeito dominó com física

---

###**Exercício 3: Personagem com Capa**
- Cloth simulation como capa
- Collision com corpo do personagem
- Animação combinada: movimento + física

---

### **10. Troubleshooting e Boas Práticas**

**Problemas Comuns:**

- **Tremulação**: Aumentar qualidade da simulação
- **Interpenetração**: Ajustar collision margins
- **Instabilidade**: Reduzir time step

---

### **Workflow Recomendado:**
1. Prototipar com baixa qualidade
2. Ajustar parâmetros principais
3. Refinar detalhes
4. Bake para keyframes (se necessário)
5. Polir animação resultante

---

### **11. Recursos e Ferramentas**

**Add-ons Úteis:**

- **Physical Starlight**: Sistema solar realista
- **Cell Fracture**: Quebra realista de objetos
- **Dynamic Paint**: Pintura dinâmica com física

---

### **Tutoriais Recomendados:**
- "Rigid Body Destruction"
- "Cloth Simulation for Beginners"
- "Physics Constraints for Game Assets"