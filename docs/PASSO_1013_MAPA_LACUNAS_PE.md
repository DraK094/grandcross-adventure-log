# PASSO 1013 — Inventário de lacunas virtuais do PE

**Aprovado por leitura estática da tabela de seções, 30/10/2026.** Próximo: **1014, ainda não executado**. Objetivo 2: **EM ANDAMENTO**.

A DLL recebida descreve seções virtuais que não são integralmente respaldadas por dados brutos no arquivo. Para seções anteriores à `.vdata`, a soma de `max(0, VirtualSize - SizeOfRawData)` é **72.529.358 bytes** (aproximadamente 69,17 MiB). É **tamanho de lacunas de mapeamento**, não tamanho de dados definitivamente recuperáveis ou código faltante executável.

| RVA inicial da seção | VirtualSize | SizeOfRawData | Excedente virtual |
|---|---:|---:|---:|
| 0x1000 | 4.444.156 | 1.333.248 | 3.110.908 |
| 0x43E000 | 77.919.356 | 29.758.976 | 48.160.380 |
| 0x4E8E000 | 15.301.658 | 4.343.808 | 10.957.850 |
| 0x5D26000 | 8.698.012 | 1.564.672 | 7.133.340 |
| 0x6572000 | 3.706.260 | 2.070.016 | 1.636.244 |
| 0x68FC000 | 1.570.572 | 49.152 | 1.521.420 |
| 0x6A7C000 (.debug) | 4.096 | 1.536 | 2.560 |
| 0x6A81000 (.idata) | 4.096 | 1.024 | 3.072 |
| 0x6A82000 (.tls) | 4.096 | 512 | 3.584 |

As demais seções anteriores à .vdata não têm excedente positivo. Esta conta usa o tamanho virtual declarado, e não a área efetivamente executada no jogo.

**Impasse evidenciado:** `il2cpp_init` RVA `0x3458B0` é nomeado pela tabela PE de exports, mas não tem corpo diretamente mapeável a partir dos bytes brutos dessa seção na cópia em disco. A reconstrução de 100% da `.vdata` não recupera automaticamente essas regiões. O fato de haver espaços virtuais não prova qual mecanismo os preenche, nem que estejam preenchidos em uma execução real.

**Próxima dependência externa:** captura controlada de informações sobre carregamento/mapeamento de regiões na execução de uma cópia do cliente, ou material adicional que documente a materialização de código. Não enviar credenciais, arquivos pessoais ou memória de outros processos; não subir dumps de jogo ao repositório público. Sem comprovação de segundo estágio completo, CodeRegistration ou servidor local jogável.

[PASSOS 1010–1012](PASSOS_1010_1012_ENTRADAS_IL2CPP.md) · [PASSO 1006](PASSO_1006_HANDOFF_BOOT_VDATA.md).
