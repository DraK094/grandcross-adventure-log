# PASSOS 1001–1004 — Identificação do contador de preparação da memória

**Data:** 30/10/2026. **Aprovados:** 1001,1002,1003,1004. **Próximo 1005 ainda NÃO executado.** Análise estática auditada via Python da seção .vdata 14.131.200 bytes (SHA-256 `60c9b60dde83be7e274dd2a1355fe45bc1cce8a4cc31916a5c8759da66cc8ad3`).

| Passo | Teste | Resultado |
|---|---|---|
| 1001 | JE em RVA `0x6D81492` | Condição pode desviar para `0x6D815BE`; caso contrário, segue para `0x6D81498` |
| 1002 | Redução das constantes 32-bit RVAs `0x6D814BB`–`0x6D81508` | `EBX = 0x674 = 1652` na trajetória sem desvio, **independente dos valores iniciais dos registradores sobrescritos** |
| 1003 | Laço RVAs `0x6D81523`–`0x6D8156E` | Com memória válida e execução completa, **1652 iterações**, 8 bytes por passo, intervalo de 13216 bytes; `[RAX+8i] += RCX` módulo 2^64 |
| 1004 | Caminho alternativo até `0x6D8161C` | O índice RBX é reobtido da pilha e o alvo `JMP [RAX]` segue **não resolvido sem estado real** |

## Evidência matemática do PASSO 1002
```python
m = 0xffffffff
r10 = (0x7cdf5677 + 1) & m
esi = (0x6f6f20a1 & 0x7ecff358)
esi = ((esi + 0x6bb759d2) & m) ^ 0xe4d315b7
r10 ^= esi
r10 = ((r10 << 3) & m)
r10 = (r10 - 0xb512b43a) & m
ebx = (0x5b3f504e + 0x0dfb3cd8 - r10 - 0x0dfb3cd8) & m
ebx >>= 3
assert ebx == 1652
```
**Correlação histórica inédita:** o número 1652 também havia surgido no PASSO 942 (laço de 1652 elementos sob estado sintético). **É correspondência de contagem; não prova que os dois laços sejam o mesmo fluxo de execução ou tenham mesmos endereços**.

## Limites
O caminho **não tomado** do JE `0x6D81492` tem contador fixo; o caminho tomado desvia a preparação e chega a operações dependentes da pilha. A soma em memória supõe entradas válidas, sem interrupções, e não comprova alterações no cliente real. Análise estática e cálculo de constantes **não demonstram** inicialização completa, transferência ao runtime IL2CPP, CodeRegistration ou MetadataRegistration.

**O objetivo número 2 do checkpoint 1000 — “Compreender a inicialização do código reconstruído” — continua EM ANDAMENTO.** Transformá-lo em Concluído exigirá encadear entrada real, estados, efeitos de pilha/memória e handoff verificável à inicialização IL2CPP. Não alterar o rótulo antes disso.

## Próximo estudo
PASSO 1005: investigar separadamente a trajetória condicional que salta em 0x6D81492 e a origem dos valores de pilha nos destinos de despacho. Se os registros forem suficientes, buscar a origem da base de relocação usada nas 1652 operações. Arquivo `global-metadata.dat` pode ser útil para futura validação de registros IL2CPP, mas não é requisito para concluir estes quatro passos.

Sem publicação de DLL ou bytes proprietários.
