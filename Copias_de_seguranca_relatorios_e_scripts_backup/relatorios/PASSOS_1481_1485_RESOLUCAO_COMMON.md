# GrandCross Local — PASSOS 1481–1485

Fonte: global-metadata(3).dat, IL2CPP metadata v29, TypeDefinition table em offset 26575524, 34488 registros de 88 bytes. A tabela de strings inicia em offset 1552996. O campo byvalTypeIndex da definicao (offset +8) permite associar TypeInfoIndex aos tipos.

TypeInfoIndex 28748 (0x704C) corresponde unicamente a TypeDefinitionIndex 22852, nome `Common`, namespace `SevenDSWestC2S`.
TypeInfoIndex 28749 (0x704D) corresponde unicamente a TypeDefinitionIndex 20203, nome `Common`, namespace `SevenDSWestS2C`.

Verificado pela leitura das entradas: 22852 primeiros inteiros [0x1B87EF,0x3D67BD,0x704C,0xFFFFFFFF]; 20203 [0x1B87EF,0x38A8E0,0x704D,0xFFFFFFFF]. Os tokens observados no processo 0x2000E099 e 0x2000E09B referem-se precisamente a essas classes `Common` por meio do encoded TypeInfo index. NAO sao IDs RMI.

A tabela de campos metadata em offset 22141564, registros de 12 bytes, identificou em `SevenDSWestC2S.Common` dois nomes `CW_RequestJoinChannel` (token 0x04003F56) e `CW_RequestWestSideMove` (0x04003F57). Em `SevenDSWestS2C.Common`, `CW_CommonCancel` (0x040007D8) e `CW_RequestForceLogoutOK` (0x040007D9). Esses tokens sao identificadores de campos de metadata e NAO IDs RMI numericos; nomes por si so nao definem a tabela retornada por GetRmiIDList.

A correspondencia de classes TypeInfo agora esta verificada offline; nenhum objeto runtime estatico foi lido e nenhum ID de protocolo foi validado. Próxima pergunta: localizar de forma somente leitura o valor runtime inicializado de `Common` e a estrutura efetivamente retornada por `GetRmiIDList`, sem executar inicializadores nem alterar memória.
