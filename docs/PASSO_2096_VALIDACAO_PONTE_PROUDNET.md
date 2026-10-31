# PASSO 2096 — Validação estrutural da ponte ProudNet

Metadata IL2CPP v29, 34.488 TypeDefinitions e 263.448 MethodDefinitions.

**Duas classes confirmadas:** `Nettention.Proud.ProudNetClientPlugin` TypeDef 33439 no offset 0x01C2694C, nome no índice 0x00559320; `Nettention.Proud.ProudNetClientPluginPINVOKE` TypeDef 33446 no offset 0x01C26BB4, índice de nome 0x005598E6.

**Nove métodos confirmados como PInvoke na classe 33446**: `NativeNetClient_Create` 257876; `NativeNetClient_HasServerConnection` 257880; `NativeNetClient_Connect__SWIG_0` 257881; `NativeNetClient_FrameMove__SWIG_0` 257882; `NativeNetClient_SetEventSink` 257883; `NativeNetClient_AttachProxy` 257884; `NativeNetClient_AttachStub` 257885; `NetClientEvent_SetCallbackJoinServerComplete` 257939; `NetClientEvent_SetCallbackError` 257946. Todas as flags PInvoke True.

**Validação:** 2/2 classes, 9/9 métodos. **Ainda não comprovado:** entrada real de importação, chamada efetiva, handshake ou servidor local funcional. Zero memória/arquivos/pacotes alterados.

**Decisão seguinte:** iniciar prova de conceito de comunicação TCP totalmente local e independente do cliente oficial, para inaugurar evidência de funcionalidade de rede sem atribuí-la erroneamente a Grand Cross.
