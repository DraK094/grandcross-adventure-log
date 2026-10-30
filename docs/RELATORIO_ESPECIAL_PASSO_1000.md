# GRANDCROSS LOCAL — RELATÓRIO ESPECIAL DO CHECKPOINT 1000

**30/10/2026 · Último passo aprovado: 1000 · Próximo: 1001, não executado**

## Visão geral
Marcação histórica de 1000 etapas numeradas; **a realização técnica mais importante é a recuperação integral da seção virtual `.vdata`**, com hash verificável e marcador de término do fluxo comprimido. A análise prosseguiu até um laço de escrita de QWORDs e despacho indireto. **Ainda não houve validação de execução real do segundo estágio nem servidor de jogo offline funcional**.

## Comparativo de cobertura — dado objetivo
| Marco | Bytes reconstruídos | Cobertura da .vdata | Principais resultados |
|---|---:|---:|---|
| 800 | Sem base comparável consolidada | — | Investigação preliminar, logs históricos |
| 900 | 524.288 (512 KiB) | 3,710% | Unicorn, hash e monitoramento híbrido |
| 957 | 4.194.304 (4 MiB) | 29,681% | 8 pares de RVA, 16 JMP, 30 saídas de fluxo |
| 958 | 4.194.304 | 29,681% | Descompressor Python independente reproduz hash |
| 959 | 14.131.200 (13,48 MiB) | **100%** | Terminador encontrado e digest integral |
| **1000** | **14.131.200** | **100%** | Auditoria de 25 instruções e síntese de fluxo |

A cobertura cresceu **26,953125×** de 900 a 1000; 900→957 = 8× e 957→959 = 3,369140625×. São **bytes virtuais reconstruídos**, não progresso de servidor.

## Ambiente e evidência
- DLL original Windows x64, 47.199.760 bytes, Unity 2022.3.27f1, IL2CPP metadata v29.1 (segundo os logs).
- ImageBase `0x180000000`; `.vdata` RVA `0x06A83000`, VA `0x186A83000`, virtual size 14.131.200, raw size zero.
- `.boot` RVA `0x077FD000`, raw offset `0x02553800`, 8.060.416 bytes.
- SHA-256 4 MiB: `b69ef8861b20e6cbc4111bc4137ac5b67b3c598054af76e53f737072280d67ac`.
- SHA-256 integral da `.vdata`: `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`.
- PASSO 959: 14.131.200 bytes recuperados em **4,824181 s** (execução Python observada) e terminador intrínseco identificado. PASSO 957: emulação Unicorn dos 4 MiB em 27,800777 s; PASSO 900: 512 KiB em 3,576512 s. **Tempos de ambientes diferentes; não são benchmark comparável**.

## Como mudou o trabalho?
| Dimensão | PASSO 900 | PASSO 1000 |
|---|---|---|
| Motor principal | Unicorn no Windows | Python puro para recuperação e análise estática |
| Limite reconstruído | 512 KiB | Seção completa, 13,48 MiB |
| Fim da descompressão | Não observado | Marcador final intrínseco |
| Chamadas fora do prefixo | Não decodificáveis | Destinos e trampolins decodificados |
| ImageBase | Relação matemática proposta | Caminho estático de CALL/JMP/POP/SUB documentado |
| Fluxo | Trechos iniciais | Loops atômicos, desvios, pilha e despacho indireto |
| Ação no PC do usuário | Necessária frequentemente | Não necessária para muitas auditorias |
| Backend jogável | Não demonstrado | Não demonstrado |

## Descobertas por período
- **885–900:** CALL/POP e ImageBase proposto; hashes 128/256/512 KiB; cópias sobrepostas; monitoramento híbrido do decoder.
- **942–950:** emulação de 94/115 instruções com estados **sintéticos**; CMP/JE; destino de tabela artificial.
- **951–957:** 8 pares adjacentes de qwords apontando a 16 JMPs; 15 Jcc e um RET; 30 saídas, 15 convergências **lineares**, não execução real.
- **958–959:** implementação independente em Python puro, reproduz hash de 4 MiB e recupera integralmente a `.vdata`.
- **960–965:** duas CALLs fora do prefixo agora decodificadas, cadeia de base PE/section, trampolins; 3 `POP RSP`, salto para `0x6D80A55`.
- **966–974:** `CALL +0`, loop `LOCK CMPXCHG` + `PAUSE`, JE e reconvergências; `JMP QWORD PTR [RAX]` em `0x6D8161C`.
- **975–999:** 25 asserts de bytes/instruções, incluindo laço `TEST RBX,RBX`, `JE`, `ADD QWORD [R13],RCX`, `ADD RAX,8`, `SUB EBX,1`, `JMP`; leituras de `GS:[0x188]` e `GS:[0x30]`; cancelamento algébrico de constantes em torno de `ADD RAX,8×RBX`.
- **1000:** checkpoint, comparação histórica e balanço honesto, **não um módulo novo do servidor**.

## Mapa resumido do despacho
```asm
0x6D81523: TEST RBX,RBX
0x6D81526: JE 0x6D81573
0x6D81555: ADD QWORD PTR [R13],RCX
0x6D81567: ADD RAX,8
0x6D8156B: SUB EBX,1
0x6D8156E: JMP 0x6D81523
...
0x6D815E5: SHL RBX,3
            ADD/SUB que se cancelam em pares
            ADD RAX,RBX
0x6D8161C: JMP QWORD PTR [RAX]
```
**Hipótese:** possível preparação de tabela de ponteiros, sem prova do conteúdo ou dos destinos. A leitura de `[RSP+0x88]` e o índice RBX dependem da pilha real; a álgebra local não pode ser aplicada cegamente a todo o percurso. O caminho CALL/POP/SUB calcula as bases **somente se a pilha tiver os retornos esperados**.

## Avaliação formal: análise e servidor são coisas diferentes
| Área | PASSO 900 | PASSO 1000 | Estado de certeza |
|---|---|---|---|
| Recuperação da `.vdata` | 3,710% | **100%** | Medição de bytes |
| Análise estática | Parcial | Parcial mais profunda | Sem cobertura global |
| Inicialização real do segundo estágio | Não | Não | Pendente |
| CodeRegistration / MetadataRegistration | Não validados | Não validados | Pendente |
| Protocolo/autenticação/gameplay reais | Não validados | Não validados | Pendente |
| Servidor offline funcional | Não demonstrado | **Não demonstrado** | 0% funcional validado; % global **indeterminado** |

As estimativas históricas 600=25%, 700=28%, 800≈31%, 900≈34% eram avaliações **subjetivas de investigação**, não taxas mensuradas do backend. **Não atribuir percentual global artificial ao PASSO 1000.**

## Conquistas narrativas
- **Cartógrafo dos Saltos (Épica):** pares RVA e 16 saltos.
- **Mestre das Bifurcações (Épica):** 16 controles, 30 saídas.
- **Quebrador de Correntes (Lendária):** decoder Python puro validado contra 4 MiB.
- **Libertador da .vdata (Lendária):** reconstrução integral e terminador.
- **O Marco Milenar (Lendária):** fechamento de 1000 etapas documentadas.

## Próxima etapa 1001 (não executada)
Rastrear `[RSP+0x88]`, `RBX`, `RAX` e os valores GS; determinar pré-condições para `JMP [RAX]`; exigir evidência dinâmica **somente** quando indispensável. Usuário oferece outros arquivos se necessários: solicitar nome e caminho exatos. Nunca publicar DLL, saída reconstruída ou arquivos proprietários no GitHub.

## Procedência
[Backup 900](BACKUP_TECNICO_PASSO_900.md) · [Backup 957](BACKUP_TECNICO_PASSO_957.md) · [Descompressão integral 959](PASSO_959_RECONSTRUCAO_INTEGRAL.md) · [Desvio 972](PASSO_972_DESPACHANTE_QWORD.md) · [Auditoria 1000](CHECKPOINT_1000.md). **Lacuna declarada:** não estão disponíveis todos os logs intermediários 901–945; nenhuma auditoria individual é inventada.
