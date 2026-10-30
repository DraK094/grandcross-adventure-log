# GrandCross Local — PASSO 1206

Análise reproduzível dos bytes `.vdata` reconstruídos do GameAssembly atual. SHA-256 confirmado: `72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231`; os primeiros 16 bytes coincidem com amostra fornecida do processo em execução. A procura por texto ASCII como `CommonPacket`, `LoginServiceInfo`, `CodeRegistration`, `Assembly-CSharp`, `global-metadata.dat` não produziu correspondências nessa seção, o que não prova ausência das estruturas.

A tabela PE de exceções começa no RVA `0x718602c` (dentro da `.vdata` reconstruída). A leitura correta dela exigiu resolver seu RVA para a seção descompactada, e não para os bytes brutos do PE. Um registro RUNTIME_FUNCTION começa em `0x6ae2000` e termina em `0x6e33f4c`, mas isso não identifica método IL2CPP algum. **Nenhum Il2CppCodeRegistration, CodeGenModule ou endereço nativo dos quatro serializadores de login foi validado neste passo.**

Limites: comparação com memória do jogo foi feita somente para 16 bytes. A tabela de exceções não traduz MethodDefinition para endereço nativo. Próximo passo 1207: investigar estrutura e organização dos registros/código sem inferir nomes a partir de offsets.