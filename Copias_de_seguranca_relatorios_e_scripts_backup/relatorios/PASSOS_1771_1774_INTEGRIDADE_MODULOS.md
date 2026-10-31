# GrandCross Local — PASSOS 1771–1774

Usuário confirmou a copia em Windows das DLLs nativas em D:\GrandCross_Local\Analise\ProudNet_1771. ProudNetClient.dll: 2396160 bytes, SHA256 E5B197F6F8485BE65C3156D7899A46F8CA08CA62943C4B554BFFE595CED769C9; ProudNetClientPlugin.dll: 146432 bytes, SHA256 91EF8EF7624491D1598F0F5EF31B83FA62A0E2A45A8324EBDB8B7EDB43BD845C. Hash das copias coincide com as originais segundo script executado pelo usuario.

No ambiente de analise foram encontrados apenas GameAssembly(4).dll e global-metadata(3).dat e artefatos anteriores; os dois binarios nativos copiados no Windows NAO foram anexados nem montados. Portanto nenhuma analise de PE imports/exports das DLLs nativas foi realizada; nao inferir resultados que dependam dos bytes nao fornecidos.

Proxima dependencia para continuar: anexar ProudNetClient.dll e ProudNetClientPlugin.dll (as copias, nao alterar originais) ou fornecer saida de export/import obtida localmente. Nao e necessario outro comando PowerShell para preparar arquivos. O objetivo e analise offline estatica sem execucao de DLLs.
