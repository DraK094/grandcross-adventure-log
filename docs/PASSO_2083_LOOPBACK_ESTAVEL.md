# PASSO 2083 — Loopback TCP persistente (31/10/2026)

**Executado e validado a partir do log PowerShell recebido.** Processo 7dsgc PID 30012, duas amostras separadas por três segundos. Script somente leitura; zero pacotes enviados e zero alterações de memória.

## Amostras 1 e 2: resultados idênticos
- TCP loopback `50789 -> 50790`, Established, ambas as pontas pertencem ao processo `7dsgc`, PID 30012.
- TCP loopback `50790 -> 50789`, Established, mesmo PID.
- Registro local porta `50790`, estado Bound, mesmo PID (não contar como terceira sessão Established).
- Contagem TCP total do PID: Bound=2, CloseWait=1, Established=2.
- Endpoints UDP observados: 0, em ambas as amostras.

## Conclusão e limites
O par de sockets TCP entre portas locais 50789 e 50790 permaneceu ativo durante as duas amostras. Não demonstra qual módulo originou a conexão nem protocolo de aplicação ProudNet; não demonstra handshake com servidor externo ou local e não caracteriza autenticação. Ausência de endpoints UDP nessas duas amostras não exclui uso em outras etapas.

**Próxima investigação recomendada:** auditoria documental/read-only dos exports e importações das DLLs ProudNet e do caminho IL2CPP de inicialização. Não inferir protocolo usando somente portas observadas. Próximo PASSO 2084 ainda não executado. Nenhum servidor funcional demonstrado.
