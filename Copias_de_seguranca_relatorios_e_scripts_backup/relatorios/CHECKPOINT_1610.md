# Checkpoint 1610

No final de CG_RequestLogin, foi constatado que 10055 (0x2747) e escrito como argumento no stack e passado a chamada indireta `jmp r10`, cujo destino vem da tabela virtual do objeto Proxy em offset +0x1A8. Essa e a ligacao comprovada para a proxima camada, mas nao e prova de que um pacote ProudNet tenha sido transmitido. Proximo passo: investigar o metodo generico de despacho S2C e procurar confirmacao independente do ID 14055. Ver PASSOS_1605_1609_TAILCALL_LOGIN.md.
