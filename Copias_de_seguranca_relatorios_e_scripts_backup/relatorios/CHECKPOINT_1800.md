# Checkpoint 1800

A interface de envio ProudNet foi rastreada offline: Plugin export CSharp_RmiProxy_RmiSend RVA 0x9D00 -> auxiliar RVA 0xB7C0 -> chamada virtual `[vtable+0x18]` em RVA 0xB948. Identificador transportado nesse argumento como uint16; core ProudNetClient.dll exporta Proud::IRmiProxy::RmiSend RVA 0x17930, mas resolver o slot da vtable continua pendente. Nenhum pacote de rede completo, handshake ou login local foi verificado.
