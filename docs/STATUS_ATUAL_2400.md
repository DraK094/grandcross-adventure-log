# GrandCross Local — Estado consolidado até PASSO 2400

**Atualizado em 01/11/2026. Último passo com resultado documentado: 2400. Próximo passo planejado: 2401 (não executado).** Projeto de pesquisa independente sobre o cliente PC Seven Deadly Sins: Grand Cross; não afiliado ao fornecedor.

## Distinção essencial das trilhas
| Área | Evidência estabelecida | Falta comprovar |
|---|---|---|
| Ambiente / arquivos | Cópias privadas de GameAssembly, metadata IL2CPP v29 e duas DLLs ProudNet analisadas | Disponibilidade dos mesmos arquivos em novos ambientes; sempre checar SHA256 |
| IL2CPP | Índices de tipos, classes, parâmetros, campos e vínculos estruturais analisados; 49 handlers e famílias de stub tipados | Registro/chamada real, CodeRegistration/MetadataRegistration completo no runtime |
| Mensagens e delegates do jogo | 24/24 correspondências nominais de Auth com stub; 1.388 tríades com assinaturas compatíveis; exceções analisadas | IDs RMI numéricos verdadeiros, bytes serializados, fluxo/ordem, compatibilidade de versões |
| ProudNet / SWIG | 113 PInvoke comuns com correspondência nominal exata em exportações; contratos de RmiStub e eventos | Fluxo do jogo pela ponte, invocação real e objetos observados |
| Nativo ProudNet | Bytes de três setters de callback verificados; seis trampolins indiretos; duas tabelas .rdata; construção do wrapper RmiStub do grupo B identificada | Construção/uso do grupo A e execução real |
| PE e execução | 384 exports GameAssembly; 28 com bytes raw e 356 sem; diagnóstico Windows MEM_IMAGE/PAGE_EXECUTE_READ para 3 exports; .vdata MEM_COMMIT/RWX | Conteúdo efetivo das páginas, chamadas reais, sequência de bootstrap |
| Backend experimental | Protótipos independentes HTTP/SQLite com cenários locais reportados | Handshake ProudNet, autenticação real, inventário/progresso interoperável, taverna jogável |

**Status do servidor local compatível: NÃO DEMONSTRADO.** Não alegar conclusão, jogabilidade ou porcentagem auditada. A quantidade de passos não expressa percentual de software pronto.

## Marcos recentes por área
- [2210](CHECKPOINT_2210_MAPA_S2C_AUTH.md), [2216](CHECKPOINT_2216_STUBS_TIPADOS.md), [2222](CHECKPOINT_2222_TRIPLAS_MENSAGENS.md), [2242](CHECKPOINT_2242_DELEGATES_TIPADOS.md): mapa do cliente e callbacks declarados.
- [2266](CHECKPOINT_2266_AUDITORIA_PE_EXPORTS.md) contém conclusões antigas; **aplicar obrigatoriamente a [ERRATA 2272](CHECKPOINT_2272_ERRATA_EXPORTS.md)** antes de citá-lo. [2274](CHECKPOINT_2274_PAGINAS_IL2CPP.md): permissões de página em execução, sem leitura de bytes.
- [2288](CHECKPOINT_2288_EXPORTS_PROUDNET.md), [2294](CHECKPOINT_2294_PONTE_SWIG_PROUDNET.md), [2305](CHECKPOINT_2305_PINVOKE_EXPORTS.md), [2310](CHECKPOINT_2310_CONTRATOS_DELEGATE_RMI.md): interface gerenciada/nativa ProudNet.
- [2328](CHECKPOINT_2328_EVENTOS_DELEGATES_TIPADOS.md), [2334](CHECKPOINT_2334_NETCLIENT_EVENT_LINKS.md), [2364](CHECKPOINT_2364_COBERTURA_EVENTOS.md): eventos e tipos.
- [2382](CHECKPOINT_2382_SETTERS_NATIVOS_CALLBACKS.md), [2388](CHECKPOINT_2388_SALTOS_INDIRETOS_CALLBACKS.md), [2393](CHECKPOINT_2393_TABELAS_TRAMPOLINS.md), [2399](CHECKPOINT_2399_CONSTRUCAO_RMISTUB_WRAPPER.md), [2400](CHECKPOINT_2400_GRUPOS_TRAMPOLINS.md): análise de instruções e tabelas nativas.

## Evidência de máquina local trazida pelo usuário (passos 2267–2274)
Processo 7dsgc com GameAssembly carregado; PE32+ SizeOfImage 0x8009000; 14 seções; .vdata VirtualSize 0xD7A000, RawSize 0, flags RWX; .boot possui bytes raw e flags RX. VirtualQueryEx: amostras de .vdata MEM_COMMIT/PAGE_EXECUTE_READWRITE; RVAs de il2cpp_domain_get/init/runtime_invoke MEM_COMMIT/PAGE_EXECUTE_READ/MEM_IMAGE. **Proteção da página não comprova código válido nem chamada executada.**

## Integridade e segurança
Não distribuir DLLs comerciais, metadata integral, conteúdo de conta, tokens, endereços privados, patches destinados a contornar segurança ou dumps de memória. Logs e scripts devem ser sanitizados. Não editar a instalação original. Licenças de terceiros podem restringir uso e redistribuição. Resultados estáticos são hipótese sobre comportamento dinâmico até haver observação independente.

Veja também [roteiro pós-2400](ROADMAP_POS_2400.md) e [índice do projeto](INDICE_CHECKPOINTS_2174_2400.md).
