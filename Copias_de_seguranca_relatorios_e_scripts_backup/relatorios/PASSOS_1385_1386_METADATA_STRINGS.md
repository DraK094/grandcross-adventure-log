# GrandCross Local — passos 1385 a 1386

Auditoria da investigacao de colecoes: offset +0x40, +0x48, +0x50 e +0x58 sao referencias percorridas por lacos no codigo coletado. Busca literal no arquivo global-metadata.dat recebido confirmou as strings `userInfo`, `loginServiceInfo`, `CommonPacket`, `Marshaler` e `UserInfo`. Essa busca nao atribui offsets nativos a nomes; sera necessario interpretar as definicoes de campos e tipos e verificar a ligacao. Nao foi comprovado formato de pacotes ou conexao com backend local.
