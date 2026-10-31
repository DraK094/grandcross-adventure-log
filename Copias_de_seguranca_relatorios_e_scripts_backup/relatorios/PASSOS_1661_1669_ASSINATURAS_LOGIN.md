# GrandCross Local — passos 1661-1669

Leitura offline de `global-metadata(3).dat`, método definitions e parameter definitions.

`SevenDSGameC2S.Proxy.CG_RequestLogin` existem duas overloads, MethodDefinition indices 179347 e 179348, tokens 0x06003F0E e 0x06003F0F. Cada uma recebe 11 parâmetros: remote/remotes, rmiContext, usn, sdkInfo, versionInfo, rejoinData, clientTimeTick, patchName, patchData, languageType, buildCountry. A primeira usa `remote` singular, segunda `remotes` plural. S2C Stub.ProcessReceivedMessage_CG_RequestLoginOK método global índice 165116, token 0x06000777, recebe quatro parâmetros __msg, pa, hostTag, remote. Um outro método ProcessReceivedMessage no índice 165083 recebe pa e hostTag.

Atenção: token IL2CPP é local à assembly, NÃO é índice global do array MethodDefinitions do metadata. As assinaturas NÃO são a estrutura do payload wire; alguns argumentos são contextos do runtime. IDs 10055 e 14055 estão confirmados por código do processo, não pela tabela de parâmetros. Próxima tarefa: decifrar tipo/estrutura de mensagens e contexto sem inventar wire format.
