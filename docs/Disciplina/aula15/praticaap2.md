# Tutoriais Práticos para AP2 — Blender 4.5 LTS
## Peça Audiovisual "Ibmec em 15 segundos"

Pequenos tutoriais simples e objetivos para dominar os principais temas solicitados na AP2.

---

## 1. PREPARANDO A CENA E A LINHA DO TEMPO

### 1.1 Copiar a cena da AC05 e configurar a timeline

1. Abra o Blender 4.5 LTS
2. Carregue o arquivo `AC05_NomeSobrenome.blend`
3. Vá em **File > Save As** e salve como `AP2_NomeSobrenome.blend`
4. Na view **Timeline** (abaixo do viewport), confirme que a resolução está **24 fps**
   - Clique na seta da view > **Output Properties** (ícone de impressora)
   - Frame rate: 24 fps
   - Output: 1920×1080 (ou sua resolução preferida)

### 1.2 Ajustar a duração da animação para 15 segundos

1. Abra a **Timeline** (se não estiver visível: Shift+F12)
2. Na barra de propriedades da timeline, defina:
   - **Start Frame:** 1
   - **End Frame:** 360 (15 segundos × 24 fps)
3. Clique no quadro **1** para começar

---

## 2. ANIMAÇÃO BÁSICA COM KEYFRAMES

### 2.1 Animar um objeto (exemplo: palavra "Ibmec")

1. Selecione o objeto **Ibmec** na cena
2. Pressione **I** (Insert keyframe) ou clique em **Insert Keyframe**
   - Escolha a propriedade a animar: **Location**, **Rotation**, **Scale**
   - Confirme no frame 1
3. Movimente o timeline até o frame **120** (5 segundos)
4. Mude a posição, rotação ou escala do objeto
5. Pressione **I** novamente para criar outro keyframe
6. Repita para outros frames importantes (ex: frames 60, 180, 300)

### 2.2 Revisar timing no Graph Editor

1. Abra o **Graph Editor** (Editor > Graph Editor ou clique em **editor type**)
2. Selecione o objeto animado
3. Observe as curvas de animação (vermelha=X, verde=Y, azul=Z)
4. Ajuste o timing:
   - Arraste os keyframes horizontalmente para mudar o tempo
   - Arraste verticalmente para mudar os valores
   - Escolha o tipo de interpolação: Linear (rápido) ou Bezier (suave)

### 2.3 Interpolação suave (Easing)

1. No Graph Editor, selecione um keyframe
2. Pressione **V** para abrir o menu de interpolação:
   - **Linear:** movimento uniforme
   - **Bezier:** movimento suave com aceleração
   - **Constant:** sem transição
3. Ajuste as alças da curva para controlar a velocidade

---

## 3. ANIMAÇÃO DE CÂMERA

### 3.1 Mover a câmera na cena

1. Selecione a **Camera** na cena (ou no Outliner)
2. Pressione **G** (Grab/Move) e arraste com o mouse, ou:
   - **G** + **X** (move no eixo X)
   - **G** + **Y** (move no eixo Y)
   - **G** + **Z** (move no eixo Z)
3. Pressione **I** para inserir keyframe de **Location**

### 3.2 Rotacionar a câmera

1. Câmera selecionada
2. Pressione **R** + eixo desejado (X, Y, ou Z)
3. Digite o ângulo ou arraste o mouse
4. Pressione **I** e escolha **Rotation** para keyframe

### 3.3 Zoom com focal length

1. Câmera selecionada
2. Na aba **Object Data Properties** (ícone de câmera), ajuste **Focal Length**
3. Valores menores = mais zoom; maiores = menos zoom
4. Altere em diferentes frames e insira keyframes

### 3.4 Dica: Visualizar o enquadramento

- Pressione **Numpad 0** para ver a câmera ativa
- Pressione **Numpad 0** novamente para voltar à vista 3D

---

## 4. ILUMINAÇÃO

### 4.1 Revisar/ajustar luzes existentes

1. Na **Outliner** (direita), encontre as luzes criadas em AC04
2. Selecione cada luz e verifique suas propriedades:
   - **Type:** Sun, Area, Spot, Point
   - **Energy:** intensidade (aumentar para mais brilho)
   - **Angle/Size:** define o tamanho da sombra

### 4.2 Mudar a intensidade de uma luz ao longo do tempo

1. Selecione a luz
2. Clique no valor **Energy** e insira um keyframe (**I**)
3. Mova para outro frame
4. Altere o valor de Energy
5. Insira outro keyframe
6. Resultado: a iluminação varia com a animação

## 5. MATERIAIS PBR E TEXTURAS (revisão da AC05)

### 5.1 Verificar materiais aplicados
# que material é esse? 
1. Selecione um objeto
2. Na aba **Shading** (superior), veja o **Shader Editor**
3. Procure pelo nó **Principled BSDF** (material padrão)
4. Conecte as texturas:
   - **Base Color:** imagem de cor
   - **Normal:** mapa normal (conecte via nó **Normal Map**)
   - **Roughness:** imagem de rugosidade
   - **Metallic:** valor entre 0 (não-metal) e 1 (metal puro)

### 5.2 Ajustar escala de UV para animação

1. Na aba **Shading**, localize o nó **Mapping** (controla escala/rotação das texturas)
2. Selecione-o e insira um keyframe em **Location**, **Rotation** ou **Scale**
3. Mude o frame e altere os valores para animar a textura

### 5.3 Empacotar texturas no .blend

1. Vá em **File > External Data > Pack All**
2. Todas as imagens externas são agora internas ao arquivo

---

## 6. COMPOSIÇÃO VISUAL E ENQUADRAMENTO

### 6.1 Regra dos terços

1. Na câmera, ative a grade de composição:
   - Na aba **Object Data Properties** (câmera), ative **Composition Guides**
2. Escolha o tipo (ex: Rule of Thirds)
3. Use como referência para posicionar elementos importantes

### 6.2 Plano-sequência (camera walk)

1. Câmera selecionada
2. Frame 1: Posicione a câmera de um lado da cena
3. Frame 360: Mova-a para outro ponto (ex: volta ao redor da marca "Ibmec")
4. Insira keyframes de Location nos frames 1 e 360
5. A câmera fará uma transição suave

---

## 7. RENDERIZAÇÃO E EXPORTAÇÃO

### 7.1 Testar render em baixa resolução

1. Na aba **Render Properties**:
   - Resolution: 640 × 360 (teste rápido)
   - Frame range: 1-360
2. Clique em **Render > Render Animation**
3. Escolha pasta de saída (ex: `C:\temp\render_test`)
4. Espere alguns frames renderizar

### 7.2 Renderizar em resolução final

1. Altere a resolução para 1920 × 1080
2. Na aba **Render Properties**, configure:
   - **Engine:** Eevee (rápido) ou Cycles (qualidade)
   - **Sampling:** 64-128 para Cycles (mais = melhor qualidade, mais lento)
   - **Frame range:** 1-360
3. Clique em **Render > Render Animation**
4. Salve em pasta segura com espaço em disco (~10-20 GB para 15s em 1080p)

### 7.3 Exportar para vídeo (MP4 H.264)

1. Abra **Output Properties**
2. Formato de saída:
   - **File Format:** MP4
   - **Codec:** H.264
   - **Bitrate:** 8000-16000 kbps (qualidade-tamanho)
3. Pasta de output: escolha onde salvar
4. Arquivo de saída: `AP2_NomeSobrenome.mp4`
5. Clique em **Render > Render Animation**
6. Resultado: vídeo MP4 direto, sem etapas extras

### 7.4 Verificação pós-render

1. Abra o arquivo `.mp4` em um player (ex: VLC)
2. Confirme:
   - Duração exata: 15 segundos
   - Taxa: 24 fps
   - Sem travamentos ou frames faltando
   - Marca "Ibmec" legível em todos os momentos

---

## 8. WORKFLOW GERAL RESUMIDO

### Passo a passo para AP2:

1. **Frame 1:** Câmera posicionada; insira keyframe de Location
2. **Frame 60 (2,5s):** Mova a câmera ou o objeto; insira novo keyframe
3. **Frame 120 (5s):** Próximo ponto da narrativa
4. **Frame 180 (7,5s):** Continuação
5. **Frame 240 (10s):** Aproximação do desfecho
6. **Frame 300 (12,5s):** Últimos ajustes visuais
7. **Frame 360 (15s):** Posição final; encerramento da cena
8. **Verificar:** Todos os materiais, texturas e luzes funcionando
9. **Render teste:** em baixa resolução (5-10 frames)
10. **Render final:** em alta resolução
11. **Export:** MP4 H.264
12. **Validar:** reproduzir vídeo completo

---

## 9. DICAS E ATALHOS ÚTEIS

| Ação | Atalho |
|------|--------|
| Inserir keyframe | **I** |
| Mover objeto | **G** |
| Rotacionar | **R** |
| Escalar | **S** |
| Mover no eixo X/Y/Z | **G** + **X/Y/Z** |
| Deletar keyframe | **Alt + I** |
| Reproduzir timeline | **Spacebar** (ou **Shift + Spacebar**) |
| Frame anterior | **Seta esquerda** |
| Próximo frame | **Seta direita** |
| Visão câmera | **Numpad 0** |
| Enquadrar seleção | **Numpad .** (ponto) |
| Abrir Graph Editor | **Ctrl + Tab** (ou manualmente) |
| Mostrar layout de animação | **Ctrl + Page Down** |

---

## 10. TROUBLESHOOTING COMUM

### A textura aparece distorcida na animação
- Verifique os UVs: Abra **UV Editor** e veja se mapeamento está correto
- Aumente a resolução da textura se disponível

### Renderização muito lenta
- Reduza o número de samples no Eevee/Cycles
- Use resolução menor para teste (640×360)
- Verifique se há objetos invisíveis contribuindo para o cálculo

### Câmera sai do enquadramento
- Use **Numpad 0** para visualizar a câmera
- Ajuste a posição antes de animar

### Arquivo não abre
- Verifique se as imagens externas estão acessíveis
- Use **File > External Data > Find Missing Files** para localizar

---

## 11. REFERÊNCIAS RÁPIDAS

- [Documentação Blender 4.5](https://docs.blender.org/manual/en/4.5/)
- [Blender Animation](https://docs.blender.org/manual/en/4.5/animation/)
- [Rendering & Cycles](https://docs.blender.org/manual/en/4.5/render/)
- [Video Output](https://docs.blender.org/manual/en/4.5/render/output/)

---

**Última atualização:** Novembro de 2026  
**Versão:** Blender 4.5 LTS
