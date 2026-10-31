# PASSO 2082 — Reconhecimento passivo de rede (31/10/2026)

**Executado, saída recebida.** Processo `7dsgc` PID 30012. Nenhum pacote enviado pelo script, nenhuma alteração de memória.

## Evidências
- `ProudNetClient.dll` carregada, base VA `0x7FFD4F240000`, ModuleMemorySize 2.433.024 bytes; arquivo no disco 2.396.160 bytes.
- `ProudNetClientPlugin.dll` carregada, base VA `0x7FFDA5350000`, ModuleMemorySize 163.840 bytes; arquivo no disco 146.432 bytes.
- Também carregadas `WS2_32.dll`, `WINHTTP.dll`, `WININET.dll` e componentes de rede do Windows.
- Cinco entradas TCP associadas ao PID: Bound local 51619/50790; CloseWait local 51619, destino porta 80; loopback Established 50790→50789 e 50789→50790.
- Zero endpoints UDP associados ao PID no instante observado.

## Interpretação e limites
As duas bibliotecas ProudNet **estão carregadas**, mas não foi demonstrado um handshake nem sessão ProudNet. O par loopback tem dois endpoints dentro do mesmo PID na coleta, mas ainda não sabemos qual subsistema o criou. `CloseWait` descreve a situação do socket, não a causa ou protocolo de aplicação. Os dados representam um instante, não uma captura histórica. Não inferir que UDP não seja utilizado em outros momentos. Nenhum servidor local funcional foi demonstrado.

## Próximo passo
PASSO 2083, ainda não executado: correlacionar sockets locais, porta par e processos por consultas read-only, sem divulgar IPs remotos, segredos ou pacotes. Relatório formal 2100 permanece pendente.
