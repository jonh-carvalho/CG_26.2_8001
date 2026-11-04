# Requisitos para o Exercício de Cores

## Bibliotecas Python Necessárias

```bash
pip install matplotlib>=3.5.0
pip install numpy>=1.21.0
pip install pillow>=8.3.0
```

**Nota**: `tkinter` e `colorsys` já vêm incluídos com Python por padrão.

## Como Executar

### 1. Aplicação GUI Completa
```bash
python exemplo_cores_completo.py
```
Escolha a opção **1** quando solicitado.

### 2. Demonstração com Matplotlib
```bash
python exemplo_cores_completo.py
```
Escolha a opção **2** quando solicitado.

## Funcionalidades Implementadas

### 📊 Conversor de Espaços de Cores
- Conversão entre RGB, HSV e HSL
- Interface interativa para seleção de cores
- Visualização em tempo real

### 🎨 Gerador de Paletas Harmônicas
- **Complementar**: Cores opostas no círculo cromático (180°)
- **Análogas**: Cores adjacentes (±30°)
- **Triádica**: Três cores equidistantes (120°)

### ♿ Analisador de Contraste WCAG
- Cálculo de razão de contraste conforme WCAG 2.1
- Avaliação de acessibilidade (AA, AAA)
- Preview visual do contraste

### 📈 Visualizações Científicas
- Círculo cromático HSV
- Análise de luminância
- Degradês de saturação

## Conceitos de Cor Aplicados

1. **Espaços de Cores**
   - RGB: Modelo aditivo para displays
   - HSV: Matiz, Saturação, Valor
   - HSL: Matiz, Saturação, Luminosidade

2. **Teoria das Cores**
   - Círculo cromático
   - Harmonia cromática
   - Temperatura de cor

3. **Acessibilidade**
   - Contraste WCAG
   - Luminância relativa
   - Legibilidade

## Extensões Sugeridas

1. **Daltonismo**: Implementar simulação de protanopia, deuteranopia e tritanopia
2. **CMYK**: Adicionar conversão para modelo subtrativo
3. **Temperatura de Cor**: Implementar conversão Kelvin ↔ RGB
4. **Extração de Paleta**: Analisar imagens para extrair paletas dominantes
5. **Filtros Artísticos**: Aplicar transformações baseadas em teoria das cores

## Estrutura de Arquivos

```
Aula06/
├── Exercicio_Cor_Python.md          # Enunciado do exercício
├── exemplo_cores_completo.py         # Implementação completa
├── requirements.txt                  # Dependências
└── README_Cores.md                   # Este arquivo
```

## Troubleshooting

### Problema: tkinter não encontrado
**Solução**: Em alguns sistemas Linux, instale:
```bash
sudo apt-get install python3-tk
```

### Problema: matplotlib não abre janelas
**Solução**: Configure o backend:
```python
import matplotlib
matplotlib.use('TkAgg')  # ou 'Qt5Agg'
```

### Problema: Cores não aparecem corretamente
**Solução**: Verifique se o monitor suporta sRGB e se o driver de vídeo está atualizado.

## Avaliação do Exercício

### Critérios (Total: 100 pontos)

1. **Funcionalidade Básica** (40 pontos)
   - Conversões RGB ↔ HSV ↔ HSL funcionam corretamente
   - Interface responsiva e intuitiva
   - Tratamento de erros adequado

2. **Teoria das Cores** (25 pontos)
   - Paletas harmônicas matematicamente corretas
   - Implementação do círculo cromático
   - Compreensão de espaços de cores

3. **Acessibilidade** (20 pontos)
   - Cálculo correto de contraste WCAG
   - Avaliação de legibilidade
   - Interface acessível

4. **Inovação e Extensões** (15 pontos)
   - Funcionalidades adicionais implementadas
   - Qualidade do código e documentação
   - Criatividade na apresentação

### Entrega

- **Código fonte** comentado e bem estruturado
- **Relatório** explicando os conceitos aplicados
- **Screenshots** das funcionalidades principais
- **Vídeo demonstrativo** (opcional, +5 pontos extras)

## Bibliografia Recomendada

1. **Adobe Color Theory**: https://color.adobe.com/create/color-wheel
2. **WCAG Guidelines**: https://www.w3.org/WAI/WCAG21/Understanding/
3. **Color Science**: Fairchild, Mark D. "Color Appearance Models"
4. **Python Documentation**: https://docs.python.org/3/library/colorsys.html