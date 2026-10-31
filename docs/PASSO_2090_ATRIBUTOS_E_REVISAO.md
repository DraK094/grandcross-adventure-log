# PASSO 2090 — Atributos dos métodos ProudNet e revisão da fase de rede

Executado em 31/10/2026. Metadata IL2CPP v29 validado. `Nettention.Proud.NetClient` (TypeDef 33408): 30 métodos. `Nettention.Proud.NativeNetClient` (TypeDef 33436): 14 métodos. **44 métodos analisados; 0 possuem MethodAttributes.PinvokeImpl (0x2000).** Todos os `ImplFlags` reportados iguais a 0x0000. Dados de arquivo, nenhuma memória, tráfego ou arquivo modificado.

## Leitura cuidadosa
A ausência de flag PInvoke nos **44 métodos dessas duas classes** não significa ausência de PInvoke em outros tipos; pode haver camada interna de wrappers gerados SWIG e entradas nativas declaradas em classe separada. Exportações CSharp_* em `ProudNetClientPlugin.dll` são reais. A existência de código de interoperabilidade é hipótese a ser testada relacionando imports estruturais de IL2CPP e registros de método.

## Checkpoint de retorno técnico (2081→2090)
- 2082: duas DLLs ProudNet carregadas; TCP 5 entradas, UDP 0 numa amostra.
- 2083: par loopback 50789/50790 estável em duas amostras e pertencente ao mesmo PID. Não comprovado ProudNet.
- 2084: export table de plugin 801 nomes e core 706.
- 2085: interface SWIG nomeada (Create, Connect, FrameMove, SetEventSink, callbacks, RMI).
- 2086: metadata v29 com os 12 termos procurados no string heap (algumas buscas limitadas a 12).
- 2087–2089: MethodDefinitions correlacionados a classes reais; `Nettention.Proud.NetClient`, `NativeNetClient`, `RmiProxy`, `RmiStub` etc.
- 2090: atributos e ausência de PInvoke flag nos dois tipos.

**Ganho real:** arquitetura estática e interfaces de conexão mapeadas. **Ainda não há** servidor experimental funcional, handshake, sessão aceita ou login local.
## Próxima decisão
Concentrar-se nos wrappers gerados SWIG de métodos `CSharp_NativeNetClient_*` e nos métodos que declaram importação nativa — restringir a inspeção a registro PE/metadata e não tentar alterar conexões com serviços oficiais. Próximo: 2091.
