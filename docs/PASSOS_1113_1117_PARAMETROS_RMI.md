# GrandCross Local - PASSOS 1113-1117

Testes independentes no metadata IL2CPP 29 antigo e atual do usuario.

1113: 12 classes de login, selecao, ProudNet e handlers encontradas e intervalos de metodos validados na versao atual.
1114: 11 classes compartilhadas preservam assinaturas (nomes e parametros) nas duas versoes; ArenaTagPvp_PacketHandler aparece apenas na atual.
1115: corrigido o parser Il2CppParameterDefinition: campos `nameIndex`, `token`, `typeIndex`, cada qual 4 bytes. Interpretacao anterior de 275 indices como tipos foi descartada; sao 275 observacoes de parametros, abrangendo 58 tipos internos distintos por versao, associacoes antigas/novas consistentes nessa amostra.
1116: indices de tipo de parametros relevantes identificados na versao atual: `ConnectToWestSideServer(ip=0xB6B5,port=0xC22C)`, `GameServerConnect(worldInfo=0x13274)`, `NativeNetClient.Connect(param=0xA1A7)`.
1117: regressao do parser corrigido bem sucedida. Nao foram decodificados nomes de tipos, IDs RMI, formato de serializacao, nem fluxo de runtime.

**Servidor local compativel e taverna offline nao demonstrados. Proximo PASSO 1118 pendente.** Nenhum arquivo proprietario ou dado privado publicado.