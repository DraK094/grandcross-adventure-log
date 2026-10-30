# GrandCross Local — PASSOS 1165–1169

Auditoria offline executada no metadata IL2CPP v29 atualizado do usuário.

**Descoberta verificada:** `CommonPacket.Marshaler` tem 3185 métodos: 1592 `Write`, 1592 `Read` e 1 construtor. Os 1592 pares adjacentes são `Write`/`Read`, e cada conjunto tem 1592 índices distintos do tipo do parâmetro. Os índices dos parâmetros entre Write e Read diferem em todos os pares; não comprovamos ainda a semântica da diferença, não são IDs RMI.

**1165:** Encontrados `Nettention.Proud.RmiProxy.GetRmiIDList()` e `RmiStub.get_GetRmiIDList`, bem como contadores associados: interfaces promissoras, nenhum valor recuperado.
**1166:** Identificadas assinaturas correspondentes de `RmiProxy.RmiSend` e `WestSideProxy.RmiSend`, sem afirmar fluxo em runtime.
**1167:** Descoberto `CommonPacket.Marshaler` com 1592 pares Write/Read. `Nettention.Proud.Message` declara `Write`/`Read`, `WriteScalar`/`ReadScalar`, `get_Data`, `get_ReadOffset`.
**1168:** Reinspecionados contratos estáticos de autenticação, sem formatos binários recuperados.
**1169:** Nenhum ID RMI numérico do jogo ou frame de rede foi reconstruído; foco seguinte é resolver os tipos dos parâmetros dos 1592 pares e localizar implementações reais. Não há servidor compatível ou login de cliente oficial demonstrados. Nenhum binário proprietário publicado.

Documentação ProudNet: https://docs.proudnet.com/proudnet.eng/proudnet/using_pn/pidl ; https://docs.proudnet.com/proudnet.eng/proudnet/using_pn/pidl/using_pidl