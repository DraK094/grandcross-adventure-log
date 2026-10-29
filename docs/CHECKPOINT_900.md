# CHECKPOINT 900 — Grand Cross Local (29/10/2026)

**PASSO 900 executado e aprovado. PASSO 901 preparado mas NÃO executado.**

## Comparação histórica e critérios
| Marco | Progresso técnico geral qualitativo | Delta |
| --- | ---: | ---: |
| 600 | 25% | — |
| 700 | 28% | +3 p.p. |
| 800 | ~31% | +3 p.p. |
| 900 | **~34% (estimativa provisória)** | **~+3 p.p.** |

**Interpretação:** o 34% é uma estimativa editorial qualitativa e revisável para acompanhamento do **conhecimento técnico obtido**, não uma medição quantitativa da engenharia reversa nem percentual de backend implementado. Para software jogável, **nenhum percentual confiável está disponível**. A única cobertura objetiva de bytes é o prefixo de 524.288/14.131.200 = **3,710% do espaço virtual de .vdata**.

### Tabela 800 × 900 por frente
Os valores do marco 800 foram copiados do registro anterior. As posições do 900 abaixo são **avaliações qualitativas provisórias**, feitas apenas para permitir comparação histórica. Valores inalterados não significam ausência de investigação.

| Frente | Marco 800 | Marco 900 (estimativa) | Mudança |
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

A avaliação elevada de **inicialização do boot** reflete a descoberta e execução emulada do descompressor original e a reconstrução do prefixo, **não** a execução final do código carregado. A avaliação de PE reflete offsets/estrutura e análise estática do salto e do cálculo de base. O progresso geral é julgamento independente, não média dessas dez frentes.

## Evidências novas do ciclo 801–900
- Descompressor `.boot` identificado; 4 rotas `REP MOVSB`, 157 instruções, 30 desvios, 5 retornos ao laço; cópias sobrepostas necessárias.
- Reconstrução em memória da `.vdata` até **512 KiB** com hash replicável e testes de cobertura/leitura nas execuções auditadas.
- Hashes: 128 KiB `ad5181b326ea0e993bbb669ac0fa154d88d63706dc9c093ca56e2b1107c7f34e`; 256 KiB `805b7aa5b0262d82aedef06afb42c658fe182133d18fcaf3d1efff2e9aa68357`; 512 KiB `8dbae2603dd37c17c6717167401d1c9d673a4178e59cabdd767612cf26f5eb19`.
- 27/27 cópias sobrepostas dos primeiros 128 KiB verificadas sem divergências (PASSO 891).
- Protótipo acelerado 910/910 microtestes; integrado aos 512 KiB com hashes idênticos, mas benchmark cruzado confirmou pior desempenho do que original (+26,039% de tempo, PASSO 896).
- Monitoramento amostrado obteve ~4,28× de aceleração versus modo leve no PASSO 898, mas excedeu meta em 34 bytes.
- Monitoramento híbrido preservou hashes e **parada exata** (PASSOS 899–900). PASSO 900: 3,576512s, 51.484 consultas RDI, RIP `0x1877FD1A5`, RSI `0x186AFA61B`, RDI `0x186B03000`, excedente zero.
- Relação estática entre endereço de retorno da segunda CALL e ImageBase validada matematicamente (PASSO 885), mas **cadeia não executada**. CALLs `.vdata+0x1C2E97` e `.vdata+0x1A3A19` ainda fora do prefixo.

## O que NÃO está concluído
Descompressão integral e tamanho final real desconhecidos; segundo estágio não executado; `CodeRegistration`/`MetadataRegistration` não localizados; protocolo real não validado; nenhum login real em servidor experimental; nenhum servidor jogável. Prototipagem de endpoints não corresponde a backend compatível.

## Metas 901–1000
1. Aumentar prefixo recuperado (PASSO 901 já preparado para 1 MiB; NÃO executado).
2. Verificar hashes e integridade independente de cada novo intervalo.
3. Recuperar regiões necessárias para analisar CALLs remotos e transições reais.
4. Procurar `CodeRegistration`/`MetadataRegistration` apenas com evidência.
5. Prosseguir com relatório formal no passo 1000.

## Backup de retomada
[BACKUP_TECNICO_PASSO_900.md](BACKUP_TECNICO_PASSO_900.md) contém contexto técnico e offsets, paths, hashes, decisões e regras de retomada. O backup é **documental**, não copia binários, scripts históricos integrais ou recursos proprietários.

**Somente leitura nos experimentos; nenhuma alteração dos arquivos oficiais.**