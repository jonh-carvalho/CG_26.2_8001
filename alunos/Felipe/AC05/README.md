# AC05 — Iluminação, Textura e Realismo

## Aluno
Felipe Ultramar

## Disciplina
Computação Gráfica

## Ferramenta Utilizada
Blender 4.5 LTS

---

# 1. Componentes de Iluminação — Modelo Phong

A iluminação da cena foi configurada seguindo os três componentes do modelo de Phong, que decompõe a luz em ambiente, difusa e especular. A tabela abaixo apresenta os valores finais utilizados:

| Componente | Configuração no Blender | Valor Utilizado |
|------------|--------------------------|-----------------|
| Ambiente   | World → Background: cor #0A0A1A, Strength | Cor: #0A0A1A / Strength: 0,05 |
| Difusa     | Luz_Abajur → Power; cor da luz | Power: 50W / Cor: #FFFFFF |
| Especular  | Roughness nos materiais dos objetos | Variável por objeto |

### Componente Ambiente
A iluminação ambiente foi configurada no World Shader com cor azul muito escura (#0A0A1A) e intensidade 0,05, simulando uma noite fechada com mínimo de luz difusa no ambiente. Não gera sombras e serve como base para a cena noturna.

### Componente Difusa
A luz Point (Luz_Abajur), posicionada dentro da cúpula do abajur, foi configurada com Power de 50W e cor branca (#FFFFFF). Essa luz ilumina suavemente os objetos ao redor, criando gradientes de luz e sombra característicos da iluminação difusa.

### Componente Especular
O componente especular foi controlado pelo valor de Roughness nos materiais de cada objeto. Valores baixos de roughness (como no copo, 0,15) produzem reflexos mais intensos, enquanto valores altos (como no livro, 0,9) resultam em superfícies opacas sem brilho.

---

# 2. Materiais Aplicados — Justificativa

| Objeto | Material | Roughness / Configuração |
|--------|----------|--------------------------|
| Mesa | PBR com textura de madeira escura | Metallic: 0,0 / Specular IOR: 0,3 |
| Livro | Procedural (Noise Texture + Color Ramp) | Roughness: 0,9 / Metallic: 0,0 |
| Copo | Vidro fosco (Transmission = 1.0) | Roughness: 0,15 / IOR: 1,45 |
| Lápis | Cor sólida (#CC2200) | Roughness: 0,5 / Metallic: 0,0 |
| Abajur (cúpula) | Plástico com leve emissão (#F5E6C0) | Emission Strength: 0,1 |

A mesa utiliza textura PBR de madeira escura obtida no Poly Haven, com UV Mapping via Smart UV Project, garantindo realismo.  
O livro usa textura procedural com Noise Texture para simular papel envelhecido.  
O copo foi configurado como vidro com transmissão total de luz e refração realista.  
O lápis utiliza material simples de cor sólida.  
A cúpula do abajur possui emissão leve para simular o brilho do material iluminado internamente.

---

# 3. Comparação Visual — Renders

## Render 1 — Cena noturna completa

Com o World Shader ativo (Strength 0,05), a cena apresenta uma iluminação ambiente azulada escura, simulando uma noite fechada. A luz do abajur (50W) cria contraste entre áreas iluminadas e sombras profundas. Observa-se reflexão especular na mesa e refração no copo.

## Render 2 — Sem luz ambiente

Com o World Shader desativado (Strength 0,0), apenas a luz do abajur influencia a cena. As regiões fora do alcance da luz ficam completamente escuras, evidenciando o cone de iluminação e destacando a importância do componente ambiente no modelo de Phong.

---

## Detalhes Técnicos
- Engine: EEVEE (Blender 4.5 LTS)
- Resolução: 1920 × 1080 px
  
https://drive.google.com/drive/folders/11WjHKMkFyalysK21lc_yCXRsyItMHZ1T?usp=drive_link
