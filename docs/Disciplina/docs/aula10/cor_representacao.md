## Representação e Processamento Digital de Imagens

Sumário Executivo

Este documento sintetiza os princípios fundamentais da representação, processamento e codificação digital de imagens, bem como os modelos de cores e a análise comparativa entre os sistemas visuais humano e artificial. Os pontos mais críticos abordados nas fontes incluem:

* Definição e Escopo do Processamento de Imagens: O processamento não visa criar imagens a partir de dados brutos (computação gráfica), mas manipular, tratar, exibir e extrair informações de imagens previamente geradas.
* Estrutura da Imagem Digital: As imagens são representadas por matrizes de pontos chamados pixels (Bit-Map), cujas resoluções espaciais dependem da quantidade de elementos nos eixos horizontal (X) e vertical (Y).
* Psicofísica do Sistema Visual Humano: A percepção de cores baseia-se na teoria dos três estímulos (tri-stimulus theory), com receptores sensíveis a comprimentos de onda específicos (Vermelho: 700 nm, Verde: 546,1 nm, Azul: 435,8 nm). O olho humano possui maior sensibilidade ao verde e à luminância do que às variações de cromaticidade.
* Modelos e Espaços de Cores: Destacam-se os modelos aditivos (RGB), subtrativos (CMY/CMYK) e modelos desacoplados orientados à transmissão ou ao usuário (YIQ, YUV, HSI, HLS, HSV). O desacoplamento da luminância em relação à cor é essencial tanto para a economia de banda em transmissões de TV quanto para o processamento de imagem em algoritmos inspirados na visão humana.
* Codificação e Profundidade de Bits: A quantização define a quantidade de cores disponíveis. Sistemas de Cor Verdadeira (True Color) utilizam 24 bits/pixel (16 milhões de cores), enquanto sistemas limitados (4 ou 8 bits) empregam paletas de cores (Color Look-Up Tables) e técnicas como dithering para simular nuances de cor.
* Visão Humana versus Visão Artificial: A visão humana é altamente flexível, subjetiva e otimizada para tarefas 3D no espectro visível. A visão artificial opera em espectros amplos (raios X ao infravermelho), é altamente exata e rápida em medições 2D baseadas em pixels, mas rígida e limitada em contexto tridimensional.

1. Fundamentos e Aplicações do Processamento de Imagens

Definição e Conceito

O Processamento de Imagens abrange a manipulação, exibição e tratamento de imagens digitais pré-existentes, além de prover a interface entre arquivos de imagem e dispositivos gráficos de entrada/saída. Não deve ser confundido com a geração sintética de imagens; seu foco é o aprimoramento do sinal visual ou a extração automática de dados contidos na imagem.

Áreas de Aplicação

As aplicações do processamento digital dividem-se centralmente em duas grandes categorias:

1. Tratamento e Melhoria de Imagens:
  * Medicina e Biologia;
  * Controle de Qualidade industrial;
  * Sistemas de Segurança e Monitoração;
  * Geologia e Sensoriamento Remoto (processamento de imagens de satélite);
  * Meteorologia.
2. Reconhecimento e Classificação de Objetos:
  * Sistemas de identificação de impressões digitais;
  * Interpretação automática de textos (OCR);
  * Visão artificial e Robótica;
  * Exploração automatizada (sistemas de exploração submarina, anti-bombas e mísseis teleguiados).

Estrutura e Resolução da Imagem Digital

* Pixel (Picture Element / Dot): Elemento básico e indivisível de uma imagem.
* Mapa de Bits (Bit-Map): Matriz bidimensional de pixels dispostos na tela do computador. Cada pixel contém uma informação de cor associada, obtida de forma direta ou por meio de consulta indireta a uma tabela de palette.
* Resolução Espacial: Define a quantidade de pontos disponíveis nas dimensões horizontal (eixo X) e vertical (eixo Y).

Padrões de Resolução e Razão de Aspecto

Dispositivo / Sistema	Resolução Típica (Pixels)	Razão de Aspecto
Campo Visual Humano	3000 \times 3000	N/A
Televisão Comum (NTSC / PAL-M)	512 \times 480	4/3
Computadores PC	640 \times 480, 800 \times 600, 1024 \times 768	4/3
Televisão de Alta Definição (HDTV)	2000 \times 1100	\approx 2
Cinema	Variável	\approx 2

2. Psicofísica da Visão Humana e Teoria das Cores

Receptores e Sensibilidade do Olho Humano

O espectro visível humano situa-se entre 400 nm (violeta) e 700 nm (vermelho) — com algumas tabelas do material registrando a faixa estendida de luz visível de 300 nm a 700 nm.

A percepção das cores fundamenta-se na Teoria dos Três Estímulos (tri-stimulus theory), segundo a qual a retina possui três tipos de receptores específicos para comprimentos de onda correspondentes às cores primárias:

* Vermelho (Red): Pico em 700 nm;
* Verde (Green): Pico em 546,1 nm;
* Azul (Blue): Pico em 435,8 nm.

O olho humano não apresenta sensibilidade uniforme ao espectro: possui maior sensibilidade ao verde, seguida pela sensibilidade ao vermelho, sendo consideravelmente menor a sensibilidade ao azul. As cores percebidas no cotidiano são o resultado de uma combinação linear (soma ponderada) das intensidades dessas três faixas.

Parâmetros Fundamentais da Cor

As fontes luminosas e a percepção cromática caracterizam-se por três parâmetros principais:

1. Intensidade / Luminância / Brilho (Brightness):
  * Mede a energia luminosa emitida ou refletida.
  * O valor zero (ausência de energia) representa o preto.
  * É o parâmetro visual ao qual o olho humano é mais sensível.
  * Sistemas monocromáticos (escala de cinza) operam exclusivamente com informação de luminância (geralmente codificada em 8 bits).
2. Matiz (Hue):
  * Representa o comprimento de onda dominante da radiação luminosa.
  * Distingue a identidade da cor (ex.: diferença entre azul, verde e vermelho).
  * Codificação típica: cerca de 4 bits.
3. Saturação:
  * Mede a pureza da cor ou a quantidade de luz branca misturada a ela.
  * A cor branca representa saturação zero (impureza máxima, mistura de todas as cores).
  * Cores altamente saturadas são chamadas de "brilhantes"; cores com baixa saturação são denominadas "pastel".
  * Codificação típica: cerca de 4 bits.

3. Modelos e Espaços de Cores

A representação de cores varia conforme o objetivo tecnológico (exibição em telas, impressão de pigmentos, transmissão de vídeo ou processamento centrado na percepção do usuário).

Sistema Aditivo (RGB)

* Fundamento: Baseia-se na emissão direta de luz por três fontes primárias (Red, Green, Blue).
* Funcionamento: A cor final é obtida adicionando-se intensidade às componentes.
  * Intensidade zero em R, G e B \rightarrow Preto.
  * Intensidade máxima em R, G e B \rightarrow Branco.
* Aplicações: Monitores de computador, displays e dispositivos de tubo de imagem (CRT).

Sistema Subtrativo (CMY e CMYK)

* Fundamento: Baseia-se na absorção e reflexão da luz por pigmentos e tintas (Ciano, Magenta, Amarelo). É o modelo complementar/inverso do RGB.
* Geometria de Espaço: Pode ser representado por um cubo simétrico ao cubo RGB, no qual a origem (0,0,0) é o Branco e o vértice máximo (1,1,1) representa o Preto.
* Variante CMYK: Adiciona o pigmento preto (Key/Black) devido à dificuldade prática de obter pigmentos puros que resultem num preto perfeito pela mistura de C, M e Y.
* Aplicações: Processos de impressão gráfica e fotografia.

Modelos de Cores Desacoplados e Orientados à Aplicação

1. Sistemas YIQ e YUV (Transmissão de Vídeo)

Projetados para a transmissão comercial de TV (padrão NTSC) e compatibilidade com receptores em preto e branco.

* Desacoplamento: A componente de luminância (Y) é mantida em uma banda de frequência mais larga, enquanto as componentes de cromaticidade (I e Q ou U e V) utilizam bandas mais estreitas (as cromaticidades podem ser codificadas em apenas 5% da banda sem degradar o sinal).
* Fórmulas do Sistema YUV:
  * U = 0,493 \times (B - Y)
  * V = 0,877 \times (R - Y)
* Matriz de Conversão RGB para YIQ: \begin{bmatrix} Y \\ I \\ Q \end{bmatrix} = \begin{bmatrix} 0,30 & 0,59 & 0,11 \\ 0,60 & -0,28 & -0,32 \\ 0,21 & -0,52 & 0,31 \end{bmatrix} \begin{bmatrix} R \\ G \\ B \end{bmatrix}

2. Sistemas HSI, HSV e HLS (Orientados ao Usuário)

* Estes sistemas estruturam a cor em termos de Matiz (Hue), Saturação (Saturation) e Intensidade (Intensity) / Valor (Value) / Luminância (Lightness).
* Ao desacoplar a intensidade das informações cromáticas, o modelo HSI aproxima-se da percepção visual humana, tornando-se ideal para o desenvolvimento de algoritmos de processamento de imagens baseados no olho humano.
* A interface gráfica dos sistemas operacionais frequentemente disponibiliza caixas de seleção baseadas no modelo HLS combinadas com entradas RGB.

Gama de Cores (Gamut)

A Gama de um sistema é o conjunto total de cores que pode ser produzido a partir de suas primárias. O aumento da saturação das primárias amplia a gama do sistema.

Hierarquia de Gamut entre Tecnologias: \text{Fotografia} > \text{Monitores Profissionais} > \text{TV Comum} \text{Monitores} > \text{Técnicas de Impressão}

4. Codificação, Quantização e Transparência

Codificação e Quantização

* Canal de Cor: Cada cor primária individual usada no sistema.
* Amostragem: Processo em que a intensidade de cada primária é codificada em um valor discreto para o canal.
* Quantização: Define a precisão/número de bits alocados por canal (comumente entre 1 e 8 bits).

Cor Verdadeira (True Color) versus Sistemas de Paleta

1. Sistemas de Cor Verdadeira (True Color):
  * O valor do pixel é a combinação direta dos valores dos canais.
  * Padrão 24 bits: 8 bits para cada uma das 3 primárias (R, G, B), gerando 256 níveis de luminância por canal \rightarrow reproduz cerca de 16 milhões de cores.
  * Padrão 15 bits (Econômico): Usa 5 bits por cor (32.768 cores). Para ajustar em palavras de 16 bits, pode-se usar uma codificação não simétrica sacrifiçando a precisão da cor azul, ou reservando o bit extra para transparência.
2. Sistemas de Paleta / Tabela de Cores (Color Look-Up Table - LUT):
  * Utilizados quando a capacidade gráfica do hardware é menor que a de cor verdadeira (sistemas de 4 ou 8 bits).
  * O valor gravado no pixel não representa a cor final, mas sim um índice referente a uma tabela de cores armazenada em memória dedicada.
  * Em modos 8 bits (VGA/SuperVGA), permite a exibição simultânea de até 256 cores.
  * Diminui a profundidade do pixel, reduzindo o uso de memória do sistema.

Técnica de Dithering

Em imagens restritas a 8 bits, o realismo é prejudicado. Para mitigar esse problema, troca-se resolução espacial por resolução de cor: grupos de pixels vizinhos são combinados com diferentes padrões de cores para simular tons que não existem diretamente na paleta ativa.

Codificação da Transparência (Canal Alfa)

* Sistemas de 16 bits (15 bits + 1 bit alfa): O bit adicional especifica transparência binária para o pixel (cada pixel é estritamente opaco ou transparente).
* Sistemas de 32 bits (24 bits RGB + 8 bits alfa): O canal alfa dedicado de 8 bits permite até 256 gradações de transparência, recurso amplamente aplicado em efeitos e processamento de vídeo.

5. Diretrizes para o Uso Eficiente de Cores

O uso de cores em interfaces digitais atende a propósitos estéticos, de destaque visual e de codificação de dados (como relevo, variação de temperatura e dinâmica de fluidos). Devido às limitações fisiológicas do sistema visual humano, aplicam-se as seguintes regras:

* Sensibilidade Espacial: O olho humano é mais sensível a variações espaciais de intensidade do que de cor. Detalhes pequenos devem diferir do fundo primariamente em intensidade (brilho) e não apenas em tonalidade.
* Combinações Inadequadas:
  * Azul e preto;
  * Amarelo e branco;
  * Regra de Ouro: Não utilizar a cor azul para elementos de texto.
* Acessibilidade para Daltônicos: Evitar o uso simultâneo de verdes e vermelhos que apresentem baixa saturação e baixa intensidade.
* Percepção de Objetos Pequenos: A capacidade humana de identificar e discriminar cores cai drasticamente em objetos de pequenas dimensões.
* Ilusões e Efeitos Contextuais:
  * A cor percebida de um elemento é alterada diretamente pela cor do fundo que o circunda.
  * Cores altamente saturadas causam o surgimento de pós-imagens (afterimages) no olho humano.
  * Cores afetam o tamanho e a distância percebidos: objetos na cor vermelha aparentam ser maiores do que objetos na cor verde. Além disso, a refração diferenciada das cores na lente ocular causa a ilusão de que as cores estão a distâncias distintas do observador.

6. Comparação Extensiva: Sistema Visual Humano vs. Visão Artificial

A tabela a seguir consolida as diferenças funcionais e físicas entre o sistema biológico humano e os sistemas de visão computacional artificial:

Parâmetro de Comparação	Sistema Visual Humano	Sistema de Visão Artificial
Espectro de Atuação	Limitado à faixa de luz visível (300\text{ nm} a 700\text{ nm}).	Opera em praticamente todo o espectro eletromagnético (dos raios X ao infravermelho).
Flexibilidade	Extremamente flexível; adapta-se facilmente a diferentes tarefas e ambientes de trabalho.	Normalmente inflexível; apresenta bom desempenho apenas na tarefa específica para a qual foi projetado.
Habilidade / Precisão	Estabelece estimativas relativamente precisas em julgamentos subjetivos.	Efetua medições exatas baseadas em contagem de pixels (depende da resolução da imagem digitalizada).
Processamento de Cor	Possui capacidade de interpretação altamente subjetiva de cores.	Mede de forma objetiva e quantitativa os valores das componentes R, G e B.
Sensibilidade Ambiental	Adapta-se a variações de iluminação, características da superfície e distância do objeto.	Sensível ao nível e padrão de iluminação, à distância do objeto e às suas características físicas.
Níveis de Cinza	Limitado na distinção simultânea de muitos níveis de cinza.	Trabalha facilmente com centenas de tons de cinza simultâneos, conforme o projeto do digitalizador.
Tempo de Resposta	Elevado, situado na ordem de 0,1\text{ segundo}.	Dependente do hardware, podendo alcançar tempos tão baixos quanto 0,001\text{ segundo}.
Processamento 2D e 3D	Executa tarefas 3D e processa múltiplos comprimentos de onda facilmente.	Executa tarefas 2D com facilidade, mas é lento e bastante limitado em tarefas 3D.
Percepção de Brilho	Percebe variações de brilho em escala logarítmica. A interpretação depende da área ao redor.	Pode perceber o brilho em escala linear ou logarítmica.
