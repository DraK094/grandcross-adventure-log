# Passos 1627-1629

User read of S2C dispatch table: ID 14055 -> primary index 54 -> secondary 33 -> block RVA 0x91AD61. Native block has `E8 85 4F FD FF` at RVA 0x91AD76, whose rel32 destination is 0x8EFD00. That RVA is independently established as the method `SevenDSGameS2C.Stub.ProcessReceivedMessage_CG_RequestLoginOK`, token 0x06000777. Therefore the mapping 14055 -> CG_RequestLoginOK is independently validated. C2S ID 10055 was already validated by two native CG_RequestLogin overloads and the runtime array. Limit: no network frame or local authentication is yet implemented or verified.
