# GrandCross Local — PASSOS 1190–1196

Arquivos locais validados por SHA-256; `.vdata` decodificada com 14.131.200 bytes e SHA256 `72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231`.

1190: inventário de 14 seções PE por RVA.
1191: sete seções com nomes em branco; corrigida colisão em parser por nomes para identidade por RVA.
1192: busca ASCII/UTF16LE em PE bruto e .vdata pelos textos `Assembly-CSharp.dll`, `ProudDotNetClientUnity.dll`, `CommonPacket`, `LoginServiceInfo`, `RmiSend`, `CodeRegistration`, `il2cpp_codegen_register`, `global-metadata.dat`: 0 hits.
1193: sondagem QWORD alinhado a 8 com endereço virtual absoluto dentro da imagem.
1194: 3 ponteiros na seção .tls destinados à própria .tls e 0 em outras seções sob essa hipótese.
1195: nenhuma dessas buscas exclui endereços relativos, codificados, relocados, compactados ou criados em runtime.
1196: `Il2CppCodeRegistration`, `CodeGenModule`, RVAs dos 4 marshalers, IDs RMI e bytes de mensagens continuam sem validação.

**Conclusão:** barreira de mapeamento estático; não alegar que a ausência de hits prove ausência de código. Próximo passo 1197 pendente. O servidor local experimental HTTP não é compatível comprovadamente com o cliente oficial.
