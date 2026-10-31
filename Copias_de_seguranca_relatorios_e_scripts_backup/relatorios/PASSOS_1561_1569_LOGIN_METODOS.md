# Passos 1561 a 1569

Analise offline do metadata v29 identificou em SevenDSGameC2S.Proxy os metodos CG_RequestLogin (tokens 0x06003F0E e 0x06003F0F); entradas candidatas da tabela Firstpass RVAs 0x5E34218 e 0x5E34220. Em SevenDSGameS2C.Stub: ProcessReceivedMessage_CG_RequestLoginOK token 0x06000777, entrada RVA 0x5E18560. Arrays runtime anteriores: C2S indice 29 = 10055; S2C indice 32 = 14055. O mapeamento campo-ID segue inferido pela ordem do metadata; ainda nao ha prova independente de dispatch, estrutura wire ou login local.
