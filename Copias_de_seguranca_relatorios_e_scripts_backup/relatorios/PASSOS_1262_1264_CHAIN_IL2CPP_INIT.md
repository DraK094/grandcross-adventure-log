# GrandCross Local — PASSOS 1262–1264

A amostra real da exportação `il2cpp_init` (RVA 0x344B60), fornecida pelo usuário, contém dois `call rel32` e um `lea` RIP-relativo. Destinos comprovados por decodificação dos bytes: primeiro `call` para RVA `0x421794`, segundo `call` para RVA `0x347DE0`, referência de dados para `0x508CD3F`.

A tabela PE `RUNTIME_FUNCTION` reconstruída da `.vdata` conferida independentemente fornece os limites: `il2cpp_init` [0x344B60,0x344B88); primeira chamada [0x421794,0x4217E0), unwind 0x5A88A8C; segunda chamada [0x347DE0,0x348EE4), unwind 0x5D66768. As duas chamadas apontam exatamente para o início de funções registradas. Seus corpos nativos não possuem cobertura nos dados brutos da seção 0. A referência de dados RVA 0x508CD3F está em seção 2, com bytes brutos disponíveis, porém não interpretados.

O script reproduzível valida o hash do GameAssembly atual e da reconstrução .vdata. Nenhum CodeGenModule, serializer nativo, RMI ID ou papel semântico das funções foi identificado. PASSO 1265 pendente de amostra curta e autorizada em memória.