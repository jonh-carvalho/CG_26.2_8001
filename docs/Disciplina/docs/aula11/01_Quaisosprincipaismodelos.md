# Principais Modelos de Iluminação em Computação Gráfica

## 1. **Modelo de Iluminação Local (Simple Illumination)**
### Características:
- Considera apenas luz direta das fontes
- Não considera sombras ou inter-reflexões
- Computacionalmente leve

### Componentes básicos:
- **Ambiente**: Iluminação constante
- **Difusa**: Reflexão Lambertiana
- **Especular**: Reflexão direcional (Phong, Blinn-Phong)

## 2. **Modelo de Phong (1975)**
### Fórmula:
```
I = I_ambiente + I_difusa + I_especular
I = k_a * I_a + k_d * (L·N) * I_d + k_s * (R·V)^α * I_s
```

### Características:
- Simula materiais plásticos/brilhantes
- Componente especular dependente do ângulo de visão
- Expoente `α` controla a "nitidez" do brilho

## 3. **Modelo Blinn-Phong (1977)**
### Melhoria sobre Phong:
- Usa vetor **half-vector** (H) em vez de reflexão (R)
- `H = (L + V) / ||L + V||`
- Computacionalmente mais eficiente
- Mais estável em ângulos rasos

## 4. **Modelo de Iluminação Global**
### Abordagens:
- **Ray Tracing**: Traça raios da câmera para a cena
- **Path Tracing**: Amostragem Monte Carlo de caminhos de luz
- **Radiosidade**: Simula transferência de energia entre superfícies

## 5. **Modelos Baseados em Física (PBR - Physically Based Rendering)**
### Características:
- Conservação de energia
- Lei de reciprocidade de Helmholtz
- Baseado em medidas do mundo real

### Modelos PBR populares:
- **Disney BRDF** (usado no Principled BSDF do Blender)
- **GGX** (distribuição de microfacetas)
- **Cook-Torrance** (modelo geral de microfacetas)

## 6. **Modelo de Cook-Torrance (1981)**
### Fórmula:
```
f_r = k_d * f_lambert + k_s * (D * F * G) / (4 * (N·V) * (N·L))
```
Onde:
- **D**: Distribuição de normais (NDF)
- **F**: Termo de Fresnel
- **G**: Função de sombreamento/ocultação

## 7. **Modelo Oren-Nayar (1994)**
### Especializado para:
- Superfícies rugosas difusas
- Materiais como barro, tecido, papel
- Considera micro-superfícies com orientações variadas

## 8. **Modelo de Minnaert (1941)**
### Característica única:
- Simula o "escurecimento do limbo" (limb darkening)
- Útil para materiais como veludo e pele
- `I ∝ (N·L)^e * (N·V)^{e-1}`

## 9. **Modelo de Ward (1992)**
### Anisotrópico:
- Simula materiais com brilho direcional
- Como CDs, tecidos brilhantes, metais escovados
- Considera diferentes rugosidades nas direções X e Y

## 10. **Modelos de Subsurface Scattering (SSS)**
### Para materiais translúcidos:
- **BSSRDF** (Bidirectional Surface Scattering Reflectance Distribution Function)
- **Difusão de difusão** (aproximação eficiente)
- Usado para pele, mármore, cera, plásticos

## Comparação de Aplicações:

| **Modelo** | **Melhor Para** | **Complexidade** |
|------------|-----------------|------------------|
| Phong | Materiais plásticos | Baixa |
| Blinn-Phong | Eficiência computacional | Baixa |
| Cook-Torrance | Metais/dielétricos realistas | Alta |
| Oren-Nayar | Superfícies rugosas | Média |
| PBR | Realismo físico | Alta |
| Ray Tracing | Reflexões/refrações precisas | Muito Alta |

## Tendências Atuais:
- **Hybrid Renderers**: Combina rasterização com ray tracing
- **Neural Rendering**: Usa redes neurais para iluminação
- **Real-time Global Illumination**: Techniques como Lumen (Unreal) e RTXGI

A escolha do modelo depende do balanço entre realismo necessário, performance disponível e tipo de material sendo simulado.