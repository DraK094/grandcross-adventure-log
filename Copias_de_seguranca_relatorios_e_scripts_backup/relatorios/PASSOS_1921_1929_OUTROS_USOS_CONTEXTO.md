# Passos 1921–1929

Em ProudNetClient.dll, funcao RVA 0x52F30 recebe ponteiro do C2SProxy via caller RVA 0x25560, le contexto [r14+8] em RVA 0x52FCF e chama virtual slot +0x48 em RVA 0x52FD6. Funcao 0x55080 recebe C2SProxy do caller RVA 0x3AC9D, le [rbx+8] em 0x55119 e tambem chama slot +0x48 em RVA 0x55120. Confirma dois consumidores do campo de contexto, independentemente de RmiSend. O tipo concreto e a atribuicao do ponteiro continuam nao identificados. Escritas no offset +0x16F8 de outras estruturas nao foram tomadas como setters sem evidência. Sem formato wire, handshake ou login local.
