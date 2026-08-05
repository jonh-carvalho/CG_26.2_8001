# Exercício Prático: Explorando Cores em Python

## Objetivo
Desenvolver uma aplicação interativa em Python que explore conceitos fundamentais de teoria das cores apresentados no material didático, incluindo:
- Espaços de cores (RGB, HSV, HSL)
- Harmonias cromáticas
- Temperatura de cor
- Contraste e saturação

## Descrição do Exercício

### Parte 1: Conversor de Espaços de Cores
Crie um programa que permita conversões entre diferentes espaços de cores:

```python
import matplotlib.pyplot as plt
import numpy as np
from colorsys import rgb_to_hsv, hsv_to_rgb, rgb_to_hls, hls_to_rgb
import tkinter as tk
from tkinter import ttk, colorchooser

class ConversorCores:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Conversor de Espaços de Cores")
        self.setup_interface()
        
    def setup_interface(self):
        # Interface para seleção de cores
        # Campos para RGB, HSV, HSL
        # Botões para conversão
        pass
        
    def rgb_para_hsv(self, r, g, b):
        """Converte RGB para HSV"""
        return rgb_to_hsv(r/255, g/255, b/255)
        
    def mostrar_cor(self, r, g, b):
        """Exibe a cor selecionada"""
        pass
```

### Parte 2: Gerador de Paletas Harmônicas
Implemente um gerador que cria paletas baseadas em harmonia cromática:

```python
class GeradorPaletas:
    def __init__(self, cor_base):
        self.cor_base = cor_base
        
    def paleta_complementar(self):
        """Gera paleta com cores complementares"""
        # Implementar rotação de 180° no círculo cromático
        pass
        
    def paleta_analogas(self):
        """Gera paleta com cores análogas (±30°)"""
        pass
        
    def paleta_triadica(self):
        """Gera paleta triádica (120° de diferença)"""
        pass
        
    def visualizar_paleta(self, cores):
        """Visualiza a paleta gerada"""
        fig, axes = plt.subplots(1, len(cores), figsize=(10, 2))
        for i, cor in enumerate(cores):
            axes[i].imshow([[cor]])
            axes[i].set_title(f'RGB: {cor}')
            axes[i].axis('off')
        plt.show()
```

### Parte 3: Simulador de Daltonismo
Desenvolva uma ferramenta que simula diferentes tipos de daltonismo:

```python
class SimuladorDaltonismo:
    def __init__(self, imagem):
        self.imagem = imagem
        
    def protanopia(self):
        """Simula deficiência para vermelho"""
        # Matriz de transformação para protanopia
        matriz = np.array([[0.567, 0.433, 0],
                          [0.558, 0.442, 0],
                          [0, 0.242, 0.758]])
        return self.aplicar_filtro(matriz)
        
    def deuteranopia(self):
        """Simula deficiência para verde"""
        pass
        
    def tritanopia(self):
        """Simula deficiência para azul"""
        pass
        
    def aplicar_filtro(self, matriz):
        """Aplica matriz de transformação na imagem"""
        pass
```

### Parte 4: Analisador de Contraste
Crie uma ferramenta que analisa o contraste entre cores:

```python
class AnalisadorContraste:
    def calcular_luminancia(self, rgb):
        """Calcula luminância relativa da cor"""
        r, g, b = [x/255.0 for x in rgb]
        # Aplicar correção gamma
        r = r/12.92 if r <= 0.03928 else ((r + 0.055)/1.055) ** 2.4
        g = g/12.92 if g <= 0.03928 else ((g + 0.055)/1.055) ** 2.4
        b = b/12.92 if b <= 0.03928 else ((b + 0.055)/1.055) ** 2.4
        return 0.2126 * r + 0.7152 * g + 0.0722 * b
        
    def razao_contraste(self, cor1, cor2):
        """Calcula razão de contraste entre duas cores"""
        l1 = self.calcular_luminancia(cor1)
        l2 = self.calcular_luminancia(cor2)
        if l1 > l2:
            return (l1 + 0.05) / (l2 + 0.05)
        else:
            return (l2 + 0.05) / (l1 + 0.05)
            
    def avaliar_acessibilidade(self, razao):
        """Avalia se o contraste atende diretrizes de acessibilidade"""
        if razao >= 7:
            return "AAA - Excelente"
        elif razao >= 4.5:
            return "AA - Bom"
        elif razao >= 3:
            return "AA Large - Aceitável para texto grande"
        else:
            return "Falha - Contraste insuficiente"
```

### Parte 5: Aplicação Principal
Integre todas as funcionalidades em uma interface única:

```python
class AplicacaoCores:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Laboratório de Cores - Computação Gráfica")
        self.setup_menu()
        
    def setup_menu(self):
        """Cria menu principal com todas as funcionalidades"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menu Conversores
        menu_conv = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Conversores", menu=menu_conv)
        menu_conv.add_command(label="RGB ↔ HSV", command=self.abrir_conversor)
        
        # Menu Paletas
        menu_pal = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Paletas", menu=menu_pal)
        menu_pal.add_command(label="Gerar Harmônicas", command=self.abrir_paletas)
        
        # Menu Acessibilidade
        menu_acc = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Acessibilidade", menu=menu_acc)
        menu_acc.add_command(label="Simular Daltonismo", command=self.abrir_daltonismo)
        menu_acc.add_command(label="Analisar Contraste", command=self.abrir_contraste)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AplicacaoCores()
    app.run()
```

## Bibliotecas Necessárias

```bash
pip install matplotlib numpy pillow tkinter colorsys
```

## Objetivos de Aprendizagem

1. **Compreender espaços de cores**: Diferenças entre RGB, HSV e HSL
2. **Aplicar teoria das cores**: Harmonia cromática e círculo cromático
3. **Desenvolver consciência de acessibilidade**: Contraste e daltonismo
4. **Programação prática**: Interface gráfica e manipulação de imagens
5. **Visualização de dados**: Representação gráfica de cores

## Extensões Possíveis

- Adicionar suporte para CMYK
- Implementar algoritmos de quantização de cores
- Criar filtros artísticos baseados em temperatura de cor
- Desenvolver ferramenta de extração de paleta de imagens
- Adicionar análise de histogramas de cor

## Avaliação

- **Funcionalidade** (40%): Todas as conversões e cálculos funcionam corretamente
- **Interface** (25%): Interface intuitiva e bem organizada
- **Precisão** (20%): Algoritmos implementados corretamente
- **Criatividade** (15%): Extensões e melhorias adicionais

Este exercício permite explorar os conceitos teóricos de cor de forma prática e interativa, consolidando o aprendizado através da programação.