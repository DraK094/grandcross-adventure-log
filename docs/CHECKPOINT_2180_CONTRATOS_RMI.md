# Checkpoint tecnico - GrandCross Local - passos 2175-2180

## Escopo e procedencia
Analise estatica da copia **global-metadata.dat** enviada pelo usuario, sem executar o cliente ou fazer conexoes de rede. Complementa `docs/CHECKPOINT_2174_ANALISE_CLIENTE_E_PROUDNET.md`.

Parser local: tabela IL2CPP v29, stride 88 bytes para tipos, stride 32 para metodos, indice de nomes no heap de strings, indice do tipo declarante e campo `parameterCount`. Resultado conferido para 15 tipos e todos os metodos desses tipos: os indices de proprietario dos metodos coincidem com os respectivos tipos. Contagens e assinaturas sao **informacoes de metadata**, nao de chamadas observadas em execucao.

## 2175 - verificacao estrutural
- Metadata v29: 34.488 registros de tipos e 263.448 registros de metodos, segundo os offsets/strides do parser.
- Amostra de 15 tipos: todos os indices de tipo declarante lidos nos respectivos metodos conferem com o tipo que os contem.
- Essa verificacao cruzada fortalece a confiabilidade do parser, sem demonstrar semantica do codigo compilado.

## 2176 - contratos nominais dos gerenciadores
| Tipo | Metodos identificados | `EnqueueSendMessage` | `OnPacketReceived` |
| --- | ---: | --- | --- |
| `PacketManager` | 25 | 5 parametros | 1 parametro |
| `GuildPacketManager` | 15 | 5 parametros | 1 parametro |
| `WestSidePacketManager` | 14 | 5 parametros | 1 parametro |
| `RelayPacketManager` | 15 | 5 parametros | 1 parametro |

`PacketManager.ConnectToGameServer` e `GuildPacketManager.ConnectToGuildServer` registram 2 parametros cada. A igualdade de aridade nao comprova equivalencia de tipos, serializacao ou fluxo.

## 2177 - contratos nominais dos proxies
Cada um de `GameProxy`, `GuildProxy`, `WestSideProxy` e `RelayProxy` possui **4 metodos**, incluindo duas sobrecargas `RmiSend` com, respectivamente, **5 e 1 parametros**. O tipo generico `Nettention.Proud.RmiProxy` inclui uma sobrecarga `RmiSend` de **5 parametros**.

**Interpretacao:** uma interface recorrente e uma hipotese de adaptacao/camada compartilhada. **Ainda nao comprovado:** tipos dos parametros, heranca, relacao de chamadas, IDs RMI ou formato do payload.

## 2178 - superficie nativa gerenciada
`Nettention.Proud.NetClient` apresenta `Connect` (1 parametro), `AttachProxy` (1), `AttachStub` (1). Isso sustenta a existencia de superficies para conexao e anexo de proxies/stubs, mas nao revela qual proxy do jogo e anexado ou em que momento.

## 2179 - autenticacao
`Auth_PacketHandler.CG_RequestLoginOK` registra **4 parametros** nos metadados. O nome e a aridade sao validos; nenhum valor de credencial, endpoint, chamada executada ou formato de autenticacao foi recuperado. Nao presumir que o handler opera sobre ProudNet em vez de outro transporte.

## 2180 - diagnostico e proxima prova
**Nova constatacao:** ha coincidencias sistematicas de aridades em quatro gerenciadores e quatro proxies, corroboradas por validacao de `declaringType` na tabela de metodos. Isso e mais especifico do que busca textual, mas **nao comprova vinculo de chamadas**.

Prova seguinte mais valiosa: recuperar os indices de tipos dos parametros/retorno de `RmiSend`, `EnqueueSendMessage` e `CG_RequestLoginOK` e validar o mapeamento IL2CPP type-index -> tipo efetivo. Se possivel, mapear callsites com evidencias do codigo compilado; caso nao seja viavel, registrar explicitamente a lacuna.

### Status das duas trilhas
- **Analise do cliente:** mapa de interfaces e contagem de parametros validado.
- **Servidor local funcional:** inalterado; servidor HTTP Python experimental nao demonstrou compatibilidade com handshake/RMI/login real do Grand Cross.

### Cuidados
Nao publicar binarios comerciais, metadata bruta, conteudo de sessao, credenciais nem endpoints privados. Nao confundir uma coincidencia de aridades com especificacao do protocolo.
