# **AP2 — Peça Audiovisual “Ibmec em 15 segundos”**

**Ferramenta:** Blender **4.5 LTS**

**Data entrega e apresentação:** 18/11/2026 no Lab 212.
**Envio:** no repositório GitHub utilizado nas ACs e na AP1

## Contexto

Na **AP1**, você concebeu e modelou uma cena para apresentar a palavra **Ibmec**, acompanhada de três objetos autorais, e planejou uma narrativa em storyboard. Na **AC04**, estudou a iluminação da cena e comparou os modelos Lambert, Phong e Blinn-Phong. Na **AC05**, desenvolveu materiais PBR e aplicou texturas aos objetos.

Na AP2, você integrará essas etapas em uma peça audiovisual de **15 segundos**, com animação, iluminação, materiais, texturas, renderização e exportação. O projeto deve preservar a ideia central da AP1, a legibilidade e a identidade visual da palavra **Ibmec**, e a contribuição dos três objetos autorais.

## Objetivo

Finalizar a cena da AP1 como uma animação 3D curta, utilizando o planejamento visual, os recursos de iluminação estudados na AC04 e os materiais e texturas preparados na AC05. A peça deverá comunicar uma ideia com clareza e apresentar movimento, composição e acabamento visual coerentes.

## Conceitos mobilizados

- **Planejamento visual:** conceito, storyboard, ritmo e organização de planos.
- **Animação:** poses-chave, keyframes, timing, espaçamento e interpolação.
- **Câmera:** enquadramento, movimento e continuidade visual.
- **Iluminação:** posição, tipo e intensidade das luzes para orientar a atenção.
- **Materiais PBR e texturas:** resposta das superfícies à luz, UVs e mapas.
- **Renderização e exportação:** configuração da cena e produção do vídeo final.

## Continuidade das etapas anteriores

1. Abra a cena da AC05 e salve uma cópia como `AP2_NomeSobrenome.blend`. Preserve os arquivos da AP1, AC04 e AC05.
2. Mantenha o conceito, a composição e os momentos previstos no storyboard da AP1. É permitido ajustar a modelagem e o enquadramento quando isso melhorar a animação, sem descaracterizar a proposta.
3. Preserve a palavra **Ibmec** como elemento visual principal, mantendo sua leitura e identidade visual. Evite movimentos, efeitos, iluminação ou texturas que a ocultem ou prejudiquem.
4. Mantenha na cena os três objetos autorais identificados na AP1. Eles devem participar da narrativa ou contribuir intencionalmente para sua apresentação.
5. Reaproveite os materiais e mapas da AC05. Ajuste-os quando necessário para que funcionem durante o movimento e sob a iluminação final.
6. Considere os estudos de iluminação da AC04, mas escolha a configuração final em função da cena e da leitura dos materiais. O `Principled BSDF` é baseado em princípios físicos; não deve ser descrito como implementação literal de Phong ou Blinn-Phong.

## Proposta da peça

Crie uma sequência com início, desenvolvimento e encerramento. A narrativa deve apresentar a palavra **Ibmec** e integrar os objetos autorais de forma coerente com o conceito da AP1.

Use o storyboard como guia e ajuste-o se a duração, a câmera ou a ação planejada mudar. A peça pode ser abstrata ou figurativa; não é necessário contar uma história complexa. A prioridade é que o público compreenda a intenção e consiga acompanhar a ação.

## Requisitos de produção

### 1. Planejamento e continuidade

- Revise o conceito, o storyboard e o papel de cada objeto na narrativa.
- Planeje a sequência em momentos ou planos, indicando ação, duração aproximada e enquadramento.
- Mantenha a marca legível nos momentos principais da peça.
- Organize a cena e mantenha nomes identificáveis para objetos, câmeras, luzes e materiais.

### 2. Animação

- Crie uma animação de **15 segundos a 24 fps**, do frame **1 ao 360**.
- Anime a câmera e pelo menos **dois elementos da cena**, sendo pelo menos um deles a palavra **Ibmec** ou um dos três objetos autorais.
- Escolha propriedades adequadas à ação, como posição, rotação, escala ou influência de uma constraint. Não é necessário animar todas as propriedades.
- Use keyframes e revise timing, espaçamento e interpolação no Graph Editor.
- Evite movimentos involuntários, mudanças bruscas e colisões visuais que prejudiquem a composição.

### 3. Iluminação, materiais e texturas

- Configure iluminação que mantenha os elementos legíveis e valorize as superfícies ao longo da sequência.
- Utilize materiais PBR da AC05 em três objetos e preserve, na palavra **Ibmec**, um material compatível com sua identidade visual.
- Verifique a aplicação das texturas durante o movimento da câmera e dos objetos; corrija distorções, escalas ou repetições que se tornem visíveis.
- Use os mapas de cor base, rugosidade e normal corretamente. Mapas de dados devem manter a interpretação de cor apropriada e mapas normais devem passar pelo nó `Normal Map`.
- Empacote as imagens externas no arquivo `.blend` ou entregue-as junto ao projeto com caminhos relativos funcionais.

### 4. Renderização e exportação

- Utilize **Eevee** ou **Cycles**(se possuir GPU poderosa) no Blender 4.5 LTS.
- Configure resolução, taxa de quadros e intervalo da animação antes da renderização final.
- Exporte o vídeo em `.mp4` com codec H.264. Faça testes curtos ou em baixa resolução antes de renderizar toda a sequência.
- Assista ao vídeo exportado integralmente para verificar imagem, duração, enquadramento e eventuais falhas.

## Requisitos técnicos

1. Duração de 15 segundos, a 24 fps, totalizando 360 frames (frames 1–360).
2. Animação de câmera e de pelo menos dois elementos da cena, com participação da palavra **Ibmec** ou de um objeto autoral.
3. Cena com a palavra **Ibmec** e os três objetos autorais da AP1 preservados e reconhecíveis.
4. Materiais PBR e texturas da AC05 aplicados aos objetos autorais, com ajustes quando necessários à sequência.
5. Iluminação configurada para apoiar a narrativa e manter a leitura dos elementos.
6. Renderização da animação completa e exportação do vídeo em `.mp4` (H.264).
7. Arquivo `.blend` organizado, com recursos externos empacotados ou entregues em caminhos relativos funcionais.

## Entregáveis

1. Arquivo `AP2_NomeSobrenome.blend` com cena, animações, materiais, texturas, iluminação, câmera e configurações de saída.
2. Vídeo final `AP2_NomeSobrenome.mp4`, com 15 segundos de duração e 24 fps.
3. Pelo menos uma imagem renderizada da peça (quadro final ou frame representativo).
4. Storyboard atualizado, se houve mudanças relevantes em relação ao da AP1.
5. Relatório curto (`.md` ou `.pdf`) contendo:
   - título, conceito e resumo da sequência;
   - descrição dos momentos ou planos e das ações animadas;
   - propriedades animadas e decisões de timing/interpolação;
   - configuração geral de iluminação e renderização;
   - descrição dos materiais e texturas reaproveitados ou ajustados da AC05;
   - desafios encontrados e soluções adotadas;
   - fontes e licenças de recursos externos utilizados.

## Critérios de avaliação — 10,0 pontos

| Critério | Pontos |
|---|---:|
| Continuidade do conceito, storyboard e composição da AP1; legibilidade e identidade da marca | 2,0 |
| Animação da câmera e dos elementos da cena; timing, interpolação e clareza do movimento | 2,5 |
| Iluminação e integração dos materiais PBR e texturas da AC04/AC05 | 2,0 |
| Qualidade visual, composição e comunicação da peça | 1,5 |
| Renderização, exportação e funcionamento do arquivo `.blend` | 1,0 |
| Organização, relatório, autoria e identificação das fontes | 1,0 |
| **Total** | **10,0** |

## Referências

- [AP1 — Conceito e Modelagem da Peça “Ibmec em 15 segundos”](./ap1.md)
- [AC04 — Modelos de Iluminação](./AC04.md)
- [AC05 — Materiais PBR e Texturas](./AC05.md)
- [Introdução à animação](../Disciplina/aula14/Animação.md)
- [Blender 4.5 LTS — documentação oficial](https://docs.blender.org/manual/en/4.5/)

## Observações

- A AP2 é a finalização da cena desenvolvida nas etapas anteriores, não uma cena independente. Mudanças são permitidas quando servirem à narrativa e preservarem a proposta central.
- Não é necessário criar uma simulação física, personagem com rig ou cena interativa. Esses recursos podem ser usados se forem pertinentes ao conceito e não comprometerem os requisitos essenciais.
- Áudio é opcional. Se utilizado, deve ser adequado à peça e ter origem/licença identificada no relatório.
- Salve cópias de segurança antes de alterações importantes e confirme que o projeto abre corretamente no Blender 4.5 LTS.