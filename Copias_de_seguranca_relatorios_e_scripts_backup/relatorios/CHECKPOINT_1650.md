# Checkpoint 1650

Os dois IDs de login estao confirmados: CG_RequestLogin 10055, CG_RequestLoginOK 14055. O handler de resposta constroi objeto com ID em +0x10, escreve referencias em +0x18 e +0x28 e valor inteiro em +0x20. Entrega objeto por callback indireto em 0x8EFF64. Em 0x8EFFBC chama outro callback e examina AL. Ainda nao ha significado confirmado de todos os campos, enquadramento ProudNet ou autenticação local.
