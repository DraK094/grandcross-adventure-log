# Checkpoint 1810

Sete estruturas candidatas de vtable em ProudNetClient.dll possuem, na posicao +0x18, o endereço de `Proud::IRmiProxy::RmiSend` (RVA 0x17930). ProudNetClientPlugin.dll chama virtualmente por +0x18 (RVA 0xB948). A equivalencia de slot foi confirmada estaticamente, nao a identidade do objeto concreto em runtime. Nenhum framing wire ou autenticacao local confirmado.
