# GrandCross Local — PASSO 1304

A leitura read-only do cliente em execução (PID 30012) revelou os nomes em texto ASCII:

- Elemento 0, ponteiro 0x0000026603DAB278: `Assembly-CSharp.dll`.
- Elemento 1, ponteiro 0x0000026604129E8E: `Assembly-CSharp-firstpass.dll`.

Ambos os nomes foram extraídos da memória a partir das estruturas recíprocas dos passos 1302–1303. A coleção tem 89 elementos; o segundo nome coincide com o assembly dos quatro métodos CommonPacket.Marshaler de login identificados no metadata.

**Validado:** associação dos dois primeiros elementos da coleção com esses nomes de assemblies.

**Não validado:** estrutura CodeGenModule, CodeRegistration, ponteiros dos quatro métodos, RMI binário, servidor local funcional. A referência QWORD1 da estrutura associada ao segundo objeto (0x000002650024C9C0 naquela sessão) é candidata a inspeção adicional, sem assumir que seja Il2CppImage.

Próximo passo: 1305, verificar estrutura e referências com somente leitura. Próximo checkpoint de dez passos: 1310.
