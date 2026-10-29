# BACKUP DE RETOMADA — GRAND CROSS LOCAL — CHECKPOINT 900
Data: 29/10/2026. Último PASSO **executado e aprovado: 900**. PASSO 901 foi preparado/enviado, **NÃO EXECUTADO**. NÃO avançar sem resolver o checkpoint e confirmar a saída do próximo passo.

## Segurança / limites do backup
Este é um backup **documental de conhecimento e recuperação do ambiente**, não uma cópia dos binários locais, arquivos de jogo, venv, scripts integrais dos 900 passos ou logs completos. Não versionar assets, binários proprietários, chaves, credenciais e dados pessoais.

## Projeto e rotina
- GitHub: https://github.com/DraK094/grandcross-adventure-log ; branch main.
- Objetivo: pesquisa independente do cliente PC de Seven Deadly Sins: Grand Cross visando avaliar viabilidade de ambiente local experimental. **Nenhum servidor offline jogável, login de cliente real com servidor local ou CodeRegistration foi comprovado.**
- Um passo por vez, scripts completos PowerShell 5.1 somente leitura, saídas auditadas antes de avançar, backup/painel/tabela comparativa a cada 100 passos. Conquistas apenas em descobertas significativas. Diferenciar análise estática, emulação, protótipos e servidor jogável.
- Preservar contexto anterior: [CHECKPOINT_800.md](CHECKPOINT_800.md), [BACKUP_TECNICO_PASSO_720.md](BACKUP_TECNICO_PASSO_720.md).

## Ambiente e caminhos
- Windows PowerShell 5.1; Python 3.11 em `E:\GrandCross_Local\Ferramentas\Emulacao_854\.venv\Scripts\python.exe`, Unicorn 2.1.4, Capstone 5.0.7.
- Binário original: `E:\JOGOS\Netmarble Game\7dsgb\GameAssembly.dll`, tamanho 47.199.760 bytes, **somente leitura**. Metadata: `E:\JOGOS\Netmarble Game\7dsgb\7dsgc_Data\il2cpp_data\Metadata\global-metadata.dat` ~31.786.920 bytes.
- Unity 2022.3.27f1; PE x64, IL2CPP metadata v29.1; ImageBase 0x180000000; 14 seções; .vdata RVA 0x06A83000, tamanho virtual 14.131.200, RawSize 0; .boot RVA 0x077FD000, raw offset 0x02553800, raw size 8.060.416.
- Entrada .boot RVA 0x077FD058; helper RVA 0x077FD1DF; decoder RVA 0x077FD05D; saída em VA 0x186A83000; fonte comprimida .boot+0x22C; salto após conclusão para .vdata+0x1CC32. **Conclusão integral e salto efetivo não observados**.
- Emulação Unicorn mapeia .vdata RWX, .boot RX (temporariamente RW para escrever cópia inicial), stack base 0x200000000. Código original apenas em memória emulada. Python executado via PowerShell here-string piped com `-B -`, sem arquivos.

## Evidências de reconstrução
| Extensão | SHA-256 |
| --- | --- |
| 128 KiB / 131072 | `ad5181b326ea0e993bbb669ac0fa154d88d63706dc9c093ca56e2b1107c7f34e` |
| 256 KiB / 262144 | `805b7aa5b0262d82aedef06afb42c658fe182133d18fcaf3d1efff2e9aa68357` |
| 371200 bytes | `4d716c81b7a47a3bcec58605f91e533cc32a938b2b9745f884cd127f617a773d` |
| 512 KiB / 524288 | `8dbae2603dd37c17c6717167401d1c9d673a4178e59cabdd767612cf26f5eb19` |

Os três checkpoints 128/256/512 KiB foram reproduzidos no passo 900. Isso cobre **3,710% do espaço virtual .vdata**, não o projeto todo. PASSO 886: execução original 5.798.697 instruções, 524.288 escritas e zero leituras não inicializadas; 285.093 bytes de entrada .boot consumidos; epílogo não alcançado. Saída inicial 16 bytes: `C6 67 00 00 94 00 99 19 FF 49 C1 27 44 01 94 B1`.

## Descobertas estáticas do código recuperado
Offsets relativos ao início de .vdata; VA = 0x186A83000 + offset:
```asm
0x1CC32 push rbp
0x1CC33 jmp 0x29F32
0x29F32 call 0x1C2E97   ; fora da regiao recuperada
0x29F37 jmp 0x1CC38   ; endereço teórico de retorno
0x1CC38 pop rbp
0x1CC39 jmp 0x4502C
0x4502C sub rbp, 0x29F37
0x45033 jmp 0x29F3C
0x29F3C call 0x1A3A19  ; fora da regiao recuperada
0x29F41 jmp 0x46026
0x46026 pop rax
0x46027 jmp 0x5A86B
0x5A86B sub rax, 0x6AACF41
0x5A871 jmp 0x30E789  ; ainda fora da regiao recuperada
```
PASSO 885: o endereço de retorno hipotético da segunda CALL é ImageBase + .vdataRVA + 0x29F41 = 0x186AACF41; subtraindo 0x6AACF41 resulta exatamente em **0x180000000**, confirmando relação matemática com o ImageBase, **não** a execução real da cadeia. Primeira constante `0x29F37` também coincide com retorno hipotético da CALL anterior. Os CALLs em 0x1C2E97 e 0x1A3A19 exigem recuperação de saída maior.

## Descompressor original
- Rotina .boot de offset 0x5D a 0x1DF; 157 instruções decodificadas estaticamente; 30 desvios diretos, cinco retornos ao laço 0x7E.
- Quatro `REP MOVSB` em offsets .boot 0x144 (origem RDI-RBP), 0x18E, 0x1A5 e 0x1C5 (origem RDI-RAX). Operação literal `MOVSB` sobreposta requer cópia sequencial, não snapshot simples.
- PASSOS 888–891: 128 KiB, 17.922 invocações reais `REP`; 126.116 hooks do Unicorn devido a iterações; 108.195 bytes escritos por REP, 22.877 por outras instruções. **27/27 cópias sobrepostas** validadas por simulação byte a byte, zero divergências. Por rota 6/0/20/1.
- PASSO 892: protótipo Python em blocos 910/910 comparações, zero divergências, 20,70x mais rápido somente em microbenchmark isolado.
- PASSOS 893–894: integração do protótipo dentro da emulação mantém hashes de 128/256/512 KiB; para 512 KiB 68.300 invocações aceleradas, 97 cópias sobrepostas, 419.604 bytes acelerados e 104.684 nativos; zero escritas REP nativas inesperadas.
- PASSOS 895–896: integração Python piorou desempenho global; no teste cruzado original 4,039654s vs acelerado 5,091557s, **acelerado 26,039% mais lento**; não usar como padrão.
- PASSO 897: remover hook de escrita reduziu o tempo aproximadamente 6,14% (auditado 15,087070s vs leve 14,160045s) com hashes iguais, mas contexto de monitoramento diferente.
- PASSO 898: consultar RDI a cada 1024 instruções, **modo amostrado**, médio 3,545868s vs modo leve 15,182223s = 4,2817x no teste; 34 bytes além do destino, RDI 0x186B03022, RIP 0x1877FD1B7; prefixos SHA iguais, parada/estado não iguais.
- PASSOS 899–900: **monitoramento híbrido** verifica RDI a cada 1024 instruções até próximo do objetivo e depois a cada instrução na janela final 4096 bytes; 512 KiB recuperados com **excedente 0** e estado idêntico ao da referência: RIP 0x1877FD1A5, RSI 0x186AFA61B, RDI 0x186B03000. PASSO 899 média híbrido 3,609810s vs amostrado 3,584940s. PASSO 900: 3,576512s, 5.798.698 hooks de código, 51.484 consultas RDI, 3 hashes corretos. **Modo híbrido não audita cobertura individual ou leituras não inicializadas**: essas evidências vêm das execuções auditadas anteriores.

## Marcos de progresso qualitativo
- Geral histórico: 600 = 25%; 700 = 28%; 800 = ~31%. São **estimativas qualitativas de investigação**, não implementação do servidor nem percentuais objetivamente mensuráveis.
- 900: progresso qualitativo **a ser avaliado**; não transformar 3,710% da .vdata em percentual de servidor ou engenharia reversa. Tabela por área no README / CHECKPOINT_900 e site, distinguindo medidas e julgamentos.
- Servidor offline funcional: **não**. Protótipos locais de endpoints não equivalem a autenticação real ou gameplay.

## Pendências prioritárias
1. Recuperar saída integral do descompressor (não sabemos o tamanho final real ou se saída equivale inteiramente à .vdata).
2. Validar dinamicamente salto para .vdata e cadeia de inicialização, inclusive dois CALLs ainda inalcançáveis.
3. Localizar CodeRegistration e MetadataRegistration para recuperar métodos IL2CPP.
4. Investigar serialização, autenticação e protocolo reais antes de avaliar servidor local.
5. Registrar documentação, hashes e checkpoints no GitHub; **não versionar conteúdo proprietário**.

## Retomada
**Último passo aprovado: 900.** O script do **PASSO 901**, meta 1 MiB (1.048.576 bytes), monitoramento híbrido com janela final 8192, já foi entregue, **mas NÃO foi executado**. Antes de solicitar saída do 901, conferir atualização de tabela histórica, painel web, README e backup no GitHub. Recebida a saída do 901, validar hash de 128/256/512 KiB e registrar novo hash 1 MiB; não presumir antecipadamente que a meta foi atingida.
