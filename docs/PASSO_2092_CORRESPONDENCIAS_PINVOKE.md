# PASSO 2092 — Correspondência nominal entre PInvoke e exportações ProudNet

**Executado:** metadata IL2CPP v29 e diretório de exportações PE de `ProudNetClientPlugin.dll`, 801 exportações. **12 de 12** métodos selecionados da classe `Nettention.Proud.ProudNetClientPluginPINVOKE` (TypeDef 33446) têm a flag PInvokeImpl e exportação cujo nome bate com a regra `CSharp_` + nome do método.

Métodos verificados: 257860 serverIP_set; 257861 serverPort_set; 257863 protocolVersion_get; 257876 NativeNetClient_Create; 257880 HasServerConnection; 257881 Connect__SWIG_0; 257882 FrameMove__SWIG_0; 257883 SetEventSink; 257884 AttachProxy; 257885 AttachStub; 257939 SetCallbackJoinServerComplete; 257946 SetCallbackError.

**Limites:** confirmação de presença de símbolo e PInvoke flag, NÃO comprovação de entrypoint/metadados de importação, invocação efetiva, formato de handshake, login ou sessão local. Zero funções executadas, pacotes enviados, arquivos ou memória modificados. Próximo PASSO 2093 não executado. Trilha de servidor ainda sem marco funcional.
