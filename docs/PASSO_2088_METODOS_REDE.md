# PASSO 2088 — Filtro de métodos de conexão e RMI

Resultado executado: metadata v29, 263.448 MethodDefinitions, 80 métodos filtrados em 50 tipos declarantes. O script exibiu apenas 35 tipos; outros 15 ficaram omitidos. Contagens: AttachProxy 2, AttachStub 2, Connect 32, Disconnect 18, FrameMove 2, HasServerConnection 2, ProcessReceivedMessage 11, RmiSend 10, SetEventSink 1.

Quatro RmiSend previamente impressos estão em tipos 8594 (índices 68363/68364) e 8607 (68443/68444); outros RmiSend em 18229 (146667/146668) e 19561 (158769/158770). Sem os nomes de TypeDefinition, não atribuir estes tipos à biblioteca ProudNet.

Progresso: isolados candidatos estruturais. Próximo PASSO 2089: recuperar nomes dos 50 TypeDefinitions diretamente da tabela com validação de header/stride e listar métodos de alta prioridade. Nenhuma chamada real, sessão local ou servidor funcional demonstrados.
