# Passos 1711-1719

A partir dos campos de LoginServiceInfo no metadata v29, os indices de tipo de `maintenanceInfo` e `emergencyNoticeInfo` podem ser relacionados a TypeDefinitions pelo campo byvalTypeIndex no offset +8. O indice original de `userInfo` = 0x9CD8 corresponde a LoginUserResultInfo, e o de `loginServiceInfo` = 0x9CD4 corresponde a LoginServiceInfo. A relacao e estrutural e nao demonstra formato wire.
