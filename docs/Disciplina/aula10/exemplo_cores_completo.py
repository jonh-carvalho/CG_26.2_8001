"""
Exemplo de Implementação: Laboratório de Cores
Exercício prático baseado no conteúdo de Cor em Computação Gráfica
"""

import matplotlib.pyplot as plt
import numpy as np
from colorsys import rgb_to_hsv, hsv_to_rgb, rgb_to_hls, hls_to_rgb
import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
from PIL import Image, ImageTk
import math

class ConversorCores:
    """Conversor entre diferentes espaços de cores"""
    
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.setup_interface()
        self.cor_atual = (255, 0, 0)  # Vermelho inicial
        
    def setup_interface(self):
        # Título
        ttk.Label(self.frame, text="Conversor de Espaços de Cores", 
                 font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Frame para seleção de cor
        frame_cor = ttk.Frame(self.frame)
        frame_cor.pack(pady=10)
        
        ttk.Button(frame_cor, text="Escolher Cor", 
                  command=self.escolher_cor).pack(side='left', padx=5)
        
        self.canvas_cor = tk.Canvas(frame_cor, width=100, height=50, bg='red')
        self.canvas_cor.pack(side='left', padx=10)
        
        # Frames para valores
        self.setup_valores()
        
    def setup_valores(self):
        # RGB
        frame_rgb = ttk.LabelFrame(self.frame, text="RGB", padding=10)
        frame_rgb.pack(fill='x', pady=5)
        
        self.var_r = tk.StringVar(value="255")
        self.var_g = tk.StringVar(value="0")
        self.var_b = tk.StringVar(value="0")
        
        ttk.Label(frame_rgb, text="R:").grid(row=0, column=0, sticky='w')
        ttk.Entry(frame_rgb, textvariable=self.var_r, width=10).grid(row=0, column=1, padx=5)
        ttk.Label(frame_rgb, text="G:").grid(row=0, column=2, sticky='w')
        ttk.Entry(frame_rgb, textvariable=self.var_g, width=10).grid(row=0, column=3, padx=5)
        ttk.Label(frame_rgb, text="B:").grid(row=0, column=4, sticky='w')
        ttk.Entry(frame_rgb, textvariable=self.var_b, width=10).grid(row=0, column=5, padx=5)
        
        # HSV
        frame_hsv = ttk.LabelFrame(self.frame, text="HSV", padding=10)
        frame_hsv.pack(fill='x', pady=5)
        
        self.var_h = tk.StringVar()
        self.var_s = tk.StringVar()
        self.var_v = tk.StringVar()
        
        ttk.Label(frame_hsv, text="H:").grid(row=0, column=0, sticky='w')
        ttk.Entry(frame_hsv, textvariable=self.var_h, width=10, state='readonly').grid(row=0, column=1, padx=5)
        ttk.Label(frame_hsv, text="S:").grid(row=0, column=2, sticky='w')
        ttk.Entry(frame_hsv, textvariable=self.var_s, width=10, state='readonly').grid(row=0, column=3, padx=5)
        ttk.Label(frame_hsv, text="V:").grid(row=0, column=4, sticky='w')
        ttk.Entry(frame_hsv, textvariable=self.var_v, width=10, state='readonly').grid(row=0, column=5, padx=5)
        
        # Botão para atualizar
        ttk.Button(self.frame, text="Atualizar Conversões", 
                  command=self.atualizar_conversoes).pack(pady=10)
        
        # Atualizar valores iniciais
        self.atualizar_conversoes()
        
    def escolher_cor(self):
        cor = colorchooser.askcolor(title="Escolha uma cor")
        if cor[0]:  # Se uma cor foi selecionada
            r, g, b = [int(c) for c in cor[0]]
            self.cor_atual = (r, g, b)
            self.var_r.set(str(r))
            self.var_g.set(str(g))
            self.var_b.set(str(b))
            self.atualizar_conversoes()
            
    def atualizar_conversoes(self):
        try:
            r = int(self.var_r.get())
            g = int(self.var_g.get())
            b = int(self.var_b.get())
            
            # Validar valores RGB
            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))
            
            self.cor_atual = (r, g, b)
            
            # Atualizar canvas
            hex_cor = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas_cor.configure(bg=hex_cor)
            
            # Converter para HSV
            h, s, v = rgb_to_hsv(r/255, g/255, b/255)
            self.var_h.set(f"{h*360:.1f}°")
            self.var_s.set(f"{s*100:.1f}%")
            self.var_v.set(f"{v*100:.1f}%")
            
        except ValueError:
            messagebox.showerror("Erro", "Valores RGB devem ser números entre 0 e 255")

class GeradorPaletas:
    """Gerador de paletas harmônicas"""
    
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.setup_interface()
        self.cor_base = (255, 0, 0)
        
    def setup_interface(self):
        ttk.Label(self.frame, text="Gerador de Paletas Harmônicas", 
                 font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Seleção de cor base
        frame_base = ttk.Frame(self.frame)
        frame_base.pack(pady=10)
        
        ttk.Button(frame_base, text="Cor Base", 
                  command=self.escolher_cor_base).pack(side='left', padx=5)
        
        self.canvas_base = tk.Canvas(frame_base, width=50, height=30, bg='red')
        self.canvas_base.pack(side='left', padx=10)
        
        # Botões para tipos de paleta
        frame_tipos = ttk.Frame(self.frame)
        frame_tipos.pack(pady=10)
        
        ttk.Button(frame_tipos, text="Complementar", 
                  command=self.gerar_complementar).pack(side='left', padx=5)
        ttk.Button(frame_tipos, text="Análogas", 
                  command=self.gerar_analogas).pack(side='left', padx=5)
        ttk.Button(frame_tipos, text="Triádica", 
                  command=self.gerar_triadica).pack(side='left', padx=5)
        
        # Frame para exibir paleta
        self.frame_paleta = ttk.Frame(self.frame)
        self.frame_paleta.pack(pady=20, fill='x')
        
    def escolher_cor_base(self):
        cor = colorchooser.askcolor(title="Escolha a cor base")
        if cor[0]:
            r, g, b = [int(c) for c in cor[0]]
            self.cor_base = (r, g, b)
            hex_cor = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas_base.configure(bg=hex_cor)
            
    def rgb_para_hsv_graus(self, r, g, b):
        h, s, v = rgb_to_hsv(r/255, g/255, b/255)
        return h * 360, s, v
        
    def hsv_graus_para_rgb(self, h, s, v):
        h_norm = (h % 360) / 360
        r, g, b = hsv_to_rgb(h_norm, s, v)
        return int(r * 255), int(g * 255), int(b * 255)
        
    def gerar_complementar(self):
        r, g, b = self.cor_base
        h, s, v = self.rgb_para_hsv_graus(r, g, b)
        
        # Cor complementar está 180° oposta no círculo cromático
        h_comp = (h + 180) % 360
        r_comp, g_comp, b_comp = self.hsv_graus_para_rgb(h_comp, s, v)
        
        paleta = [self.cor_base, (r_comp, g_comp, b_comp)]
        self.exibir_paleta(paleta, "Complementar")
        
    def gerar_analogas(self):
        r, g, b = self.cor_base
        h, s, v = self.rgb_para_hsv_graus(r, g, b)
        
        # Cores análogas: ±30° da cor base
        cores = []
        for offset in [-30, 0, 30]:
            h_nova = (h + offset) % 360
            r_nova, g_nova, b_nova = self.hsv_graus_para_rgb(h_nova, s, v)
            cores.append((r_nova, g_nova, b_nova))
            
        self.exibir_paleta(cores, "Análogas")
        
    def gerar_triadica(self):
        r, g, b = self.cor_base
        h, s, v = self.rgb_para_hsv_graus(r, g, b)
        
        # Cores triádicas: 120° de diferença
        cores = []
        for offset in [0, 120, 240]:
            h_nova = (h + offset) % 360
            r_nova, g_nova, b_nova = self.hsv_graus_para_rgb(h_nova, s, v)
            cores.append((r_nova, g_nova, b_nova))
            
        self.exibir_paleta(cores, "Triádica")
        
    def exibir_paleta(self, cores, tipo):
        # Limpar paleta anterior
        for widget in self.frame_paleta.winfo_children():
            widget.destroy()
            
        ttk.Label(self.frame_paleta, text=f"Paleta {tipo}:", 
                 font=('Arial', 12, 'bold')).pack()
        
        frame_cores = ttk.Frame(self.frame_paleta)
        frame_cores.pack(pady=10)
        
        for i, (r, g, b) in enumerate(cores):
            frame_cor = ttk.Frame(frame_cores)
            frame_cor.pack(side='left', padx=5)
            
            hex_cor = f"#{r:02x}{g:02x}{b:02x}"
            canvas = tk.Canvas(frame_cor, width=60, height=60, bg=hex_cor)
            canvas.pack()
            
            ttk.Label(frame_cor, text=f"RGB({r},{g},{b})", 
                     font=('Arial', 8)).pack()

class AnalisadorContraste:
    """Analisador de contraste e acessibilidade"""
    
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.setup_interface()
        self.cor1 = (0, 0, 0)      # Preto
        self.cor2 = (255, 255, 255) # Branco
        
    def setup_interface(self):
        ttk.Label(self.frame, text="Analisador de Contraste", 
                 font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Seleção de cores
        frame_cores = ttk.Frame(self.frame)
        frame_cores.pack(pady=10)
        
        # Cor 1
        frame_cor1 = ttk.Frame(frame_cores)
        frame_cor1.pack(side='left', padx=20)
        
        ttk.Label(frame_cor1, text="Cor 1 (Texto)").pack()
        ttk.Button(frame_cor1, text="Escolher", 
                  command=lambda: self.escolher_cor(1)).pack(pady=5)
        self.canvas1 = tk.Canvas(frame_cor1, width=80, height=40, bg='black')
        self.canvas1.pack()
        
        # Cor 2
        frame_cor2 = ttk.Frame(frame_cores)
        frame_cor2.pack(side='left', padx=20)
        
        ttk.Label(frame_cor2, text="Cor 2 (Fundo)").pack()
        ttk.Button(frame_cor2, text="Escolher", 
                  command=lambda: self.escolher_cor(2)).pack(pady=5)
        self.canvas2 = tk.Canvas(frame_cor2, width=80, height=40, bg='white')
        self.canvas2.pack()
        
        # Botão para analisar
        ttk.Button(self.frame, text="Analisar Contraste", 
                  command=self.analisar_contraste).pack(pady=20)
        
        # Área de resultados
        self.frame_resultado = ttk.LabelFrame(self.frame, text="Resultado", padding=10)
        self.frame_resultado.pack(fill='x', pady=10)
        
        self.label_razao = ttk.Label(self.frame_resultado, text="Razão de Contraste: -")
        self.label_razao.pack()
        
        self.label_avaliacao = ttk.Label(self.frame_resultado, text="Avaliação: -")
        self.label_avaliacao.pack()
        
        # Preview do contraste
        self.canvas_preview = tk.Canvas(self.frame, width=300, height=100)
        self.canvas_preview.pack(pady=10)
        
        # Análise inicial
        self.analisar_contraste()
        
    def escolher_cor(self, numero):
        cor = colorchooser.askcolor(title=f"Escolha a cor {numero}")
        if cor[0]:
            r, g, b = [int(c) for c in cor[0]]
            hex_cor = f"#{r:02x}{g:02x}{b:02x}"
            
            if numero == 1:
                self.cor1 = (r, g, b)
                self.canvas1.configure(bg=hex_cor)
            else:
                self.cor2 = (r, g, b)
                self.canvas2.configure(bg=hex_cor)
                
            self.analisar_contraste()
            
    def calcular_luminancia(self, rgb):
        """Calcula luminância relativa (WCAG 2.1)"""
        r, g, b = [x/255.0 for x in rgb]
        
        # Aplicar correção gamma
        def gamma_correcao(c):
            return c/12.92 if c <= 0.03928 else ((c + 0.055)/1.055) ** 2.4
            
        r = gamma_correcao(r)
        g = gamma_correcao(g)
        b = gamma_correcao(b)
        
        return 0.2126 * r + 0.7152 * g + 0.0722 * b
        
    def analisar_contraste(self):
        l1 = self.calcular_luminancia(self.cor1)
        l2 = self.calcular_luminancia(self.cor2)
        
        # Calcular razão de contraste
        if l1 > l2:
            razao = (l1 + 0.05) / (l2 + 0.05)
        else:
            razao = (l2 + 0.05) / (l1 + 0.05)
            
        # Avaliar acessibilidade
        if razao >= 7:
            avaliacao = "AAA - Excelente para todo tipo de texto"
            cor_status = "green"
        elif razao >= 4.5:
            avaliacao = "AA - Bom para texto normal"
            cor_status = "blue"
        elif razao >= 3:
            avaliacao = "AA Large - Apenas para texto grande (18pt+)"
            cor_status = "orange"
        else:
            avaliacao = "Falha - Contraste insuficiente"
            cor_status = "red"
            
        # Atualizar interface
        self.label_razao.config(text=f"Razão de Contraste: {razao:.2f}:1")
        self.label_avaliacao.config(text=f"Avaliação: {avaliacao}", foreground=cor_status)
        
        # Atualizar preview
        self.atualizar_preview()
        
    def atualizar_preview(self):
        self.canvas_preview.delete("all")
        
        # Cores em hex
        hex_cor1 = f"#{self.cor1[0]:02x}{self.cor1[1]:02x}{self.cor1[2]:02x}"
        hex_cor2 = f"#{self.cor2[0]:02x}{self.cor2[1]:02x}{self.cor2[2]:02x}"
        
        # Desenhar preview
        self.canvas_preview.create_rectangle(0, 0, 300, 100, fill=hex_cor2, outline="")
        self.canvas_preview.create_text(150, 30, text="Texto de Exemplo", 
                                       fill=hex_cor1, font=('Arial', 14))
        self.canvas_preview.create_text(150, 60, text="Example Text (Large)", 
                                       fill=hex_cor1, font=('Arial', 18, 'bold'))

class AplicacaoCores:
    """Aplicação principal integrando todas as funcionalidades"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Laboratório de Cores - Computação Gráfica")
        self.root.geometry("800x600")
        
        # Criar notebook para abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.setup_abas()
        
    def setup_abas(self):
        # Aba Conversor
        aba_conversor = ttk.Frame(self.notebook)
        self.notebook.add(aba_conversor, text="Conversor de Cores")
        self.conversor = ConversorCores(aba_conversor)
        
        # Aba Paletas
        aba_paletas = ttk.Frame(self.notebook)
        self.notebook.add(aba_paletas, text="Paletas Harmônicas")
        self.paletas = GeradorPaletas(aba_paletas)
        
        # Aba Contraste
        aba_contraste = ttk.Frame(self.notebook)
        self.notebook.add(aba_contraste, text="Análise de Contraste")
        self.contraste = AnalisadorContraste(aba_contraste)
        
    def run(self):
        self.root.mainloop()

# Exemplo de uso das funcionalidades via matplotlib
def demonstracao_matplotlib():
    """Demonstração usando matplotlib para visualizações"""
    
    # Criar figura com subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Laboratório de Cores - Demonstrações', fontsize=16)
    
    # 1. Círculo cromático HSV
    ax1 = axes[0, 0]
    theta = np.linspace(0, 2*np.pi, 360)
    radius = np.linspace(0, 1, 100)
    T, R = np.meshgrid(theta, radius)
    
    # Converter para RGB
    H = T / (2*np.pi)
    S = R
    V = np.ones_like(H)
    
    rgb_array = np.zeros((100, 360, 3))
    for i in range(100):
        for j in range(360):
            rgb_array[i, j] = hsv_to_rgb(H[i, j], S[i, j], V[i, j])
    
    ax1.imshow(rgb_array, extent=[-1, 1, -1, 1])
    ax1.set_title('Círculo Cromático HSV')
    ax1.set_aspect('equal')
    
    # 2. Paleta complementar
    ax2 = axes[0, 1]
    cor_base = (0.8, 0.2, 0.3)  # RGB normalizado
    h, s, v = rgb_to_hsv(*cor_base)
    h_comp = (h + 0.5) % 1.0
    cor_comp = hsv_to_rgb(h_comp, s, v)
    
    cores_comp = [cor_base, cor_comp]
    for i, cor in enumerate(cores_comp):
        ax2.add_patch(plt.Rectangle((i, 0), 1, 1, facecolor=cor))
    ax2.set_xlim(0, 2)
    ax2.set_ylim(0, 1)
    ax2.set_title('Cores Complementares')
    ax2.set_xticks([0.5, 1.5])
    ax2.set_xticklabels(['Base', 'Complementar'])
    
    # 3. Degradê de saturação
    ax3 = axes[1, 0]
    saturacoes = np.linspace(0, 1, 100)
    h_base = 0.6  # Azul
    v_base = 0.8
    
    degradê = np.zeros((50, 100, 3))
    for i, s in enumerate(saturacoes):
        cor = hsv_to_rgb(h_base, s, v_base)
        degradê[:, i] = cor
    
    ax3.imshow(degradê, aspect='auto', extent=[0, 1, 0, 1])
    ax3.set_title('Variação de Saturação')
    ax3.set_xlabel('Saturação (0 = Cinza, 1 = Pura)')
    
    # 4. Análise de luminância
    ax4 = axes[1, 1]
    cores_teste = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'black', 'white']
    luminancias = []
    
    for cor_nome in cores_teste:
        # Converter nome da cor para RGB
        if cor_nome == 'red': rgb = (255, 0, 0)
        elif cor_nome == 'green': rgb = (0, 255, 0)
        elif cor_nome == 'blue': rgb = (0, 0, 255)
        elif cor_nome == 'yellow': rgb = (255, 255, 0)
        elif cor_nome == 'cyan': rgb = (0, 255, 255)
        elif cor_nome == 'magenta': rgb = (255, 0, 255)
        elif cor_nome == 'black': rgb = (0, 0, 0)
        elif cor_nome == 'white': rgb = (255, 255, 255)
        
        # Calcular luminância
        r, g, b = [x/255.0 for x in rgb]
        luminancia = 0.2126 * r + 0.7152 * g + 0.0722 * b
        luminancias.append(luminancia)
    
    bars = ax4.bar(cores_teste, luminancias, color=cores_teste)
    ax4.set_title('Luminância Relativa por Cor')
    ax4.set_ylabel('Luminância')
    ax4.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Executar aplicação principal
    print("Iniciando Laboratório de Cores...")
    print("1. Aplicação GUI")
    print("2. Demonstração matplotlib")
    
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == "1":
        app = AplicacaoCores()
        app.run()
    elif escolha == "2":
        demonstracao_matplotlib()
    else:
        print("Opção inválida. Executando aplicação GUI...")
        app = AplicacaoCores()
        app.run()