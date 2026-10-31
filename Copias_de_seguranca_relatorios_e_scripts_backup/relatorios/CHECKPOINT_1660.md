# Checkpoint 1660

IDs confirmados por código nativo: C2S CG_RequestLogin=10055; S2C CG_RequestLoginOK=14055. A resposta cria objetos com ID em +0x10, entrega a callbacks condicionais via estruturas [rdi+0x40] e [rdi+0x38], e retorna normalmente após último callback. Os bytes após `ret` são de tratamento de erro/função seguinte. Significados dos campos, payload de rede e autenticação local não foram verificados.
