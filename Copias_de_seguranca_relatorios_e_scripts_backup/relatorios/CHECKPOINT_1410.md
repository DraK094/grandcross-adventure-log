# GrandCross Local — checkpoint 1410

A coleta do passo 1407 confirmou que a referência [objeto principal+0xC0] possui, pelo menos, duas referências internas processadas por laços em +0x10 e +0x18. Na primeira, cada elemento é encaminhado para auxiliar 0x6B8040; na segunda, o código acessa campos dword +0x10 e +0x14 do elemento. Isso é análise estática de código de processo; tipos nominais e protocolo não comprovados. Não existe login funcional no backend local demonstrado. Próxima verificação: continuar bytes do método em RVA 0x6DFB60; script restrito a leitura e limite do módulo.
