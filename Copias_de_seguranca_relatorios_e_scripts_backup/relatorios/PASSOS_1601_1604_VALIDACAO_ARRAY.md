# GrandCross Local — passos 1601–1604

Leitura do usuário de GameAssembly RVA 0x4243260, 160 bytes, analisada com objdump x64. A rotina valida RCX e R8 contra zero; inspeciona um comprimento na pilha e rejeita valor negativo; chama 0x3594C0 para ambos os arrays; rejeita deslocamentos negativos (registradores R15D e R14D); prepara origem/destino/offsets e chama 0x358CE0 em RVA 0x42432E8. O retorno é testado. Evidência consistente com rotina genérica de cópia de arrays, mas os bytes coletados não demonstram a cópia efetiva nem o pacote ProudNet.

A cadeia validada anteriormente: `SevenDSGameC2S.Proxy.CG_RequestLogin` carrega ID 10055 (0x2747), uma rotina aloca array de dois bytes e grava `47 27` little-endian no objeto; a rotina 0x3DE81E0 participa de manipulação de arrays. Nenhum pacote completo ou login no backend local foi validado. Próxima prioridade: voltar à rotina específica de envio e identificar montagem de payload e chamada terminal, sem seguir sub-rotinas genéricas de cópia.
