# GrandCross Local — checkpoint 2288: caminho alternativo pelos binários ProudNet

## Descoberta confirmada por inspeção estática PE

Além do `GameAssembly.dll`, foram inspecionadas as cópias locais `ProudNetClient.dll` e `ProudNetClientPlugin.dll`, sem modificar os arquivos.

- `ProudNetClient.dll`: **706 exportações nomeadas**, das quais **682** possuem RVA associado a bytes raw; distribuição por seção: **550** em `.text`, **150** em `.data` e **6** em `.rdata`. As 24 restantes não possuem bytes raw no endereço exportado. A classificação por seção não significa que os itens de `.data` sejam funções executáveis.
- `ProudNetClientPlugin.dll`: **801 exportações nomeadas**, todas com bytes raw e todas localizadas na seção `.text`.
- A biblioteca nativa possui símbolos C++ nomeados relacionados a `Proud::CNetConnectionParam` e outros componentes ProudNet.
- O plugin oferece exportações com padrão `CSharp_*`, incluindo estruturas de endereços, e uma ponte nativa que poderá ser estudada **sem depender** da região virtual sem bytes do `GameAssembly.dll`.

## Significado e limites

**Novo caminho de investigação independente:** existem implementações ProudNet diretamente presentes em seções `.text` convencionais nas cópias fornecidas. Isso melhora a possibilidade de examinar **a interface genérica do SDK ProudNet**.

**Não é prova** de que possamos recuperar IDs RMI específicos do Grand Cross, registro dos delegates do cliente, serialização customizada do jogo, autenticação, compatibilidade de protocolo nem funcionamento de servidor local. Não se identificou nesta etapa o fluxo de chamada real entre o cliente IL2CPP e o plugin.

Reproduzível com `gc_2284_2288_proud_exports.py`; evidência JSON `GrandCross_2284_2288_proud_exports.json`. Não incluir binários proprietários, códigos de autenticação ou credenciais.

**Trilha cliente:** rota alternativa de análise descoberta. **Trilha servidor jogável:** permanece não demonstrada.
