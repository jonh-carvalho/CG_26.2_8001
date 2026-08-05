## Esqueleto Digital e Movimento

- Compreender o conceito de rigging e sua importância na animação
- Aprender a criar uma estrutura óssea (armature) básica
- Dominar técnicas de skinning (associação da malha ao esqueleto)
- Criar poses e animação simples de personagem

### **Fundamentos do Rigging**

**O que é Rigging?**

Esqueleto digital: 

> Estrutura hierárquica de ossos virtuais (armature) e controladores que simulam articulações e pivôs de um personagem/objeto. Conectado à malha por skinning (vertex groups e pesos), o esqueleto transmite suas transformações aos vértices, permitindo posing e animação consistentes sem alterar a geometria. Suporta FK/IK, constraints e limites, oferecendo controle preciso e reutilizável do movimento.

- Analogia com marionetes e sistema ósseo humano

- Componentes principais:
    - Armature: 
    
    > Estrutura hierárquica de ossos que funciona como o “esqueleto” do personagem/objeto; define juntas e pivôs, organiza a cinemática e, via Armature Modifier e Vertex Groups, transmite transformações à malha; é construída em Edit Mode e controlada em Pose Mode.
    
    - Bones: 
    
    > Ossos individuais que compõem a armature; cada bone tem head, tail e eixos locais; suportam relações pai–filho, constraints e limites.
    
    - Vertex Groups: 
    > Grupos de vértices nomeados que mapeiam para bones; usados pelo Armature Modifier para distribuir influência de deformação.
    
    - Weight Painting:
    
    > Processo de atribuição e edição visual dos pesos (0–1) que definem quanto cada osso influencia os vértices da malha; cores indicam intensidade (azul = 0, vermelho = 1); exige normalização dos pesos por vértice para deformações limpas

**Hierarquia e Relacionamentos**

- Cadeia cinemática (IK vs FK)
    
    >**FK** (Forward Kinematics): Animação hierárquica onde a transformação dos ossos pais afeta os filhos.

    >**IK** (Inverse Kinematics): Animação onde a posição final de um osso determina a posição dos ossos anteriores na cadeia.

- Bone parenting e herança de transformações
    
    > Osso pai → Osso filho
    
    > Osso filho → Osso pai

- Controladores e constraints
    
    > Controladores: Objetos auxiliares para facilitar a manipulação de bones.
    
    > Constraints: Restrições aplicadas aos bones para limitar movimentos (ex.: limitar rotação, seguir caminho).

### **Criando um Rig Básico**

**Preparação do Modelo**

1. Importar/ criar personagem simples
2. Verificar topologia da malha
3. Posicionar no centro do mundo (0,0,0)

**Criando a Armature**

Conceitos computacionais:

- Estruturas hierárquicas
- Transformações relativas
- Sistemas de coordenadas aninhadas


**Passo a passo:**

1. **Add → Armature**
2. **Edit Mode**: Extrudar bones para pernas, braços, torso
3. **Naming convention**: 
   - L_UpperArm, R_UpperArm
   - Spine, Head, Hips
4. **Pose Mode**: Testar rotações básicas

**Skinning - Associando Malha ao Esqueleto**

1. Selecionar malha → Shift selecionar armature
2. **Ctrl + P → With Automatic Weights**
3. **Weight Painting Mode**: Ajustar influências
   - Azul (0 influência) → Vermelho (100% influência)

### **Animação com Rig**

**Princípios de Posing**

- Linha de ação
- Contraposto
- Peso e balanceamento

**Criando Animação Walk Cycle**

Ciclo de caminhada - Frames chave:

- 0: Contact (pé atrás)
- 6: Passing (pé médio)
- 12: Contact (pé frente)
- 18: Passing (pé médio)
- 24: Volta ao frame 0


**Passo a passo:**
1. **Pose Mode** selecionar bones
2. **Frame 1**: Pose inicial
3. **I → LocRot** (Location + Rotation)
4. **Frame 12**: Pose oposta
5. **I → LocRot**
6. **Graph Editor**: Suavizar curvas de animação

### 3. Técnicas Avançadas de Rigging

**Inverse Kinematics (IK) vs Forward Kinematics (FK)**
- **FK**: Animação hierárquica (pai → filho)
- **IK**: Alvo final define posição da cadeia

**Configurando IK:**
1. **Add → Bone** (alvo IK)
2. **Bone Constraints → Inverse Kinematics**
3. **Chain Length**: Definir quantos bones são afetados

**Control Rig e Auto-Rigging**
- **Rigify**: Add-on para rigs complexos
- **Bone Layers**: Organização de controls
- **Custom Shapes**: Formas visuais para controls

### 4. Conceitos de Computação Aplicados

**Estruturas de Dados**
```python
# Exemplo conceitual de estrutura bone:
class Bone:
    def __init__(self):
        self.name = ""
        self.parent = None
        self.children = []
        self.local_matrix = Matrix()
        self.global_matrix = Matrix()
```

**Algoritmos**
- **DFS (Depth-First Search)**: Para calcular transformações hierárquicas
- **Interpolação esférica**: Para rotações de quaternion
- **Skinning linear**: Cálculo de vértices baseado em pesos

**Otimização**
- LOD (Level of Detail) para rigging
- Caching de animações
- Bake de physics para performance

### 5. Exercícios Práticos

**Exercício 1: Rig de Braço Simples**
- 3 bones: upper arm, forearm, hand
- Testar FK vs IK
- Animar movimento de "acenar"

**Exercício 2: Facial Rigging**
- Bones para expressões faciais
- Shape keys para morph targets
- Animar fala simples

**Exercício 3: Rig Completo Humanoide**
- Torso, pernas, braços, cabeça
- Sistema IK para pernas
- Controls para animador

### 6. Boas Práticas e Troubleshooting

**Problemas Comuns:**
- **Mesh distortion**: Ajustar weight painting
- **Gimbal lock**: Usar quaternions
- **Scale issues**: Aplicar transformações

**Workflow Eficiente:**
1. Modelar em T-pose
2. Criar armature
3. Weight painting
4. Configurar IK/FK
5. Criar controls
6. Animar


### 8. Recursos e Ferramentas

**Add-ons Úteis:**
- Rigify (auto-rigging)
- Auto-Rig Pro
- MHX Runtime

**Tutoriais Recomendados:**
- "Human Meta-Rig" com Rigify
- "Facial Rigging with Shape Keys"
- "Game Character Pipeline"
