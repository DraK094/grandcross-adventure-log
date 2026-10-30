# GrandCross Local — passos 1372 a 1374

O usuario leu 96 bytes a partir do RVA 0x4349C30. No caminho linear ha chamadas para 0x3DE81E0 e 0x4349810, restauracao dos registradores e retorno em 0x4349C58. Ha blocos apos o retorno, alcancaveis por outros desvios, com chamadas para 0x3BF730, 0x4349530, 0x43E150 e 0x3BF520. A analise valida a estrutura de fluxo, nao identifica o formato de pacote de login nem prova comunicacao de rede. Evitar inferir que o codigo apos o retorno e sequencial.
