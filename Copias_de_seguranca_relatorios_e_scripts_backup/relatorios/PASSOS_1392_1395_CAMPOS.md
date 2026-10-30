# GrandCross Local — passos 1392–1395

A leitura do usuário no processo PID 30012, base GameAssembly 0x7FFD00550000, trouxe offsets +0x400 e +0x480 do método candidato no RVA 0x6DF460. Há referências em [rdi+0x80] e [rdi+0x88] processadas com loops de contagem e índice; mais adiante o código lê qwords [rdi+0x90] e [rdi+0x98] para chamadas auxiliares. A amostra termina no meio de uma instrução e a análise não atribui nomes de campos nem prova formato de pacote ou conexão do cliente ao servidor local.
