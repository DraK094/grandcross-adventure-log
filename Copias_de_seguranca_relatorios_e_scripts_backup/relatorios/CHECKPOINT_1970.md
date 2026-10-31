# GrandCross Local — checkpoint 1970

PASSO 1969: usuário confirmou na memória do jogo a tabela de ponteiros da assembly Assembly-CSharp-firstpass em RVA 0x5E149B0, base GameAssembly 0x7FFD00550000, PID 30012.

Métodos concretos de ProcessReceivedMessage e RVA obtidos: SevenDSGameS2C.Stub token 0x06000756 RID1878 índice1877 -> RVA 0x917840; SevenDSGameS2C_Weapon.Stub token 0x06001BFE índice7165 -> RVA 0x5043F0; SevenDSGameS2C_Guild.Stub token 0x06001CA0 índice7327 -> RVA 0x4ED570. Bytes iniciais correspondentes enviados pelo usuário. Revalidados tokens com global-metadata.dat. Metadata também declara implementações Stage 0x0600290C índice10507, Pvp 0x06004BC0 índice19391, Shop 0x06004E50 índice20047, ainda sem ponteiros lidos. Flags dos seis métodos 0x00C6, sem flag abstract (0x400). Base RmiStub abstrato token 0x06000117, ponteiro nulo como esperado.

O primeiro stub geral RVA 0x917840 já tinha sido correlacionado, em análise anterior, ao despacho do ID de login S2C 14055 e handler RVA 0x8EFD00. Não confundir acesso a dispatcher e handler com login funcional. Protocolo wire/handshake e execução local pendentes.
