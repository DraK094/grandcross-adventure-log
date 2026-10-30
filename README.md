# ⚔️ Grand Cross Local — Adventure Log

## 🔎 PASSOS 1041–1044 — Importações e IAT (30/10/2026)

**Último passo auditado: 1044; próximo: 1045, ainda não executado.** As duas versões da GameAssembly.dll importam os mesmos **10 símbolos diretamente**, um por biblioteca. Entre eles, `GetModuleHandleA` e o símbolo de resolução `Baselib_DynamicLibrary_GetFunction` (o nome não prova chamada). A `.vdata` atual, reconstruída e validada por hash, contém **uma ocorrência literal** de RVA `0x06AE0260` no offset `.vdata+0xF189`, que corresponde à célula IAT de `GetModuleHandleA`, porém **sem evidência de uso efetivo**; os outros nove RVAs não tiveram coincidências literais nas duas representações varridas. **Objetivo 2 — inicialização IL2CPP completa: EM ANDAMENTO.** [Auditoria 1041–1043](./docs/PASSOS_1041_1043_IMPORTS_E_REFERENCIAS.md) · [Contexto 1044](./docs/PASSO_1044_CONTEXTO_IAT.md).

---


## 🔐 NOVO CHECKPOINT — PASSO 1036 (30/10/2026)

**Último passo auditado 1036; 1037 NÃO executado.** Na DLL atual (SHA256 `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`), mapeados os blocos estáticos após a nova entrada e laço atômico; encontrada nova instrução de despacho `JMP QWORD PTR [RAX]` em RVA `0x6DF45A0`. A expressão depende dos estados reais de pilha, registradores e memória do cliente, **não resolvidos por bytes estáticos**. **Objetivo 1: 100% da seção `.vdata` atual reconstruída; Objetivo 2: EM ANDAMENTO.** [1028–1030](./docs/PASSOS_1028_1030_LOOP_ATOMICO_ATUAL.md) · [1031–1035](./docs/PASSOS_1031_1035_DESPACHANTE_ATUAL.md) · [1036](./docs/PASSO_1036_DEPENDENCIA_ESTADO.md). Sem comprovação de execução integral ou servidor local funcional.

---


## 🔎 OBJETIVO 2 — STATUS PASSO 1013 (30/10/2026)

**Em andamento — impedimento técnico identificado.** Passos 1010–1013: a DLL exporta 384 nomes (239 com `il2cpp`), incluindo `il2cpp_init` RVA `0x3458B0`, mas esse RVA fica além dos bytes brutos armazenados na sua seção. **356/384** destinos exportados não estão diretamente respaldados por bytes na cópia em disco. Outras seções anteriores à `.vdata` somam **72.529.358 bytes** de excedente virtual sobre raw; isso não significa que esse total seja código recuperável. Para demonstrar toda a inicialização, é necessário identificar o carregamento real de código e os estados de execução, além da `.vdata` decodificada. O segundo check verde **não está justificado**. [Auditoria 1010–1012](./docs/PASSOS_1010_1012_ENTRADAS_IL2CPP.md) · [Mapa PE 1013](./docs/PASSO_1013_MAPA_LACUNAS_PE.md). Próximo: 1014, **não executado**. Sem servidor offline funcional.

---


## 🧩 Metadados recebidos — PASSOS 1007–1009

Cópia `global-metadata.dat` (31.786.920 bytes) validada: assinatura IL2CPP v29, 31 regiões do cabeçalho coerentes, **34.451 definições de tipos, 89 imagens e 89 assemblies**; primeira imagem `Assembly-CSharp.dll` com 20.065 tipos. **Objetivo 2 permanece EM ANDAMENTO**: ainda faltam os registros nativos e comprovação da cadeia de inicialização. [Auditoria 1007–1009](./docs/PASSOS_1007_1009_AUDITORIA_METADATA.md). Próximo: PASSO 1010.

---


## 🧬 OBJETIVO 2 — INICIALIZAÇÃO DO CÓDIGO RECONSTRUÍDO (PASSO 1006)

**Status: EM ANDAMENTO** (não marcar como concluído sem comprovar o caminho completo de inicialização e handoff ao runtime IL2CPP). Passos 1001–1006 aprovados em auditorias estáticas com a DLL original: contador exato **1652** no laço RVA `0x6D81523`, mesmo laço estudado no passo 942; `.boot` calcula base `.vdata` e prepara `JMP RAX` para `.vdata+0x1CC32` após verificar/carregar a seção. Ainda faltam estados dinâmicos, resolução de despachos indiretos e prova de inicialização do IL2CPP.

[1001–1004](./docs/PASSOS_1001_1004_CONTADOR_1652.md) · [1005](./docs/PASSO_1005_UNIFICACAO_LOOP_942.md) · [1006](./docs/PASSO_1006_HANDOFF_BOOT_VDATA.md). **Último passo: 1006; próximo: 1007.**

---


## 🏆 MARCO 1000 — 30/10/2026

📊 **[Relatório especial PASSO 1000 — comparação 800/900/957/959/1000, conquistas e progresso real](./docs/RELATORIO_ESPECIAL_PASSO_1000.md)**



**Último passo validado: 1000 (checkpoint); próximo: 1001.** Passos 975–999: 25 asserções estáticas de bytes e instruções sobre a `.vdata` reconstruída (14.131.200 bytes, SHA256 `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`). Observado laço que opera em QWORDs sucessivos e `JMP QWORD PTR [RAX]`; **destino dinâmico desconhecido**. Não há execução do segundo estágio nem servidor offline funcional comprovado. **100% refere-se apenas à reconstrução dos bytes virtuais da seção.**

**[Relatório formal e evidências PASSO 1000](./docs/CHECKPOINT_1000.md)**.

---


## 🧪 STATUS MAIS RECENTE — PASSO 974 (29/10/2026)
- **PASSOS 966–974 executados e auditados em Python nesta rodada**. Último aprovado: **974**. Próximo reservado: **975 (não executado)**.
- Destino RVA `0x6D80A55`: `CALL +0`; depois instruções que manipulam a pilha e uma sequência `XOR EAX,EAX / LOCK CMPXCHG / JE / PAUSE / JMP` compatível com tentativa atômica repetida.
- Novos controles `0x6D80E42`, `0x6D80FF6`, `0x6D81060`, `0x6D81492`, `0x6D81526`; reconvergências por **inspeção linear estática**, nunca execução real dos dois estados.
- RVA `0x6D8161C`: `JMP QWORD PTR [RAX]`. Os ADD/SUB do trecho anterior cancelam-se, com contribuição `8×RBX` para RAX; **destino real não identificado**.
- [Relatórios 966](./docs/PASSO_966_CALL_ZERO.md) · [967](./docs/PASSO_967_LOOP_ATOMICO.md) · [968](./docs/PASSO_968_CONDICAO_APOS_LOOP.md) · [969](./docs/PASSO_969_CONVERGENCIA.md) · [970](./docs/PASSO_970_RAMOS.md) · [971](./docs/PASSO_971_RECONVERGENCIA_SECUNDARIA.md) · [972](./docs/PASSO_972_DESPACHANTE_QWORD.md) · [973](./docs/PASSO_973_RAMO_RETORNO.md) · [974](./docs/PASSO_974_JMP_INDIRETO.md).
- **Limites:** sem estado dinâmico real do cliente, segundo estágio real não confirmado, sem registros IL2CPP encontrados e **sem servidor offline funcional**. SHA256 da saída integral 13,48 MiB: `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`.

---


## 🔬 STATUS ATUAL — PASSO 962 (29/10/2026)
- **Último passo aprovado: 962. Próximo passo: 963 (não executado).** Trabalhos reproduzidos aqui com DLL enviada pelo usuário, sem modificá-la.
- **PASSO 959:** reconstrução integral em Python puro de 14.131.200 bytes da seção `.vdata` (13,48 MiB) com marcador final, SHA256 `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`. 100% **da cobertura de bytes da seção**, não do projeto/servidor.
- **PASSOS 960–961:** destinos das duas CALLs antes fora de alcance decodificados. Sob o estado de pilha hipotético, a cadeia permite calcular a base da seção `.vdata` e a base PE, mas **a execução real não foi comprovada**.
- **PASSO 962:** trampolins `0x6D91789 → 0x6ABF4B0 → 0x6DA5F72`, parada em `MOV RAX,RAX`, sem execução do destino.
- Documentação: [957](./docs/BACKUP_TECNICO_PASSO_957.md) · [959](./docs/PASSO_959_RECONSTRUCAO_INTEGRAL.md) · [960](./docs/PASSO_960_CHAMADAS_RESOLVIDAS.md) · [961](./docs/PASSO_961_CALCULO_IMAGEBASE.md) · [962](./docs/PASSO_962_TRAMPOLINS.md).
- **Sem CodeRegistration/MetadataRegistration validados, sem segundo estágio efetivamente executado e sem servidor offline funcional.**

---


## 🛡️ ESTADO ATUAL — PASSO 957 APROVADO (29/10/2026)
- **Último passo executado e validado: 957.** **PASSO 958 ainda não iniciado**; intervalo reservado para realizar backup e auditar o repositório.
- **[BACKUP TÉCNICO DETALHADO DOS PASSOS 900–957](./docs/BACKUP_TECNICO_PASSO_957.md)** — endereços, hashes, descrição dos experimentos, mapas dos 16 destinos, 15 controles, 30 saídas, 15 convergências estáticas e instruções de retomada. Não inclui binários nem a coleção integral dos scripts/logs.
- Prefixo de **4.194.304 bytes (4 MiB)** de `.vdata` recuperado repetidamente; SHA-256 `b69ef8861b20e6cbc4111bc4137ac5b67b3c598054af76e53f737072280d67ac`. Cobertura de bytes declarados da seção: **29,681%**, em comparação a 3,710% no passo 900. **Não é percentual de servidor pronto.**
- PASSO 949: comparação real `CMP/J E` validada por 4 cenários emulados (2 saltos tomados, 2 não tomados); PASSO 950: integração de 115 instruções e salto indireto para 3 destinos artificiais.
- PASSOS 951–953: tabela de **8 pares** de RVAs que apontam a **16 instruções `JMP rel32` consecutivas** e 16 destinos distintos dentro do prefixo recuperado.
- PASSOS 954–955: os 16 destinos têm primeira transferência mapeada, **15 Jcc (10 JBE, 5 JE) e 1 RET**. PASSO 956: 30 saídas estáticas. PASSO 957: **30/30 trajetos**, 26 observações JCC, 4 JMP e **15/15 pares com endereços de instrução comuns**, sem prova de execução dinâmica real.
- **Limites:** decoder completo/segundo estágio real ainda não demonstrados; `CodeRegistration` não localizado; nenhum servidor offline compatível/jogável. O backup é documental; não contém assets proprietários, credenciais ou código original.
- **Marco formal seguinte:** 1000. Estimativa histórica geral ~34% no marco 900 é **subjetiva e não foi atualizada artificialmente** no 957.

---


Diário público de investigação independente do cliente PC de **Seven Deadly Sins: Grand Cross**. Não afiliado à Netmarble.

## 🏰 Estado atual — CHECKPOINT 900 APROVADO (29/10/2026)
- **Último passo executado e validado: 900**.
- **Passo 901:** script de reconstrução de 1 MiB entregue, **ainda não executado**.
- **Próximo checkpoint:** 1000.
- **[Relatório e tabela comparativa 800 → 900](./docs/CHECKPOINT_900.md)**.
- **[BACKUP TÉCNICO DE RETOMADA — PASSO 900](./docs/BACKUP_TECNICO_PASSO_900.md)** (documentação de conhecimento; não é backup dos binários, scripts completos ou assets).
- [Backup do marco 800](./docs/CHECKPOINT_800.md) · [Backup técnico anterior, passo 720](./docs/BACKUP_TECNICO_PASSO_720.md) · [Painel web](./index.html).

### Tabela dos checkpoints
| Marco | Progresso técnico geral estimado | Diferença |
| --- | ---: | ---: |
| 600 | 25% | — |
| 700 | 28% | +3 p.p. |
| 800 | ~31% | +3 p.p. |
| 900 | **~34% (provisório)** | **~+3 p.p.** |

**Atenção:** os percentuais acima são estimativas **qualitativas e subjetivas do conhecimento técnico**, não frações do software pronto. O avanço quantitativo verificável é **524.288 / 14.131.200 bytes (3,710%) do espaço virtual .vdata** recuperados como prefixo. Nenhum servidor offline compatível ou jogável foi validado.

### Evolução por área · 800 → 900 (estimativas qualitativas)
| Área | 800 | 900 | Δ |
| --- | ---: | ---: | ---: |
| Ambiente e ferramentas | 95% | 96% | +1 p.p. |
| Metadados IL2CPP | 95% | 95% | 0 |
| Formato PE e GameAssembly | 84% | 89% | +5 p.p. |
| Arquivos Unity e recursos | 68% | 68% | 0 |
| Protocolo e mensagens | 58% | 58% | 0 |
| Sistema de missões | 38% | 38% | 0 |
| Inicialização do boot | 35% | 60% | +25 p.p. |
| Autenticação local | 9% | 9% | 0 |
| Backend e servidor offline | 0% | 0% | 0 |
| Jogo offline funcional | 0% | 0% | 0 |

A reavaliação de boot mede capacidade de análise e emulação do descompressor, não prova execução do segundo estágio. O valor geral não é média dos percentuais por área.

### Evidências do passo 900
- Descompressor .boot mapeado; 4 rotas REP MOVSB; 27/27 cópias sobrepostas testadas nos primeiros 128 KiB.
- Prefixo de **512 KiB** reproduzido com SHA256 `8dbae2603dd37c17c6717167401d1c9d673a4178e59cabdd767612cf26f5eb19`; hashes de 128/256 KiB igualmente confirmados.
- Monitoramento híbrido validado: parada exata; RIP `0x1877FD1A5`, RSI `0x186AFA61B`, RDI `0x186B03000`, excedente 0; tempo 3,576512 s no PASSO 900.
- Implementação alternativa em Python preservou hashes mas foi mais lenta no benchmark end-to-end; modo híbrido reduziu custo de monitoramento.
- **Ainda não comprovados:** saída integral, execução do segundo estágio, CodeRegistration, MetadataRegistration, login real e servidor jogável.

## Histórico pré-checkpoint 900

## Histórico — marco 800 auditado (29/10/2026)
- **Último passo concluído: 800**; auditoria integral com resultado OK.
- **Próximo passo: 801**, script *Inventário Arquitetural* entregue e **ainda não executado**.
- **Próximo checkpoint formal: 900**.
- Servidor local funcional: **não implementado**.
- **[Backup de retomada do marco 800](./docs/CHECKPOINT_800.md)**. Contexto detalhado anterior: [backup técnico até passo 720](./docs/BACKUP_TECNICO_PASSO_720.md).
- Painel [index.html](./index.html) atualizado para o marco 800.

### Marcos e comparação correta
| Marco | Progresso técnico geral estimado |
| --- | ---: |
| 600 | 25% |
| 700 | 28% |
| 800 | ~31% |

As porcentagens são **estimativas qualitativas**, não progresso de software funcional. Os valores individuais do marco 600 não foram recuperados e não devem ser inventados; por área a comparação fundamentada é **700 vs. 800**.

### Áreas — marco 700 → 800
| Área | 700 | 800 |
| --- | ---: | ---: |
| Ambiente e ferramentas | 95% | 95% |
| Metadados IL2CPP | 90% | 95% |
| Formato PE e GameAssembly | 82% | 84% |
| Arquivos Unity e recursos | 65% | 68% |
| Protocolo e mensagens | 45% | 58% |
| Sistema de missões | 38% | 38% |
| Inicialização do boot | 35% | 35% |
| Autenticação local | 5% | 9% |
| Backend e servidor offline | 0% | 0% |
| Jogo offline funcional | 0% | 0% |

### Auditoria de metadados — passo 800
- IL2CPP v29: 34.451 TypeDefs, 262.861 MethodDefs, 200.338 Fields, 2.800 GenericContainers, 4.232 GenericParameters.
- `SyncPacketBase<T>`: TypeDef 12874, contêiner 333; `SyncPacketMarshaler<T>`: TypeDef 12875, contêiner 334. Parâmetro T confirmado em ambas.
- PvP: 16 classes, 22 campos, 32 métodos. Destroy: 17 classes, 27 campos, 35 métodos. Total: 33 classes, 49 campos, 67 métodos.
- 33 identificadores de pacotes decodificados no passo 792, sem validação de formato na rede.
- Marshalers concretos localizados; descritores genéricos concretos, corpos de métodos, serialização e protocolo funcional pendentes.

### Próxima fase
Investigar inventário arquitetural e planejar protótipo **independente**. O PASSO 801 aguarda saída do PowerShell 5.1 do usuário. Cada passo é read-only, autossuficiente e validado antes do próximo. Não versionar binários, assets proprietários, chaves ou credenciais.

---
## Histórico anterior preservado

# ⚔️ Grand Cross Local — Adventure Log

Diário público de investigação técnica do cliente PC de **Seven Deadly Sins: Grand Cross**. Projeto independente, não afiliado à Netmarble.

## Estado atual — análise até o passo 720 (marco 700 auditado)
- **Último passo concluído: 720**.
- **Próximo passo preparado: 721 (ainda não executado)** — validar formatos compactado-4 e F0-UInt32LE com cinco constantes XXHash32.
- **Próximo relatório formal: passo 800**.
- **Marco 700 concluído** com auditoria estrutural do metadata IL2CPP.
- **Nenhum servidor offline compatível e funcional** implementado ou validado.

## Painel e comparação histórica
A página [index.html](./index.html) inclui o painel de progresso, o histórico técnico e a comparação entre os marcos 600 e 700.

| Indicador | Marco 600 | Marco 700 |
| --- | ---: | ---: |
| Progresso geral estimado | 25% | 28% |
| Diferença | — | +3 pontos percentuais |

Os percentuais são **estimativas qualitativas de acompanhamento**, não medidas objetivas de software implementado. Os **dez percentuais individuais do marco 600 não foram recuperados**; o painel apresenta os valores registrados no marco 700, sem inventar diferenças históricas por área.

### Valores registrados no marco 700

| Área | Estimativa |
| --- | ---: |
| Ambiente e ferramentas | 95% |
| Metadados IL2CPP | 90% |
| Formato PE e GameAssembly | 82% |
| Arquivos Unity e recursos | 65% |
| Protocolo e mensagens | 45% |
| Sistema de missões | 38% |
| Inicialização do boot | 35% |
| Autenticação local | 5% |
| Backend e servidor offline | 0% |
| Jogo offline funcional | 0% |

## Descobertas confirmadas até o passo 701
- Metadata IL2CPP v29: **34.451 TypeDefinitions**, **262.861 MethodDefinitions**, **240.898 parâmetros**, **200.338 campos**, **16.530 entradas de interface**, **2.800 contêineres genéricos**, **4.232 parâmetros genéricos**, **89 images** e **89 assemblies**.
- Definição **System.Collections.Generic.IEnumerator`1** identificada em **TypeDef 25068** (ByValTypeIndex **35455**); contêiner genérico **1065**, com parâmetro **T** em **1518**, posição **0**. A auditoria corrigiu uma interpretação incorreta do deslocamento do contêiner.
- **3.746 classes** com interface TypeIndex **11115** e o trio de interfaces consistente; **3.726** com padrão `d__` e **20** com padrão `c__Iterator`. A associação de TypeIndex 11115 a uma instanciação de `IEnumerator<object>` é **hipótese fortemente sustentada, não resolução direta**.
- **11 classes** de comunicação e autenticação localizadas, incluindo `NetmarbleS.SessionPlatform`, `NetmarbleS.Auth`, `WestSidePacketManager`, `RelayPacketManager` e proxies.
- **Passo 701:** **102 métodos** catalogados em sete classes de sessão, conexão e fluxo. Nomes de métodos **não comprovam a ordem real de execução**.
- Marcos anteriores preservados: **70/70** cabeçalhos UnityFS internos validados; **734** membros `TableType`; **1.165 IDs C2S** e **624 IDs S2C** catalogados.
- Análise PE anterior: `GameAssembly.dll` x64, seção `.vdata` virtual sem dados físicos e seção `.boot` RX. A origem do conteúdo de `.vdata` em execução permanece indeterminada.

## Backup para continuidade em outras conversas

**[📚 Backup técnico completo do conhecimento recuperado até o PASSO 720](./docs/BACKUP_TECNICO_PASSO_720.md)** — documentação detalhada com contexto do projeto, caminhos locais, ferramentas, estruturas IL2CPP, offsets, classes de rede, enums, constantes, validações, hipóteses e roteiro de retomada. Não inclui os 720 scripts integrais, logs completos ou binários.

**Decisão em 29/10/2026:** manter a análise técnica somente leitura até o **PASSO 800**; nesse marco, além do relatório e atualização do painel, começar a **arquitetura experimental para testes locais**. O PASSO 721 já foi entregue e aguarda saída do PowerShell. Nenhum servidor local foi implementado.

**Passos 712–720:** defaults de ConnectionState 0/1/2; testes 22/22 no passo 716; negativos confirmados 3/3 no passo 718; 46.060 defaults auditados no passo 719, 396 primeiros bytes E0–FF (227 F0); passo 720 confirmou quatro constantes XXHash32 com F0 + UInt32LE, enquanto PRIME32_5 começa com D6 e provavelmente usa formato compactado-4. Não anunciar 5/5 antes de executar 721.

## Limitações e próximas investigações
A análise estática do cliente **não equivale** a autenticação local, implementação de backend ou jogo offline funcional. A sequência real de inicialização, a semântica das mensagens e as dependências do servidor permanecem pendentes.

**Próximo passo (721):** executar o script já entregue e conferir as cinco constantes XXHash32; resultado do passo 720 foi 4/5 por pressupor incorretamente F0 universal.

## Segurança e direitos
Não publicar binários do jogo, assets proprietários, chaves, credenciais ou dados privados. Este repositório contém somente documentação técnica e um painel independente.

## Atualizações
O site é HTML/CSS/JavaScript sem dependências. Atualizações no GitHub exigem commits; executar PowerShell no computador não sincroniza automaticamente com este repositório.
