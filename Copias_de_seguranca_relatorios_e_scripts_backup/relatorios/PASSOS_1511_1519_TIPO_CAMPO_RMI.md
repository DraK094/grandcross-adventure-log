# GrandCross Local — passos 1511–1519

Análise offline reprodutível de `global-metadata(3).dat` (metadata IL2CPP v29). Cabeçalho indica seção `FieldDefinition` em offset 22141564, comprimento 2411004 bytes (200917 registros de 12 bytes). Interpretado cada registro como nameIndex, typeIndex, token; nomes da seção string em offset 1552996.

O índice de tipo `0xAD5C` ocorre em **2800 definições de campos** no metadata, incluindo:
- índice de campo 148706: `CW_RequestJoinChannel`, token `0x04003F56`;
- índice 148707: `CW_RequestWestSideMove`, token `0x04003F57`;
- índice 134500: `CW_CommonCancel`, token `0x040007D8`;
- índice 134501: `CW_RequestForceLogoutOK`, token `0x040007D9`;
- índice 152591: `CG_RequestNetmarbleAuthOK`, token `0x04004E83`;
- índice 152594: `CG_RequestLoginOK`, token `0x04004E86`;
- índices 197768 e 197769: `RmiID_None` e `RmiID_Last`, respectivamente.

A coincidência da tipagem com campos nomeados RmiID_None/RmiID_Last reforça a hipótese de um tipo integral de identificadores RMI. **O valor `0xAD5C` é um índice de tipo, NÃO um ID de protocolo.** Os tokens de campo `0x04......` também não representam seus valores ou IDs RMI. Ainda falta obter a identidade nativa do tipo `0xAD5C` e os valores efetivamente armazenados nos campos estáticos.

Próxima direção: localizar em metadata as classes de definição de constantes RMI e suas rotinas de inicialização. Não continuar perseguindo os trampolins genéricos do runtime. Não há login local validado.
