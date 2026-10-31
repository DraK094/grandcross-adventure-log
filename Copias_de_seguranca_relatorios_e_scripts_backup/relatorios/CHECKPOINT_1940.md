# Checkpoint 1940 — ponteiro e tamanho do buffer de mensagem recebida

Confirmados exports nativos do Plugin: NativeReceivedMessage_GetMsgBuffer RVA 0x9880, GetMsgBufferLength RVA 0x98D0, GetMsgReadOffset RVA 0x9910. Primeiro retorna ponteiro, segundo comprimento, terceiro deslocamento derivado de valor em bits (`sar 3`), sendo necessario validar argumento real. Campo messageID +0x6C e flag hasMessageID +0x70 identificados. O conteudo destes buffers nao foi capturado; nem formato wire nem login local foram comprovados.
