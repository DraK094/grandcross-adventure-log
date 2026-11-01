# GrandCross Local — checkpoint 2283: auditoria das exportações com bytes raw

Análise estática, somente leitura, da cópia `GameAssembly.dll` (SHA-256 `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`). Foram revisadas as 28 exportações com bytes raw mapeáveis, distribuídas por seis RVAs distintos: `0x3310`, `0x40F0`, `0x12720`, `0x55AE0`, `0x55AF0`, `0x5EFB0`.

Em janelas de aproximadamente 4 KiB ao redor dos seis endereços, a entropia de Shannon observada foi, respectivamente, `7.9337`, `7.9362`, `7.9190`, `7.9404`, `7.9403` e `7.9412` bits/byte. Os primeiros 256 KiB das duas primeiras seções sem nome apresentaram entropias `7.9839` e `7.9861`, enquanto `.edata` apresentou `5.3833` na amostra. `.boot` apresentou `7.9545`.

**Conclusão limitada:** a alta entropia é compatível com bytes transformados, compactados, cifrados, ofuscados ou outros dados de alta variabilidade, mas **não identifica nenhum desses mecanismos**. A simples existência de bytes no arquivo em seis RVAs **não comprova** que contenham instruções de máquina válidas. Tampouco as flags de execução ou os resultados anteriores de `VirtualQueryEx` demonstram os conteúdos executados. Não foi encontrada nesta rodada uma prova de registro de delegates ou compatibilidade do servidor local.

Reprodução local: `gc_2278_2283_static_audit.py` e `GrandCross_2278_2283_static_evidence.json`, ambos derivados sem publicar bytes proprietários completos. **Trilha cliente:** limite de interpretação refinado. **Trilha servidor funcional:** inalterada.
