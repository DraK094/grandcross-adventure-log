# GrandCross Local — 1551 a 1553: direcionamento C2S login

Leitura offline do global-metadata(3).dat: SevenDSGameC2S.Common inicia campos no indice 151111; campo `CG_RequestLogin` esta na posicao zero-based 29 (fieldIndex 151140, token 0x040048D8), `CG_RequestNetmarbleAuth` posicao 26. Sao 1176 campos de mensagem e RmiIDList no indice 1176. Em SevenDSGameS2C.Common, campo `CG_RequestLoginOK` posicao 32, confirmado array[32]=14055; correspondência nome-valor ainda dependente de validação independente.

Recalculo de RIP-relative do bytecode `.cctor` GameC2S (RVA 0x7E2830) identifica global da classe C2S em RVA 0x5FB6948. A proxima coleta minima, somente leitura, deve buscar array C2S, confirmar comprimento 1176, ler indices 26,27,28,29,30 e 1175, e fazer comparacao com a resposta S2C 14055. Valores de C2S ainda desconhecidos; nao inventar o numero de CG_RequestLogin. Nenhuma troca cliente-servidor local testada.
