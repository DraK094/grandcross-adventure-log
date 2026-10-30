# PASSOS 1028–1030 — Trampolim e ciclo atômico na versão atual

**Aprovados em análise estática direta de bytes em 30/10/2026.** Próximo PASSO 1031 ainda não executado. Objetivo 2 (inicialização completa) EM ANDAMENTO.

- DLL atual: SHA-256 `01761332ea33c2ff2c88b3fea8da924cd8482d7dfa86b5b02c1c1cb6f1660624`.
- .vdata reconstruída com 14.131.200 bytes, SHA-256 `72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231`.

## PASSO 1028
Desmontagem linear do bloco iniciado em `.vdata+0x2E5CAF` encontrou `JMP rel32` em `.vdata+0x2E5E12` (VA `0x186DC7E12`), bytes `E9 1A BC 02 00`, que apontam ao VA `0x186DF3A31`, isto é, `.vdata+0x311A31`, RVA `0x6DF3A31`. Antes do salto há operações complicadas de RSP; só o destino codificado foi demonstrado.

## PASSO 1029
Na nova entrada `.vdata+0x311A31`, bytes `E8 00 00 00 00` = `CALL` à instrução seguinte `0x186DF3A36`. O endereço seria empilhado caso a trajetória fosse executada com pilha válida. Não houve validação dinâmica de estados.

## PASSO 1030
Padrão de laço atômico confirmado:
```asm
0x6DF3D5C XOR EAX,EAX
0x6DF3D5E LOCK CMPXCHG DWORD PTR [RBX+RBP],ECX
0x6DF3D63 JE 0x6DF3D70
0x6DF3D69 PAUSE
0x6DF3D6B JMP 0x6DF3D5C
0x6DF3D70 PUSH QWORD PTR [RSP]
```
É uma estrutura semelhante ao antigo PASSO 967, mas a execução real depende de estado não observado. **Não comprova handoff ao runtime IL2CPP**.

Objetivo 1 reconstrução da seção atual: concluído. Objetivo 2 inicialização: EM ANDAMENTO. Próximo PASSO 1031 examinar ramos após `0x6DF3D70`. Não publicar DLL nem saída proprietária.