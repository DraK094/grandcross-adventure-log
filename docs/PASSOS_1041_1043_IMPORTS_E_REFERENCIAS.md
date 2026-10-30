# PASSOS 1041–1043 — Importações mínimas e referências na .vdata

30/10/2026. Análises locais Python sobre as DLLs fornecidas. Passos 1041–1043 concluídos como verificações estáticas; próximo 1044 não executado. Objetivo 2 permanece EM ANDAMENTO.

PASSO 1041: PE da DLL atual, SHA256 01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624: 10 descritores de importação, com um thunk/função por DLL. Bibliotecas e símbolos: kernel32/GetModuleHandleA; USER32/IsWindowVisible; ADVAPI32/CryptAcquireContextW; ole32/CoUninitialize; OLEAUT32/ordinal 77; SHELL32/SHGetKnownFolderPath; WS2_32/inet_ntop; IPHLPAPI/GetIfEntry; dbghelp/SymInitialize; baselib/?Baselib_DynamicLibrary_GetFunction@il2cpp_baselib@@... . Nome mangled indica função de busca de símbolos, mas não prova que o código de inicialização a chame.

PASSO 1042: os mesmos dez pares DLL/símbolo ocorrem na DLL antiga (SHA256 fab18d112f6414090c4cf36c25908fae1056c87d56e6ac432c053b52e2933ddd), sem mudanças de nomes. As RVAs das células IAT mudaram de 0x6A81260..0x6A812F0 para 0x6AE0260..0x6AE02F0, igualmente espaçados em 0x10.

PASSO 1043: .vdata atual reconstruída em Python puro, 14.131.200 bytes; SHA256 72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231 (reproduzido). Varredura literal por (a) cada RVA de importação representado em DWORD little-endian e (b) endereço VA presumindo ImageBase 0x180000000 representado em QWORD little-endian. Apenas GetModuleHandleA IAT RVA 0x06AE0260 teve uma ocorrência DWORD no offset .vdata+0xF189. Ao redor há oito bytes `60 02 AE 06 00 00 00 00` compatíveis com um valor RVA de 64 bits, mas não foi provado que seja dado ou instrução, nem que seja usado em execução. Os outros 9 RVAs não tiveram correspondência literal nos dois formatos; referências relativas, calculadas ou transformadas não são excluídas.

Limite: importações mínimas e nome de API de resolução de função **não demonstram** resolução dinâmica efetiva, chamada de il2cpp_init, valores reais de memória, CodeRegistration ou MetadataRegistration. O PE exporta il2cpp_init, mas seu corpo ainda não está disponível como bytes brutos de sua seção. Nenhum servidor offline funcional comprovado.

Retomada PASSO 1044: classificar com cuidado a estrutura que contém o RVA 0x06AE0260 em .vdata+0xF189, verificando alinhamento, vizinhança, e possíveis leituras estáticas sem inferir execução; depois examinar outras vias de resolução de funções da DLL.

Somente documentação própria versionada, sem copiar bibliotecas proprietárias.