# GrandCross Local — PASSOS 1207–1212

Resultado central: corrigido um falso caminho de busca por ponteiros. O diretório PE de exceções é armazenado na secao .vdata, mas indexa funcoes da imagem inteira. Tem 310763 entradas, com 310762 começando antes da .vdata e 1 começando dentro dela (RVA inicial 0x6ae2000, RVA final 0x6e33f4c).

O diretorio ocupa o intervalo RVA 0x718602c a 0x7514730. Entre os primeiros registros de funcao estao inicios 0x1010, 0x1230, 0x1260 e 0x1300.

Analise quantitativa da secao reconstruida (SHA256 72147fdd436f457250e117be65c722aaa1f52f48d3887092fb8e994934f09231): janelas de 1 MiB tiveram perfis diferentes de entropia; tres janelas iniciadas em RVA 0x71e2000, 0x72e2000 e 0x73e2000 continham 100% de DWORDs alinhados cujo valor era numericamente compativel com RVA da imagem. Isso e compativel com faixa coberta por tabela de excecoes, NAO prova CodeRegistration.

Proxima pesquisa: excluir faixa de excecoes nas sondagens, separar RVA de 32 bits de VA 64 bits e validar estruturas por referencias cruzadas. CodeRegistration, CodeGenModule, RVAs de marshalers, IDs RMI e formato de rede NAO encontrados. Ultimo passo 1212, proximo 1213.