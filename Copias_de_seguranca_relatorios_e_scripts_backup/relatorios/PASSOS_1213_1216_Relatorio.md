# GrandCross Local — PASSOS 1213–1216

Análise offline no GameAssembly atual, com `.vdata` reconstruída e hash SHA256 confirmado `72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231`.

1213 — Conferidas 14 seções PE e permissões declaradas. 1214 — Excluída integralmente a faixa do diretório de exceções `[0x718602c,0x7514730)` de uma sondagem de DWORDs compatíveis numericamente com RVA. 1215 — Nas janelas fora dessa tabela antes de 0x718602c, cerca de 13%–23% dos DWORDs estavam na faixa de RVA da imagem; janelas começando em 0x75e2000 e 0x76e2000 apresentaram zero correspondências na mesma heurística. 1216 — Esta é apenas análise de distribuições, não prova de ponteiros, criptografia ou CodeRegistration.

Ainda não recuperamos Il2CppCodeRegistration, CodeGenModule, endereço nativo dos serializadores, IDs RMI nem bytes de rede validados. Próximo passo 1217.