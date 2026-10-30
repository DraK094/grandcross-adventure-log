# PASSO 1057 — Comparação de sockets em duas telas

Usuário executou consulta PowerShell com jogo parado na taverna e depois abrindo menu de personagens/inventário. Ambas as amostras mostraram as mesmas três entradas Established para o PID do 7dsgc:

- `127.0.0.1:50789 -> 127.0.0.1:50790`
- `127.0.0.1:50790 -> 127.0.0.1:50789`
- `192.168.1.106:59142 -> 43.174.218.165:23071`

`Compare-Object` não retornou diferenças. **PASSO 1057 APROVADO apenas para comparação de lista de sockets.** Não demonstra tráfego efetivo, protocolo, função dos serviços nem compatibilidade de servidor local.

Próxima ação recomendada: avançar de inventário de sockets para identificação de transporte e eventuais logs/arquivos de configuração documentados, utilizando inspeção não invasiva. Não afirmar que alterar opções de região assegura a adição de um servidor local.