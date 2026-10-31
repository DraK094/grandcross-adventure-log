# Checkpoint 1910

Construtor de CNetClientImpl contém C2SProxy em +0x16F0; em 0x41FF8 atribui vtable RVA 0x117C10, apos construtor-base 0x144D0 zerar o contexto [this+8]. Portanto contexto do proxy reside em CNetClientImpl+0x16F8, e depende de atribuição posterior. Rotina 0x55080 que recebe C2SProxy chama slot +0x48 do objeto desse contexto. Ainda sem identidade de contexto, framing de transporte ou login local.
