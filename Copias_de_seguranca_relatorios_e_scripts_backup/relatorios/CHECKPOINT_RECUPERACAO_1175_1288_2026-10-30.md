# GrandCross Local — checkpoint de recuperação até o PASSO 1288
Data: 2026-10-30. Fonte: transcrições fornecidas pelo usuário, relatórios históricos do repositório e evidências locais recuperadas. Este relatório é uma **reconciliação**, não um novo teste do cliente.

## Estado
- **Último passo documentado: 1288** (auditoria documental 15/15 dos JSON 1281–1284 e 1285–1287).
- **Passo 1289 preparado e NÃO executado**: auditoria read-only de GameAssembly.dll e global-metadata.dat na instalação documentada.
- **Ainda não funcional**: nenhum handshake ProudNet compatível, login real validado, mensagem RMI binária recuperada ou acesso à taverna via servidor local. Backend HTTP/SQLite do laboratório é separado do cliente.
- CodeGenModule para Assembly-CSharp-firstpass.dll, CodeRegistration e quatro endereços nativos dos serializadores: **não localizados**.
- Não publicar GameAssembly.dll, global-metadata.dat, dados pessoais, tokens de autenticação ou dumps sensíveis.

## Registro histórico recuperado
| Passos | Evidência / conclusão |
|---|---|
| 1175–1186 | LoginServiceInfo, WestSideUserInfo e 4 serializadores CommonPacket.Marshaler identificados por metadata: tokens 0x600328C, 0x600328D, 0x6003292 e 0x6003293; MethodDefinitions globais 176145, 176146, 176151, 176152. Não são IDs RMI. |
| 1187–1200 | Reconstrução .vdata de 14.131.200 bytes; 310.763 registros RUNTIME_FUNCTION; análise de PE, entry point .boot, TLS e buscas negativas inconclusivas por CodeRegistration. O hash histórico 72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231 requer conciliação com um hash diferente mencionado em documento antigo. |
| 1201–1203 | Módulos carregados e base de GameAssembly confirmados durante PID 30012; SHA-256 do arquivo no disco idêntico à versão analisada: 01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624; intervalos .vdata/.boot dentro do módulo. Endereços absolutos só valem para aquela sessão. |
| 1204–1206 | .vdata MEM_COMMIT/PAGE_EXECUTE_READWRITE, .boot MEM_COMMIT/PAGE_EXECUTE_READ; primeiros 16 bytes da .vdata em memória iguais aos da reconstrução; diretório de exceção identificado dentro da .vdata. 16 bytes iguais não provam conteúdo completo idêntico. |
| 1213–1216 | Regiões da .vdata com densidades distintas de valores compatíveis com RVA; não prova ponteiros nem criptografia. |
| 1217–1223 | Assembly-CSharp-firstpass.dll contém 20.548 métodos com RID contínuo; posições RID-1 12939,12940,12945,12946 como candidatos, **não** índices de methodPointers validados; PE tem 3 relocações DIR64 na região TLS. |
| 1228–1238 | Quatro seções executáveis, 310.763 começos de função registrados, 207.223 além da cobertura de bytes brutos no arquivo. Não identifica quais funções são os serializadores. |
| 1239–1242 | RVA 0x20B2740 calculado, código x64 lido em memória e cruzado com UNWIND_INFO (PUSH_NONVOL RBX, ALLOC_SMALL 32); confirma ligação estrutural, não identidade IL2CPP. |
| 1243–1248 | Auditado metadata com métodos abstratos/genéricos; RIDs contíguos, porém sem prova de mapeamento RID→ponteiro. |
| 1249–1261 | 384 exportações PE, il2cpp_init RVA 0x344B60, auditoria de imports, TLS sem callbacks recuperáveis. |
| 1262–1272 | Bytecode inicial de il2cpp_init lido; chamadas para 0x421794 e 0x347DE0, depois 0x42DB50; rotina compartilhada 0x42D378. Referência de dados para texto 'Cannot marshal field socket' não é evidência de CodeGenModule. |
| 1273–1276 | Função 0x42D378 usa base PE RVA 0x0 e tabela em 0x6326F10; nomes AreFileApisANSI e CompareStringEx sugerem outro subsistema. Hipótese de resolvedor de APIs não comprovada. |
| 1277–1284 | 384 nomes exportados, 286 RVAs distintos, 36 grupos de aliases, 56 RVAs no início de RUNTIME_FUNCTION e apenas 6 com bytes brutos; aliases exigem cautela. Nenhum endereço de serializador identificado. |
| 1285–1288 | Auditoria 1288 compara os registros 1281–1284 e 1285–1287: 15/15 verificações documentais aprovadas; tentativa anterior de localizar arquivos em D:\GrandCross_Local não demonstra ausência, pois o caminho histórico era E:\JOGOS\Netmarble Game\7dsgb. |

## Lacunas e material ainda não integralmente recuperado
- Alguns intervalos (1207–1212, 1224–1227 e evidências integrais de 1285–1287) não foram fornecidos integralmente nas transcrições deste chat; não presumir seus resultados além de relatórios verificáveis.
- Vários nomes de arquivos em transcrições eram links de outro chat; não tratá-los como binários disponíveis nem como backups GitHub concluídos.
- Nem todo relatório histórico foi publicado no GitHub: existem commits específicos confirmados e tentativas bloqueadas. Não afirmar que todas as evidências estão arquivadas.
- Um checkpoint documental não substitui testes reproduzíveis.

## Próxima ação
Executar o PASSO 1289 (se necessário, com ajuda do usuário no Windows) para confirmar caminho, tamanhos e SHA-256 dos dois binários; somente depois avançar com inspeção IL2CPP. Toda mudança de etapa deve alimentar o registro e o backup a cada múltiplo de 10, com commit SHA confirmado.
