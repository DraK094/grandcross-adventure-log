# ⚔️ Grand Cross Local — Adventure Log

Diário público de investigação técnica do cliente PC de **Seven Deadly Sins: Grand Cross**. Projeto independente, não afiliado à Netmarble.

## Estado registrado
- Último passo concluído: **601** (checkpoint 600 validado)
- Próximo passo planejado: **602** (inspeção estática dos primeiros bytes da seção `.boot`)
- Próximo relatório formal: **700** (checkpoint 600 concluído e auditado)
- **70/70** cabeçalhos UnityFS internos validados na amostra
- **734** membros `TableType` decodificados
- **1165** IDs C2S e **624** IDs S2C catalogados
- **Nenhum servidor local compatível e funcional** validado

## Painel
O site está no arquivo [index.html](./index.html), feito com HTML, CSS e JavaScript, sem dependências. Pode ser aberto localmente no navegador. Para disponibilizar uma URL pública é necessário configurar hospedagem, por exemplo GitHub Pages.

## Atualizações
Registramos descobertas após validação, resumindo os marcos relevantes em vez de inventar uma transcrição de todos os passos. A integração autorizada permite atualizar o GitHub; a execução de PowerShell no PC não sincroniza automaticamente sem um mecanismo adicional.

## Segurança e direitos
Não publicar binários do jogo, assets proprietários, chaves, credenciais ou dados privados. Este repositório contém somente documentação técnica e um painel independente.

## Progresso e estimativas
- **Checkpoint 600: 100% concluído e validado** (marco de investigação, não percentual do servidor).
- **601 passos concluídos; passo 602 preparado, ainda não executado.**
- **Progresso total rumo a um servidor offline:** não quantificável com rigor; nenhum backend local compatível foi implementado ou validado.
- Análise estática avançada; dinâmica de inicialização e dependências de backend ainda não demonstradas.

## Marcos técnicos — passos 585–601
- `GameAssembly.dll`: 47.199.760 bytes, PE32+ x64, 14 seções, base preferida `0x180000000`, SHA-256 `FAB18D112F6414090C4CF36C25908FAE1056C87D56E6AC432C053B52E2933DDD`.
- Exportações: 384 funções nomeadas, 239 com prefixo `il2cpp_`; alguns RVAs exportados caem fora da área física correspondente à seção.
- `.vdata`: RVA `0x06A83000`, tamanho virtual 14.131.200 bytes, `RawSize=0`, flags **RWX** (`0xE0000060`).
- `.boot`: RVA `0x077FD000`, tamanho físico/virtual 8.060.416 bytes, flags **RX** (`0x60000060`); inicia imediatamente após `.vdata`.
- EntryPoint `0x077FD058` começa com `CALL rel32` para rotina em `0x077FD1DF`; fluxo examinado calcula alvo `0x06A9FC32` dentro de `.vdata`, sem bytes físicos associados. Conteúdo em tempo de execução **não determinado**.
- Diretório de exceções aponta para `.vdata` (`0x07127024`, 3.706.272 bytes declarados), sem conteúdo físico nessa seção.
- Importações declaradas: 10 DLLs / 10 funções; uma delas `Baselib_DynamicLibrary_GetFunction`; presença não prova como `.vdata` é inicializada.
- TLS: 40 bytes; `AddressOfCallbacks=0`, sem lista de callbacks declarada.
- Relocations: 16 bytes; três entradas `DIR64` nos campos TLS e uma `ABSOLUTE` de preenchimento.
- `DllCharacteristics=0x0060`: ASLR e HIGH_ENTROPY_VA declarados; NX_COMPAT não declarado.
- **Checkpoint 600:** 18/19 verificações inicialmente aprovadas; a divergência foi um erro nas máscaras de permissão dos scripts, corrigido e confirmado no passo 601. `.vdata` RWX, `.boot` RX, contiguidade e ausência de dados físicos `.vdata` verificadas.

## Próxima investigação
**PASSO 602:** examinar os 88 bytes anteriores ao EntryPoint de `.boot`, e comparar os primeiros 96 bytes do EntryPoint e da rotina chamada. Apenas análise estática; não há evidência de um servidor offline funcional.
