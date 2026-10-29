# BACKUP TÉCNICO DE RETOMADA — PASSOS 900–957
**Data:** 29/10/2026. **Último passo executado e aprovado: 957.** Próximo passo reservado: **958, ainda NÃO executado**. **Backup documental**, sem binários proprietários, executáveis, assets, credenciais, venv ou coleção integral dos scripts.

## 0. Leitura obrigatória / histórico anterior
- [Backup validado no passo 900](BACKUP_TECNICO_PASSO_900.md) e [checkpoint 900](CHECKPOINT_900.md): preservam extensivamente os passos 800–900, especialmente os caminhos de boot, configuração, hashes de 128/256/512 KiB e limitações históricas.
- Este documento **acrescenta o período 901–957**. Não substitui nem altera a evidência antiga.
- **Lacuna documental:** os logs completos de todos os passos 901–945 não estão disponíveis nesta sessão. O presente arquivo **não inventa** resultados individuais: registra apenas evidências de passos intermediários citadas em relatórios verificados e as saídas completas 947–957 disponíveis na conversa. Para auditoria íntegra de cada passo, preservar também os logs originais em posse do usuário.

## 1. Objetivo, regras e limites
Projeto independente de pesquisa técnica do cliente Windows de *The Seven Deadly Sins: Grand Cross*, sem afiliação com Netmarble. Objetivo a longo prazo: estudar viabilidade de testes locais, **sem afirmar haver servidor offline funcional**.
- Rotina: **um passo numerado de cada vez**, PowerShell 5.1 autossuficiente, Python embutido via here-string e `-B -`, executar apenas depois de receber e auditar a saída anterior. Manter testes read-only em relação aos arquivos oficiais.
- Diferenciar: (a) bytes estáticos e disassembly, (b) emulação isolada com memória fabricada, (c) execução real no cliente e (d) backend compatível. As duas últimas **não foram comprovadas neste ciclo**.
- Publicação: documentação própria somente; não versionar binários proprietários, assets, chaves, tokens ou conteúdo pessoal.

## 2. Ambiente local
- Cliente: `E:\JOGOS\Netmarble Game\7dsgb\GameAssembly.dll` — **47.199.760 bytes**.
- Python do laboratório: `E:\GrandCross_Local\Ferramentas\Emulacao_854\.venv\Scripts\python.exe` com Unicorn e Capstone.
- Windows PowerShell 5.1; Unity 2022.3.27f1; GameAssembly PE x64; metadados IL2CPP v29 / 29.1, conforme investigações anteriores.
- ImageBase PE: `0x180000000`. Seção `.vdata`: RVA `0x06A83000`, início VA `0x186A83000`, **14.131.200 bytes de tamanho virtual**, raw size 0.
- Seção `.boot`: RVA `0x077FD000`, offset de arquivo `0x02553800`, tamanho `8.060.416` bytes; entrada executada em `.boot+0x58`.
- No Unicorn, reconstrução da `.vdata` em memória, pilha sintética usual em `0x200000000`; nenhuma alteração do binário original.

## 3. Evolução da recuperação da .vdata
| Marco | Quantidade recuperada | Hash SHA-256 | Observação |
| --- | ---: | --- | --- |
| 900 | 524.288 bytes (512 KiB) | `8dbae2603dd37c17c6717167401d1c9d673a4178e59cabdd767612cf26f5eb19` | Evidência auditada no checkpoint 900 |
| 918 | prefixo de 4 MiB validado conforme registro intermediário recuperado | vide hash abaixo | Resultado textual detalhado não integralmente arquivado aqui |
| 951–957 | 4.194.304 bytes (4 MiB) | `b69ef8861b20e6cbc4111bc4137ac5b67b3c598054af76e53f737072280d67ac` | SHA repetido em **sete passos consecutivos**, 951, 952, 953, 954, 955, 956, 957 |

Quatro MiB correspondem a **29,681%** do espaço virtual declarado de 14.131.200 bytes em `.vdata` (medida de cobertura de bytes, **não** progresso total do projeto nem garantia de decodificação integral). Em reconstruções recentes, parada exata em `RDI=0x186E83000` após aproximadamente **44.769.590 instruções** no ambiente emulado; 957 reportou 27,800777 s. A recuperação integral, epílogo real e salto ao segundo estágio permanecem não demonstrados.

## 4. Experimentos de computação e despacho (PASSOS 942–950)
**PASSO 942:** laço estático de 20 instruções `.vdata+0x2FE523..0x2FE573` aplicado a 1.652 elementos artificiais. 33.042 instruções emuladas; canários preservados.

**PASSO 943:** percurso conjunto LOOP(20)+PREP(18)+DISPATCH(21), **59 instruções estáticas** de `0x2FE523` a `0x2FE61E` (final exclusivo), aproximadamente 33.081 instruções executadas. Transformações e salto para destinos artificiais; **tabela e endereço de salto reais desconhecidos**.

**PASSO 944:** desmontagem de **129 instruções** em `0x2FE2F0..0x2FE523`, localizando `CMP RDX,RAX` em `0x2FE48F` e `JE` em `0x2FE492` para `0x2FE5BE`, o início do despachante. O trajeto sem desvio leva à preparação e ao laço de 1.652 iterações.

**PASSO 945:** 34 instruções em `0x2FE377..0x2FE40F`; em quatro cenários sintéticos `RAX_final=(RCX+0x06D776B5) mod 2^64`, registradores e pilha esperados preservados.

**PASSO 946:** 27 instruções em `0x2FE2F0..0x2FE377`; fonte em `[RSP_inicial+0x90]`, grava `(fonte+RCX) mod 2^64` em `[RBP+RBX_inicial]`; máscara XOR intermediária cancela; quatro cenários aprovados.

**PASSO 947:** 61 instruções consecutivas (27+34), quatro testes aprovados, dois iguais e dois diferentes. Memória escrita `= fonte+RCX`, `RAX=RCX+0x06D776B5`. Ainda não executa o CMP.

**PASSO 948:** 23 instruções em `0x2FE40F..0x2FE469`. Demonstrado `RBX=0xAC` (172 decimal), independente dos quatro estados sintéticos iniciais; próxima leitura `[RBP+0xAC]`; `R10/R11/R12/RBP/RSP` restaurados.

**PASSO 949:** 94 instruções contínuas até `JE`; quatro testes: 2 `JE` tomados e 2 não. Destinos `0x2FE5BE` ou `0x2FE498`. Confirma que o conteúdo em `[RBP+0xAC]`, e **não somente** o valor da fonte, controla a igualdade `RDX==RAX`. Caso com `RBX_inicial=0x130` grava em outro endereço e desvia diferentemente.

**PASSO 950:** 94 instruções de preparação/comparação + 21 do despachante = **115 instruções dinâmicas no caminho tomado**. Índices de tabela artificiais 0, 3, 7 selecionaram `0x700000000`, `0x700000300`, `0x700000700`; 3/3 destinos corretos; cenário desigual interrompido em `0x2FE498`, 94 instruções. Controle `JMP [RAX]` em `0x2FE61C` (final da rotina `0x2FE61E`). **Não executados os destinos, nem identificada tabela real.**

Relação simplificada sob hipóteses de memória válida e sem aliasing relevante:
```c
MEM64[RBP + RBX_initial] = (source_stack + RCX) & UINT64_MAX;
RAX = (RCX + 0x06D776B5) & UINT64_MAX;
RBX = 0xAC;
RDX = MEM64[RBP + 0xAC];
if (RDX == RAX) goto RVA_0x6D815BE; // .vdata +0x2FE5BE
else goto RVA_0x6D81498;             // .vdata +0x2FE498
```
**Nota de endereçamento:** os offsets `0x2FE...` são relativos ao início da seção `.vdata`; portanto `VA=0x186A83000+offset` e `RVA=0x06A83000+offset`. Os símbolos ilustrativos acima não são funções reais identificadas.

## 5. A hipótese da constante como RVA e a tabela de pares (951–953)
**PASSO 951:** a constante `0x06D776B5`, interpretada como RVA, leva a `VA=0x186D776B5`, offset `.vdata+0x2F46B5` **dentro dos 4 MiB reconstruídos**. Não está provado que o cliente utilize o ImageBase como RCX nesse ponto. A região mostrou sequências de qwords semelhantes a RVAs, não ponteiros virtuais absolutos. Hash dos 128 bytes locais: `2da6e1f6de53131a5dd4ad049045ed226893ffe5aaa3f6b0cb2c8804d941c893`; 64 bytes zero.
**PASSO 952:** oito pares consecutivos de qwords a partir da região; todos `segundo=primeiro+5`, ambos RVAs pertencentes ao prefixo e cada primeiro endereço aponta para opcode `E9`, instrução `JMP rel32` de 5 bytes. **8/8 pares, 8 primeiros JMP, 0 CALL.**
**PASSO 953:** confirmado que **ambos** os RVAs de cada par apontam a `JMP rel32`; **16/16** destinos permanecem nos 4 MiB; 16 destinos diferentes, nenhum coincide com fonte da tabela. Mapa:
| Par | Primeiro JMP RVA | Destino 1 RVA | Segundo JMP RVA | Destino 2 RVA |
|---|---|---|---|---|
|0|`0x6AC939A`|`0x6ADBC70`|`0x6AC939F`|`0x6AC9FA0`|
|1|`0x6ABFE58`|`0x6A92152`|`0x6ABFE5D`|`0x6AE6664`|
|2|`0x6AC7C5E`|`0x6A908B4`|`0x6AC7C63`|`0x6AE448D`|
|3|`0x6AC7BD4`|`0x6ABECC7`|`0x6AC7BD9`|`0x6AE1144`|
|4|`0x6AB2808`|`0x6AA1BA8`|`0x6AB280D`|`0x6A9AEE8`|
|5|`0x6ADE52E`|`0x6ABB38E`|`0x6ADE533`|`0x6AB3246`|
|6|`0x6AC6212`|`0x6AE3DFE`|`0x6AC6217`|`0x6AA4808`|
|7|`0x6AC594C`|`0x6A911F3`|`0x6AC5951`|`0x6AA7D72`|
Semântica da tabela **não confirmada**; uma possível estrutura de pontos de controle, não nomear como tabela de correções comprovada.

## 6. Primeiros controles dos 16 destinos (954–955)
**PASSO 954:** até 32 instruções por destino: 16/16 inspecionados; somente dois JCC encontrados dentro do limite: `0x6AE44C6 JE ->0x6AE44DC`, `0x6AA7E02 JE ->0x6AA7E19`. Restantes 14 não atingiram um controle dentro do limite.
**PASSO 955:** expansão para até 256 instruções / 2048 bytes: **16/16** encontraram primeira transferência, sendo **15 condicionais (10 JBE, 5 JE)** e **1 RET** em `0x6AE66EE`. Nenhuma falha de decodificação. **RET é dependente da pilha**: saída anterior `0xFFFFFFFE80000000` era artefato de interpretar operando `RET 0` como endereço, corrigido.
Tabela dos 15 desvios estáticos:
| Par lado | Site RVA | Condição | Alvo tomado RVA | Fallthrough RVA |
|---|---|---|---|---|
|0 A|`0x6ADBF2F`|JBE|`0x6ADBF69`|`0x6ADBF35`|
|0 B|`0x6ACA0CE`|JBE|`0x6ACA0E4`|`0x6ACA0D4`|
|1 A|`0x6A92275`|JE|`0x6A9228B`|`0x6A9227B`|
|2 A|`0x6A909DF`|JBE|`0x6A909F1`|`0x6A909E5`|
|2 B|`0x6AE44C6`|JE|`0x6AE44DC`|`0x6AE44CC`|
|3 A|`0x6ABEE15`|JBE|`0x6ABEE44`|`0x6ABEE1B`|
|3 B|`0x6AE1587`|JBE|`0x6AE15B2`|`0x6AE158D`|
|4 A|`0x6AA1CE1`|JBE|`0x6AA1CF7`|`0x6AA1CE7`|
|4 B|`0x6A9B14C`|JBE|`0x6A9B167`|`0x6A9B152`|
|5 A|`0x6ABB4BE`|JBE|`0x6ABB4D5`|`0x6ABB4C4`|
|5 B|`0x6AB33FD`|JE|`0x6AB3414`|`0x6AB3403`|
|6 A|`0x6AE3F9B`|JBE|`0x6AE3FAF`|`0x6AE3FA1`|
|6 B|`0x6AA4956`|JE|`0x6AA496C`|`0x6AA495C`|
|7 A|`0x6A91324`|JBE|`0x6A9133B`|`0x6A9132A`|
|7 B|`0x6AA7E02`|JE|`0x6AA7E19`|`0x6AA7E08`|

## 7. Saídas e convergências estáticas (956–957)
**PASSO 956:** decodificados **15/15** sites, **30/30** saídas (tomado e não tomado), 30 endereços distintos, nenhuma repetição entre os endereços de entrada; primeiro opcode entre `mov` (10), `and` (5), `add` (4), `or` (4), `xor` (4), `sub` (3). Nenhum caminho executado.
**PASSO 957:** prosseguimento linear até a primeira transferência de cada uma das 30 saídas, limite 256 instruções / 2048 bytes. **30/30** encontraram controle; **26 JCC e 4 JMP**. Foram contadas **2.765 instruções examinadas**, **1.410 endereços de instrução distintos**, **1.355 endereços compartilhados**. **15/15 pares** compartilham pelo menos um mesmo endereço no trecho examinado; em cada caso, o primeiro endereço comum mostrado foi a entrada do lado TOMADO (porque o fluxo linear do lado NÃO TOMADO prossegue até ali). Isto é uma evidência de **reconvergência linear estática**, NÃO execução real das duas condições nem equivalência dos estados de registradores/memória após reconvergir. Par 2A termina em JMP indireto no site `0x6A90D01`; par 7A em JMP indireto no site `0x6A916E0`; ambos os lados dos dois pares chegam a esses mesmos sites. Os demais 13 pares seguem a JCC. São **15 sites de controle distintos**, embora a contagem por 30 caminhos registre 26 JCC + 4 JMP.
| Par/lado | Próximo site compartilhado RVA | Próximo destino direto tomado RVA | Categoria |
|---|---|---|---|
|0 A|`0x6ADC09A`|`0x6ADC126`|JCC|
|0 B|`0x6ACA306`|`0x6ACA320`|JCC|
|1 A|`0x6A923BF`|`0x6A923E9`|JCC|
|2 A|`0x6A90D01`|indireto|JMP|
|2 B|`0x6AE4600`|`0x6AE4627`|JCC|
|3 A|`0x6ABF09E`|`0x6ABF0AF`|JCC|
|3 B|`0x6AE173F`|`0x6AE17E0`|JCC|
|4 A|`0x6AA1D6B`|`0x6AA1D82`|JCC|
|4 B|`0x6A9B27C`|`0x6A9B298`|JCC|
|5 A|`0x6ABB705`|`0x6ABB74C`|JCC|
|5 B|`0x6AB34E2`|`0x6AB3510`|JCC|
|6 A|`0x6AE4255`|`0x6AE4263`|JCC|
|6 B|`0x6AA4A68`|`0x6AA4A75`|JCC|
|7 A|`0x6A916E0`|indireto|JMP|
|7 B|`0x6AA8166`|`0x6AA81A3`|JCC|

## 8. Interpretação rigorosa
- **Comprovado:** reconstrução reproduzível dos primeiros 4 MiB; localização exata das instruções; table qwords+5 que apontam a saltos E9; JMP e Jcc decodificados; exemplos de emulação sintética com transição CMP→JE→JMP indireto; sobreposição de endereços nas trilhas estáticas.
- **Hipóteses:** a função da tabela de pares, o significado dos campos lidos em [RBP+0x41], [RBP+0x101], [RBP+0x13B], [RBP+0x143], e a relação do RCX real com ImageBase.
- **Não comprovado:** fluxo dinâmico real dos 16 destinos ou de todas as 30 saídas, estado real da pilha e tabela, decoder inteiramente concluído, segundo estágio executado no cliente, CodeRegistration ou MetadataRegistration localizado e backend local compatível.
- O registro antigo de um protótipo de comunicação localhost não significa autenticação compatível ou servidor de jogo funcional.
- Conquistas narrativas deste ciclo: **Cartógrafo dos Saltos (Épica)** para tabela de oito pares de saltos; **Mestre das Bifurcações (Épica)** para 16 primeiros controles decodificados. São marcos da análise, não da implementação do servidor.

## 9. Evolução quantitativa e qualitativa frente ao 900
- **Cobertura objetiva** da `.vdata`: 524.288 → 4.194.304 bytes = 8× a quantidade de bytes; de **3,710% para 29,681%** do espaço virtual declarado, aumento de cerca de **25,971 pontos percentuais de cobertura de bytes**. Não são pontos de avanço geral do software.
- **Conhecimento de fluxo de controle:** de cadeias iniciais parcialmente fora de prefixo (900) a 94 instruções e 115 instruções emuladas sob condições sintéticas, 16 destinos, 15 testes condicionais e 30 saídas analisadas estaticamente (957).
- **Percentuais de progresso técnico** do checkpoint 900 (geral ~34%, subjetivo) permanecem **baseline histórica**, sem atribuir novo percentual inventado ao 957. O marco 1000 fará revisão formal. Backend compatível e jogo offline funcional **não foram demonstrados**.
- Não existem evidências nesta documentação para prometer uma data ou percentual preciso de conclusão.

## 10. Retomada exata em outro chat
1. Consultar `README.md`, `docs/BACKUP_TECNICO_PASSO_900.md`, este documento e `docs/CHECKPOINT_900.md`.
2. **Último passo aprovado: 957** com `MapeamentoExpandido=APROVADO`, `ConvergenciasLocaisCandidatas=15`, `Controles_JCC=26`, `Controles_JMP=4`.
3. **PASSO 958 ainda NÃO enviado nem executado**. Antes de propor próximo código, confirmar que o backup e atualizações do GitHub estejam efetivamente disponíveis.
4. Próximo estudo sugerido: analisar, **estaticamente**, por que o lado NÃO TOMADO alcança o início da região TOMADA nos quinze casos; determinar os limites e efeitos de cada sub-bloco, distinguir linhas de controle de falsas convergências por linearização, mapear os saltos indiretos de 0x6A90D01 e 0x6A916E0 sem inventar o estado real.
5. Continuar com um script PowerShell completo por vez, não alterar cliente, não presumir autenticação real; checkpoint formal de progresso no passo 1000.
