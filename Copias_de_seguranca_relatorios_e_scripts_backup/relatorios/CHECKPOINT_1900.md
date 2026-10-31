# Checkpoint 1900

Separado o objeto proxy (this) de seu contexto em [this+8] no RmiSend. Em sete vtables de proxy o callback opcional slot +0x10 é RVA 0x168A0 (ret 0), enquanto o slot +0x18 aponta para RmiSend RVA 0x17930. A chamada principal de interface +0x40 usa a vtable do contexto, ainda sem identidade concreta. Não há prova de framing nem autenticação local funcional. Scripts gc_rmisend_context_1881.py e gc_proxy_callback_1891.py foram executados offline.
