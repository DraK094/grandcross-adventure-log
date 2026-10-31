# GrandCross Local — PASSOS 1476–1479

Fonte local verificada: global-metadata(3).dat, IL2CPP metadata v29, tabela TypeDefinition em offset 26575524, 3034944 bytes, 34488 registros de 88 bytes.

1476: tokens globais lidos em runtime em PASSO 1472: 0x2000E099 e 0x2000E09B. A decodificacao de MetadataUsageType (bits altos = 1 TypeInfo, bit baixo = 1 nao resolvido, indices baixos deslocados >> 1) fornece os indices Il2CppType 28748 (0x704C) e 28749 (0x704D). Il2CppTypeIndex NAO equivale diretamente a TypeDefinitionIndex. Referencia: Il2CppInspector MetadataUsage.FromEncodedIndex.

1477: ao tentar interpretar 28748/28749 como INDICES de TypeDefinition, obtem-se System.Configuration.SpecialSettingAttribute e System.Configuration.UriSection, incompatíveis com a hipótese West. Essa e uma demonstracao de que a correspondencia direta e incorreta, nao identificacao das classes referentes aos tokens.

1478: vasculhada tabela TypeDefinition por namespace e nome: 21860=SevenDSWestS2C.Proxy; 22419=SevenDSWestC2S.Proxy; 23053=SevenDSWestS2C.Stub; 23289=SevenDSWestC2S.Stub. Esses indices sao TypeDefinitionIndex e nao os indices Il2CppType 28748/28749.

1479: para vincular os indices Il2CppType aos TypeDefinition correspondentes, e necessario recuperar sua entrada na tabela native s_Il2CppTypeTable (code registration/metadata registration) ou consultar de forma somente leitura a estrutura resolvida. O arquivo global-metadata isolado nao contem a tabela Il2CppType nativa. Nenhum ID RMI numerico foi identificado; nenhuma conexao de login local foi comprovada.
