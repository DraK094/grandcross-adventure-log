# GrandCross Local — passos 1581–1584

Coleta do usuário no processo local PID 30012: RVA 0x4349F40 contém `45 33 C0` (`xor r8d,r8d`) seguido de `E9 78 01 00 00` (`jmp` relativo +0x178), cujo destino calculado é RVA 0x434A0C0. Assim, a função chamada logo após carregar 10055 é um wrapper que zera o terceiro argumento e encaminha a execução; não demonstra por si só gravação no buffer nem formato wire.

Os outros bytes dos 160 lidos após padding CC pertencem a funções vizinhas e não são continuação do wrapper. A identificação 10055 para CG_RequestLogin continua validada pelas duas sobrecargas e array C2S. Próxima leitura dirigida: 128 bytes no endereço de destino 0x434A0C0, somente leitura, para identificar o tratamento do argumento EDX.
