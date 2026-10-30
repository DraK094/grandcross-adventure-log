# GrandCross Local — PASSOS 1365–1367

Leituras fornecidas: RVA 0x4349B50 e 0x41FA710, 96 bytes cada. A primeira verifica RDX e lê dword no offset +0x10, desviando caso nulo ou negativo. A segunda passa o valor 8 a uma auxiliar, verifica um ponteiro retornado e uma contagem em +0x18, e grava uma referência em +0x20. São padrões de manipulação de estruturas; não comprovam serialização de rede. A identidade funcional das auxiliares permanece pendente, assim como a comunicação cliente-servidor local.
