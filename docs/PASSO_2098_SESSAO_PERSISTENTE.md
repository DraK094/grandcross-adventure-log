# PASSO 2098 — Sessão TCP experimental com estados

Verificado pelo log de execução do usuário: listener de loopback em 127.0.0.1:50277 (porta efêmera dessa execução), uma conexão cliente-servidor, quatro testes aprovados: `GCLOCAL/1 HELLO`→`WELCOME` (estado READY), `PING`→`PONG`, `STATUS`→`STATUS READY` e `BYE`→`GOODBYE` (estado CLOSED). Conexões encerradas ao fim. 4/4 validações.

**Comprovado:** uma sessão TCP experimental suporta múltiplas trocas e transições de estado consistentes. **Não comprovado:** protocolo ProudNet, handshake com o executável Grand Cross, login ou backend do jogo. O cliente oficial não foi utilizado e não houve arquivo modificado. A nomenclatura de servidor local funcional refere-se somente ao protótipo `GCLOCAL/1`.

**Próximo passo 2099:** organizar servidor e cliente locais em scripts independentes e persistentes, adicionar tratamento de mensagens inválidas e comando de parada. Nenhuma integração com o cliente oficial.
