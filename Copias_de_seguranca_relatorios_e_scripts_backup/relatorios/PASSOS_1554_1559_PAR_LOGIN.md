# GrandCross Local — passos 1554–1559

Leitura do usuario no processo local (PID 30012, base 0x7FFD00550000): `SevenDSGameC2S.Common` global RVA 0x5FB6948; classPtr 0x2650258C510; static fields ptr 0x26797DDFC10; array ptr 0x26795976000; comprimento 1176. Valores: array[0]=10000; [26]=10052; [27]=10053; [28]=10054; [29]=10055 (0x2747); [30]=10056; [1175]=13712.

Na direção S2C, coleta anterior: array de 628; [29]=14052, [30]=14053, [31]=14054, [32]=14055 (0x36E7), [33]=14056. Cruzamento da ordem de campos do metadata aponta para CG_RequestLogin no índice C2S 29, e CG_RequestLoginOK no índice S2C 32. Associação nome-valor permanece inferida pela ordem, não validada independentemente por despacho/constante; os valores do array estão observados diretamente. Candidatos bem sustentados de par request/response: 10055 e 14055. Não presumir que o padrão +4000 funcione fora destes exemplos, nem que bytes transmitidos sejam estes 32 bits crus. Não existe handshake ProudNet ou login no backend local demonstrado.

Próxima etapa: buscar confirmação independente da correspondência no código de envio/dispatch e só então criar teste isolado sintético da dupla; manter cliente oficial e servidores públicos fora dos testes.
