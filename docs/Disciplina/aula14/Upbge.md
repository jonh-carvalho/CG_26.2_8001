---
marp: true
theme: gaia

---

## **Do Blender para o Motor em Tempo Real**

### **Objetivos da Aula**

- Compreender o fluxo de trabalho Blender → UPBGE
- Dominar a exportação de assets e cenas
- Implementar lógica de jogo usando Logic Bricks e Python
- Otimizar modelos para tempo real


---


#### **Introdução ao UPBGE**

**O que é UPBGE?**

- UPBGE (Uchronia Project Blender Game Engine)
- Fork do BGE oficial mantido pela comunidade
- Integração nativa Blender + Engine de jogo
- Vantagens:
  - Fluxo integrado sem exportação/importação
  - Uso direto de arquivos .blend
  - Desenvolvimento rápido de protótipos

---


#### **Diferenças para Outras Engines:**
- **Unity/Unreal**: Exportação para formatos intermediários
- **UPBGE**: Uso direto do .blend como cena de jogo
- **Workflow**: Tudo dentro do Blender

---

#### **Configuração de Cena para UPBGE**

**Preparando Objetos 3D**

- Conceitos de otimização:
- Low-poly modeling
- UV mapping eficiente
- LOD (Level of Detail)

---


#### **Configurações Essenciais:**
1. **Scene Properties → Scene**
   - **Game Physics**: Habilitar física Bullet
   - **Gravity**: Ajustar para jogo (normalmente -9.8 Z)

---

#### **Configurações Essenciais:**
2. **Object Properties → Physics**
   - **Collision Bounds**: Box, Sphere, Cylinder, Cone
   - **Mass**: Para objetos dinâmicos
   - **Physics Type**: 
     - **Static**: Objetos imóveis
     - **Dynamic**: Objetos com física
     - **Rigid Body**: Corpos rígidos

---


#### **Otimização de Modelos:**
- **Polycount**: Manter baixo para tempo real
- **Materials**: Usar poucos materiais por objeto
- **Textures**: Potências de 2 (256, 512, 1024)

---


#### **Logic Bricks - Lógica Visual**

**Sistema de Logic Bricks:**
- **Sensors**: Detectam eventos (teclado, mouse, colisão)
- **Controllers**: Processam lógica (AND, OR, Python)
- **Actuators**: Executam ações (movimento, animação, som)

---


#### **Exemplo: Controle de Personagem**

Configuração básica de movimento:
- Sensor: Keyboard (W, A, S, D)
- Controller: AND
- Actuator: Motion (Movement/Location)


---

#### **Passo a passo - Personagem Andando:**
1. **Add Sensor → Keyboard** (Tecla W)
2. **Add Controller → And**
3. **Add Actuator → Motion** (Movement Z)
4. **Conectar** Sensor → Controller → Actuator

**Colisão e Interação:**
1. **Sensor → Collision** (detecta colisões)
2. **Sensor → Mouse** (cliques, movimento)
3. **Actuator → Scene** (mudar cena)
4. **Actuator → Sound** (reproduzir áudio)

---


### 3. Scripting com Python no UPBGE

**Acesso à API do UPBGE:**
```python
import bge
from bge import logic
from bge import render

# Objetos principais:
cont = logic.getCurrentController()
own = cont.owner  # Dono do script (objeto)
scene = logic.getCurrentScene()
```

---


**Exemplo: Movimento com Python**
```python
def move_player():
    cont = logic.getCurrentController()
    own = cont.owner
    
    keyboard = logic.keyboard.events
    move_speed = 0.1
    
    # Controles WASD
    if keyboard[bge.events.WKEY]:
        own.applyMovement([0, move_speed, 0], True)
    if keyboard[bge.events.SKEY]:
        own.applyMovement([0, -move_speed, 0], True)
    if keyboard[bge.events.AKEY]:
        own.applyMovement([-move_speed, 0, 0], True)
    if keyboard[bge.events.DKEY]:
        own.applyMovement([move_speed, 0, 0], True)
```

---


## **Configurando Script Python:**
1. **Text Editor** → New Script
2. **Logic Editor** → Add Controller → Python
3. **Module**: nome_do_script
4. **Function**: nome_da_função


---


### **4. Sistema de Animação no UPBGE**

**Action Actuator para Animações:**

Configuração de animações:
- Armature Actions
- Frame ranges
- Blend modes


---


#### **Animação de Personagem:**
1. **Add Actuator → Action**
2. **Action**: Selecionar ação armature
3. **Frame Range**: Definir frames da animação
4. **Blendin**: Suavizar transições


---


#### **Controle por Script:**
```python
def play_animation(anim_name, blend=5):
    cont = logic.getCurrentController()
    act_actuator = cont.actuators[anim_name]
    
    # Configurar blend
    act_actuator.blendin = blend
    
    # Executar animação
    cont.activate(act_actuator)
```

---


### **5. Sistema de Materiais e Shaders**

**Materiais para Tempo Real:**

- **GLSL Materials**: Shaders modernos
- **Texturas**: Diffuse, Normal, Specular
- **Lighting**: Real-time lighting

---

#### **Configuração Básica:**
1. **Material Properties → Use Shaders**
2. **Texture Properties → Type**: Image/Movie
3. **Mapping**: UV/Generated
4. **Influence**: Color/Normal/Specular

---


#### **Shader Nodes (Cycles/EEVEE):**
- Compatibilidade limitada no UPBGE
- Usar materiais simples para melhor performance

---

### **6. Exportação e Build**

**Exportando Projeto:**

# Formatos suportados:
# - .blend (nativo)
# - Executável standalone
# - Android APK (com configuração)


---


#### **Runtime Standalone:**
1. **File → Export → Standalone Runtime**
2. **Platform**: Windows/Linux/macOS
3. **Settings**: Incluir dependências

---

**Configuração para Android:**
1. **Build Android UPBGE**
2. **Export → Android Application**
3. **Permissions**: Definir permissões necessárias

---

### 7. Conceitos de Computação Aplicados

**Otimização de Performance:**
Técnicas importantes:
- Frustum Culling
- Occlusion Culling  
- LOD (Level of Detail)
- Object Pooling


---

#### **Estruturas de Dados para Jogos:**

```python
class GameState:
    def __init__(self):
        self.player = None
        self.enemies = []
        self.collectibles = []
        self.score = 0
        
    def update(self):
        # Atualizar lógica do jogo
        pass
```

---

**Gestão de Cenas:**
```python
def load_scene(scene_name):
    """Carrega uma nova cena"""
    logic.addScene(scene_name)
    
def unload_scene(scene_name):
    """Remove uma cena"""
    logic.endScene(scene_name)
```

---

### **8. Exercícios Práticos**

**Exercício 1: Coletável Simples**
- Objeto com rotação (Logic Bricks)
- Colisão com personagem
- Contador de pontos (Python)

---

### **8. Exercícios Práticos**
**Exercício 2: Inimigo Patrulha**
- Movimento entre waypoints
- Detecção de jogador
- Animação de ataque

---

### **8. Exercícios Práticos**
**Exercício 3: Interface HUD**
- Texto para pontuação
- Barra de vida
- Menu pause

---

### **10. Boas Práticas e Troubleshooting**

**Otimização:**
- **Polycount**: < 10k triângulos por cena
- **Texturas**: Usar atlas de texturas
- **Física**: Simplificar collision shapes
- **Scripts**: Evitar loops infinitos

---


**Debugging:**
```python
# Ferramentas de debug:
print("Debug info:", variable)

# Console do jogo (Pressione ~ ingame)
# Visualizador de física (Visualizar bounds)
```

---


#### **Problemas Comuns:**
- **Performance**: Verificar polycount e scripts
- **Colisões**: Ajustar collision bounds
- **Animação**: Checar action names e frames
- **Scripts**: Verificar imports e sintaxe

---


### 11. **Recursos e Extensões**

**Bibliotecas Úteis:**
- **BLF**: Para renderização de texto
- **BGE Audio**: Sistema de áudio
- **BGE Render**: Controle de renderização


---


#### **Add-ons Recomendados:**
- **BGE Power Sequencer**: Para cutscenes
- **BGE Particle Systems**: Partículas avançadas
- **BGE Network**: Para multiplayer

---
 