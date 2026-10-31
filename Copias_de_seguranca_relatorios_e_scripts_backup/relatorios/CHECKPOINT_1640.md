# Checkpoint 1640

ID C2S CG_RequestLogin 10055 confirmado no método nativo. ID S2C CG_RequestLoginOK 14055 confirmado no dispatcher e no handler nativo (`mov edx,0x36E7` e `mov [rbx+0x10],0x36E7`). O handler usa chamada indireta por slot +0x1A8, ainda sem identificacao do destino ou formato wire. Nao ha autenticação local funcional.
