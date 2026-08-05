---
marp: true
theme: gaia
class: invert
paginate: true
headingDivider: 2
footer: "Transformações Geométricas - Computação Gráfica"
style: |
  section {
    font-family: 'Fira Sans', sans-serif;
  }
  img {
    filter: drop-shadow(0 0 8px rgba(255,255,255,0.2));
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

<!-- _class: lead -->
# ![w:200](https://upload.wikimedia.org/wikipedia/commons/3/3a/Linear_subspaces_with_shading.svg)  
# Transformações Geométricas
### Fundamentos para Modelagem 2D/3D

![bg right:40%](https://images.unsplash.com/photo-1620641788421-7a1c342ea42e?auto=format&fit=crop&w=800)

---

### **Por que Transformações?**
#### Operações essenciais em CG:

1. **Posicionamento** de objetos na cena
2. **Animações** (translação, rotação, escala)
3. **Projeções** (3D → 2D)
4. **Hierarquia** de objetos (ex: braço robótico)

```mermaid
graph TD
    A[Objeto Original] --> B[Transformação]
    B --> C[Objeto Transformado]
```

![bg right:40%](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/2D_affine_transformation_matrix.svg/800px-2D_affine_transformation_matrix.svg.png)

---

<!-- _transition: fade -->
### **Transformações Básicas 2D**

<div class="columns">
<div>

#### 1. Translação
- **Equação:**  
  \( \begin{cases} x' = x + t_x \\ y' = y + t_y \end{cases} \)
- **Matriz:**  
  \( \begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix} \)

![h:200](https://upload.wikimedia.org/wikipedia/commons/2/2b/2D_translation.svg)


#### 2. Escala
- **Equação:**  
  \( \begin{cases} x' = s_x \cdot x \\ y' = s_y \cdot y \end{cases} \)

- **Matriz:**  
  \( \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix} \)

![h:200](https://upload.wikimedia.org/wikipedia/commons/3/3e/2D_scaling.svg)

---

### **Rotação 2D**
#### Transformação angular em torno da origem

- **Equação:**  
  \( \begin{cases} x' = x \cdot \cos\theta - y \cdot \sin\theta \\ y' = x \cdot \sin\theta + y \cdot \cos\theta \end{cases} \)

- **Matriz Homogênea:**  
  \( \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \)

![bg right:50%](https://upload.wikimedia.org/wikipedia/commons/8/87/2D_rotation.svg)

#### Exemplo Prático:
```python
# Pseudocódigo para rotação
def rotate(point, angle):
    theta = radians(angle)
    return [
        point[0]*cos(theta) - point[1]*sin(theta),
        point[0]*sin(theta) + point[1]*cos(theta)
    ]
```

---

<!-- _transition: slide -->
### **Composição de Transformações**
#### Ordem importa! (Não comutativa)

1. **Sequência correta:**  
   Escala → Rotação → Translação
2. **Problema comum:**  
   Rotacionar em torno de um ponto arbitrário

```mermaid
graph LR
    A[Objeto] --> B[Transladar para origem]
    B --> C[Rotacionar]
    C --> D[Transladar de volta]
```

![bg right:40%](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Combination_of_transformations.png/800px-Combination_of_transformations.png)

---

### **Transformações 3D**
#### Extensão do 2D com coordenada \( z \)

<div class="columns">
<div>

#### Translação 3D
\( \begin{bmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{bmatrix} \)

#### Escala 3D
\( \begin{bmatrix} s_x & 0 & 0 & 0 \\ 0 & s_y & 0 & 0 \\ 0 & 0 & s_z & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \)

</div>
<div>

#### Rotação 3D
Eixos principais:
- **X:** \( R_x(\theta) \)
- **Y:** \( R_y(\theta) \)
- **Z:** \( R_z(\theta) \)

![h:200](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Roll_Pitch_Yaw_rotations.svg/800px-Roll_Pitch_Yaw_rotations.svg.png)


---

### **Aplicações Práticas**
#### Exemplos reais em CG

1. **Hierarquia de Objetos:**  
   ```mermaid
   graph TB
       A[Personagem] --> B[Braço]
       B --> C[Antebraço]
       C --> D[Mão]
   ```

2. **Câmera Virtual:**  
   - Sistema de coordenadas de visualização
   - Matriz **View** (rotação + translação inversa)

3. **Projeção Perspectiva:**  
   \( \begin{bmatrix} \frac{2n}{r-l} & 0 & \frac{r+l}{r-l} & 0 \\ 0 & \frac{2n}{t-b} & \frac{t+b}{t-b} & 0 \\ 0 & 0 & -\frac{f+n}{f-n} & -\frac{2fn}{f-n} \\ 0 & 0 & -1 & 0 \end{bmatrix} \)

![bg right:40%](https://images.unsplash.com/photo-1551269901-5c5e14c25df7?auto=format&fit=crop&w=800)

---

<!-- _class: lead -->
# ![w:150](https://commons.wikimedia.org/wiki/File:Opengl-logo.svg)  
# Demonstração Interativa
### Explore transformações em tempo real

**Ferramentas sugeridas:**
- Three.js (WebGL)
- OpenGL/WebGL Shaders
- Blender Python API

![bg right:40%](https://images.unsplash.com/photo-1639762681057-408e52192e55?auto=format&fit=crop&w=800)

---

### **Referências**
1. Foley, Van Dam. *Computer Graphics: Principles and Practice*
2. Shirley, Marschner. *Fundamentals of Computer Graphics*
3. [LearnOpenGL - Transformations](https://learnopengl.com/Getting-started/Transformations)
4. [3Blue1Brown - Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDOjZzFwXHKw7LJJ5dIR8JK)

**Imagens:** Wikimedia Commons, Unsplash (licenças livres)

## Recursos Visuais Incluídos:
1. Diagramas vetoriais SVG da Wikimedia
2. Ilustrações matemáticas de matrizes
3. Grafos Mermaid para hierarquias
4. Pseudocódigo para implementação
5. Links para tutoriais interativos

## Como Executar:

```bash
marp transformacoes-geometricas.md -o transformacoes.pdf --html
# Ou para servir localmente:
marp -s transformacoes.md
```

**Dica:** Use o tema `gaia` com `invert` para melhor contraste em projetores, e adicione `<!-- _transition: slide/fade -->` entre slides para efeitos visuais suaves.