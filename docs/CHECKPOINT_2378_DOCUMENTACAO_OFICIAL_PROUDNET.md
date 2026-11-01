# GrandCross Local — checkpoint 2378: confirmação externa do SDK ProudNet

Investigação documental adicional, após as análises de metadata IL2CPP e da ponte CSharp do plugin.

**Fontes oficiais do fornecedor (ProudNet):**
- https://docs.proudnet.com/proudnet.eng/proudnet/using_pn/eventhandling — descreve o padrão de eventos/delegates e a associação de um receptor de eventos via SetEventSink.
- https://docs.proudnet.com/proudnet.eng/proudnet/using_pn/server_client/using_client — documenta FrameMove para processar eventos e RMI acumulados no cliente.
- https://docs.proudnet.com/proudnet.eng/proudnet-note/sample — apresenta amostras de registros AttachStub e AttachProxy e de manipuladores de eventos.

**Cruzamento:** as classes presentes no metadata do Grand Cross declaram NetClient/NativeNetClient, AttachProxy, AttachStub, SetEventSink e FrameMove, coerentes com o papel genérico descrito na documentação do SDK. Isso é uma *corroboração externa de semântica da API* — evidência mais independente que apenas relacionar nomes internos.

**Limitação:** a documentação do SDK não é evidência da ordem de chamadas reais do Grand Cross, de registro efetivo dos delegates, IDs RMI, formatos de payload, handshake, autenticação ou compatibilidade com servidor local. Não foram realizadas modificações na instalação nem coleta de mensagens.

Trilha análise do cliente: referência externa validou o desenho geral da interface ProudNet. Trilha servidor funcional: ainda não demonstrado. Relatório completo local: GrandCross_Local_CHECKPOINT_2373_2378.md.