# Passos 1543–1549 — IDs numericos observados

Coleta do usuario (PID 30012, GameS2C.Common, array gerenciado comprimento 628): indices 0..3 = 14001, 14002, 14003, 14004; indice 29 = 14052; 30=14053; 31=14054; 32=14055 (0x36E7); 33=14056; 627=15606. A suposicao anterior de sequencia continua 14001 + indice era ERRADA: nao existe tal sequencia global.

Inspecao offline do global-metadata(3).dat (v29, tabela de campos offset 22141564): SevenDSGameS2C.Common possui 629 campos, com 628 de mensagens e o ultimo RmiIDList. Dentro do inicio das mensagens, os campos 152591..152595 correspondem a indices relativos 29..33: CG_RequestNetmarbleAuthOK, CG_RequestAuthenticateCreateOK, CG_RequestEditorUserInfoByNickNameOK, CG_RequestLoginOK e CG_RequestLoginInstantlyOK.

A relacao por ordem sugere fortemente CG_RequestLoginOK=14055, CG_RequestNetmarbleAuthOK=14052. FATO VERIFICADO: array[32] = 14055. CORRESPONDENCIA CAMPO→VALOR: inferida pela ordem, ainda requer comprovacao independente de leitura de campo estatico ou codigo de despacho. Sem handshake local ou login funcional.
