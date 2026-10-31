# Checkpoint 1920

Confirmada a construção embutida de C2SProxy em CNetClientImpl+0x16F0, com vtable final RVA 0x117C10, e inicialização do contexto [this+8] em zero pelo construtor-base RVA 0x144D0. A rotina 0x55080 recebe esse proxy e consome seu campo de contexto em [this+8], invocando vtable slot +0x48. Escritas no offset numericamente equivalente +0x16F8 em outros métodos NÃO estabelecem atribuição a CNetClientImpl. Destino do slot +0x40 durante RmiSend segue desconhecido. Sem protocolo wire ou autenticação local validada.
