# GrandCross Local — Checkpoint 2300

Investigação estática, somente leitura, das exportações do ProudNetClientPlugin.dll e dos métodos de Nettention.Proud no metadata IL2CPP v29.

- NativeNetClient: 14 métodos declarados e 61 exportações com prefixo CSharp_NativeNetClient_. Nomes em comum incluem AttachProxy, AttachStub, Create, Connect e FrameMove.
- RmiProxy: 8 métodos declarados e quatro exportações CSharp_RmiProxy_, incluindo CSharp_RmiProxy_RmiSend.
- RmiStub: 8 métodos declarados e quatro exportações CSharp_RmiStub_. Destaca-se CSharp_RmiStub_SetCallbackProcessReceivedMessage, além de setters para callbacks de listas de RMI IDs.
- NativeRmiContext: 25 métodos e 40 exportações CSharp_NativeRmiContext_ com padrões de propriedades.
- NativeInternalProxy e NativeInternalStub incluem métodos RmiSend e ProcessReceivedMessage nos metadados, porém sem exportações com nomes de classe idênticos.

Marco: existe uma API do plugin explicitamente nomeada para registrar callback ProcessReceivedMessage. Isso sustenta uma ponte de interoperabilidade, mas não prova que o jogo a invoque, qual callback é usado, IDs RMI, payload, autenticação ou compatibilidade com servidor local.

Trilha de análise do cliente: avanço na identificação da interface ProudNet. Trilha servidor jogável: sem compatibilidade demonstrada. Sem porcentagem objetiva verificável. Não publicar binários proprietários, metadata completo ou dados de conta.

Arquivos derivados locais: gc_2295_2300_crosswalk.py; GrandCross_2295_2300_bridge_crosswalk.json; GrandCross_Local_CHECKPOINT_2300.md.