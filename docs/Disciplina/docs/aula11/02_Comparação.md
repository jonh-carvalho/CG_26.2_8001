# Comparação de Modelos de Iluminação: Realismo vs Performance vs Material

## 📊 Tabela Comparativa Completa

| **Modelo** | **Realismo** | **Performance** | **Melhor Para** | **Pior Para** | **Custo Computacional** |
|------------|-------------|-----------------|------------------|---------------|------------------------|
| **Lambert** | ⭐☆☆☆☆ | ⭐⭐⭐⭐⭐ | Superfícies mate, papel | Materiais brilhantes | Muito Baixo |
| **Phong** | ⭐⭐☆☆☆ | ⭐⭐⭐⭐☆ | Plásticos, materiais sintéticos | Materiais metálicos | Baixo |
| **Blinn-Phong** | ⭐⭐☆☆☆ | ⭐⭐⭐⭐⭐ | Eficiência geral, jogos | Materiais complexos | Baixo |
| **Oren-Nayar** | ⭐⭐⭐☆☆ | ⭐⭐⭐☆☆ | Tecidos, barro, superfícies rugosas | Materiais lisos | Médio-Baixo |
| **Cook-Torrance** | ⭐⭐⭐⭐☆ | ⭐⭐☆☆☆ | Metais, vidro, materiais realistas | Performance crítica | Alto |
| **PBR Completo** | ⭐⭐⭐⭐⭐ | ⭐☆☆☆☆ | CGI, filmes, arquitetura | Tempo real antigo | Muito Alto |
| **Ray Tracing** | ⭐⭐⭐⭐⭐ | ⭐☆☆☆☆ | Reflexões precisas, sombras suaves | Dispositivos móveis | Extremo |
| **Hybrid Renderers** | ⭐⭐⭐⭐☆ | ⭐⭐☆☆☆ | Jogos modernos, RTX | Hardware antigo | Alto-Moderado |

## 🎯 Guia de Seleção por Cenário

### **1. Jogos Mobile/Web (Performance Crítica)**
```
Recomendado: Blinn-Phong ou Phong
• Performance: ⭐⭐⭐⭐⭐
• Realismo: ⭐⭐☆☆☆
• Materiais: Plásticos, cores sólidas
```

### **2. Jogos AAA Modernos (Balanço)**
```
Recomendado: PBR Simplificado + Hybrid Rendering
• Performance: ⭐⭐⭐☆☆
• Realismo: ⭐⭐⭐⭐☆
• Materiais: Metais, plásticos, tecidos
```

### **3. Visualização Arquitetônica (Realismo Moderado)**
```
Recomendado: Cook-Torrance + Iluminação Global
• Performance: ⭐⭐☆☆☆
• Realismo: ⭐⭐⭐⭐☆
• Materiais: Concreto, madeira, vidro
```

### **4. Filmes/Animacao (Máximo Realismo)**
```
Recomendado: PBR Completo + Path Tracing
• Performance: ⭐☆☆☆☆
• Realismo: ⭐⭐⭐⭐⭐
• Materiais: Todos os tipos complexos
```

### **5. Prototipagem Rápida**
```
Recomendado: Lambert/Phong
• Performance: ⭐⭐⭐⭐⭐
• Realismo: ⭐☆☆☆☆
• Materiais: Básicos para blocking
```

## 🔧 Especificação por Tipo de Material

### **Materiais Não-Metálicos (Dielétricos)**
- **Plástico liso**: Phong/Blinn-Phong
- **Plástico rugoso**: Oren-Nayar
- **Madeira**: Lambert + texturas
- **Tecido**: Oren-Nayar + subsurface scattering

### **Materiais Metálicos**
- **Metais polidos**: Cook-Torrance (GGX)
- **Metais corroídos**: PBR com roughness map
- **Ouro/cobre**: PBR com tintura especular

### **Materiais Translúcidos**
- **Vidro**: Ray Tracing + Fresnel
- **Pele**: Subsurface scattering
- **Cera/mármore**: BSSRDF simplificado

## ⚡ Impacto Performance por Componente

### **Componentes Leves**
- Iluminação ambiente: 1-2% custo
- Difusa Lambert: 3-5% custo
- Especular Phong: 5-10% custo

### **Componentes Moderados**
- Mapeamento de normais: 10-15% custo
- Oren-Nayar: 15-20% custo
- Cook-Torrance básico: 20-30% custo

### **Componentes Pesados**
- Ray Tracing: 200-500% custo
- Subsurface scattering: 50-100% custo
- Iluminação global: 100-300% custo

## 🎮 Exemplos Práticos por Plataforma

### **Mobile (OpenGL ES)**
```glsl
// Shader móvel eficiente - Blinn-Phong
vec3 calculateLight() {
    vec3 diffuse = max(dot(N, L), 0.0) * lightColor;
    vec3 H = normalize(L + V);
    vec3 specular = pow(max(dot(N, H), 0.0), 32.0) * specColor;
    return ambient + diffuse + specular;
}
```

### **Desktop Moderno (Vulkan/Metal)**
```glsl
// Shader PBR simplificado
vec3 calculatePBR() {
    float NDF = DistributionGGX(N, H, roughness);
    float G = GeometrySmith(N, V, L, roughness);
    vec3 F = fresnelSchlick(max(dot(H, V), 0.0), F0);
    // ... combinação Cook-Torrance
}
```

### **Ray Tracing (DX12/Vulkan RT)**
```hlsl
// Shader RT completo
[shader("closesthit")]
void Main() {
    float3 hitPoint = WorldRayOrigin() + RayTCurrent() * WorldRayDirection();
    // Recursive ray tracing para reflexões/refrações
}
```

## 📈 Recomendações por Orçamento Computacional

### **Orçamento Baixo (< 2ms/frame)**
- Blinn-Phong com 1-3 luzes
- Sem shadows dinâmicos
- Texturas difusas apenas

### **Orçamento Médio (2-8ms/frame)**
- PBR simplificado
- Shadow maps estáticos
- Normal mapping
- 3-8 luzes

### **Orçamento Alto (8-16ms/frame)**
- PBR completo
- Iluminação global estática
- SSR (Screen Space Reflections)
- 8-16 luzes com shadows

### **Orçamento Ilimitado (> 16ms/frame)**
- Path tracing completo
- Ray tracing dinâmico
- Subsurface scattering
- Participating media

Esta comparação ajuda a selecionar o modelo ideal baseado nas constraints específicas do projeto, hardware disponível e qualidade visual desejada.