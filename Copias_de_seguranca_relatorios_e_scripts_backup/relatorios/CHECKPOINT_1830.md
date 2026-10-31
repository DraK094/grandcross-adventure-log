# Checkpoint 1830

MSVC RTTI recuperado estaticamente nas sete vtables de RmiSend: IRmiProxy, ProudC2S::Proxy, ProudC2C::Proxy, CNetClientImpl::C2CProxy, CNetClientImpl::C2SProxy, DumpC2S::Proxy e EmergencyC2S::Proxy. Todas tem slot +0x18 apontando a RVA 0x17930. Evidencia estrutural da implementacao da ponte nativa, sem determinar objeto live, wire format ou login local funcional.
