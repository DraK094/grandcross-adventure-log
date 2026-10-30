# GrandCross Local — PASSOS 1170–1174

## Evidência principal

Cruzamento reproduzível da tabela de parâmetros de `Auth_PacketHandler` com a lista de sobrecargas `CommonPacket.Marshaler.Write` no metadata IL2CPP v29 atual. A integridade do metadata foi verificada por SHA-256 antes do cruzamento.

| Handler | Parâmetro | Índice de tipo `Write` | Token `Write` | Token `Read` seguinte | Índice de tipo `Read` |
|---|---|---:|---|---|---:|
| CG_RequestLoginOK | userInfo | 40152 | `0x600328c` | `0x600328d` | 22543 |
| CG_RequestLoginOK | loginServiceInfo | 40148 | `0x6003292` | `0x6003293` | 22542 |
| CG_RequestLoginInstantlyOK | sendDailyReset | 50187 | `0x600343e` | `0x600343f` | 23063 |
| CG_RequestLoginInstantlyOK | loginServiceInfo | 40148 | `0x6003292` | `0x6003293` | 22542 |
| CG_RequestNetmarbleAuthOK | info | 41435 | `0x600327a` | `0x600327b` | 22608 |
| CG_RequestAuthenticateCreateOK | info | 41435 | `0x600327a` | `0x600327b` | 22608 |

## PASSOS
**1170:** comparação automatizada de índices de tipos de parâmetros dos handlers de autenticação com sobrecargas `Write`.

**1171:** coincidência exata única encontrada para `userInfo` (40152) e `loginServiceInfo` (40148), em `CommonPacket.Marshaler.Write`.

**1172:** para cada sobrecarga `Write` correspondente há um método `Read` subsequente, com token diferente e tipo de parâmetro distinto. A associação como par estrutural é confirmada pela adjacência; sua semântica de execução não foi validada.

**1173:** também foram encontradas correspondências para `sendDailyReset` e os parâmetros `info`; não houve correspondência nas sobrecargas dessa classe para `remote`, `rmiContext` ou `sessionKey`, o que **não** significa que esses dados não sejam serializados por outro caminho.

**1174:** auditoria dos limites. Nenhum ID RMI numérico, nenhuma implementação de marshalling em código nativo, nenhum frame binário real ou conexão cliente-servidor foi recuperado.

## Conclusão

Identificamos ligações concretas entre parâmetros de mensagens de login e sobrecargas de `CommonPacket.Marshaler`. Ainda não reproduzimos bytes nem comprovamos o fluxo real de login.

Próximo passo: 1175 — resolver tipos e implementações de `Write`, sem confundir índices de tipos com índices de definições.