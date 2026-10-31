# GrandCross Local — passos 1605–1609

Fonte: amostra de 192 bytes do processo fornecida no PASSO 1605, RVA 0x783F10, contendo final do metodo SevenDSGameC2S.Proxy.CG_RequestLogin (RVA inicial 0x783E00).

Observacoes na montagem x64, respeitando limites de instrucoes: 0x783F57 carrega referencia global 0x605AF48; 0x783F63 chama alocacao 0x3BEA30 com edx=1, guarda valor anterior de EBP em [rax+0x20] na condicao de array valido. A partir de 0x783F79, usa o objeto em RDI; [RDI] fornece tabela, carrega R10=[tabela+0x1A8] e outra palavra [tabela+0x1B0]. Em 0x783F9F escreve `mov dword ptr [rsp+0x78],0x2747`, isto e, ID 10055 como argumento na pilha. Em 0x783FC8 ocorre `jmp r10` (tailcall indireto), apos restaurar registradores e pilha. Isso prova propagacao do ID para uma chamada virtual/indireta da proxima camada, mas nao comprova envio de rede nem o wire format. As instrucoes iniciais da amostra no offset 0x783F10 estavam cortadas; a desmontagem deve comecar em fronteira valida (0x783F14).

Novo alvo: metodo de despacho generico SevenDSGameS2C.Stub.ProcessReceivedMessage, token 0x06000756 (RID 1878), candidato indice de tabela Firstpass 1877, RVA de entrada 0x5E18458. Verificar ponteiro e inspecionar codigo para buscar uso da resposta 14055, sem atribuir sem prova. A diferenca entre valor de ID numérico e bytes de transporte permanece essencial.
