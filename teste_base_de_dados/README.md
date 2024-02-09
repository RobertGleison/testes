# Considerações sobre o teste de base de dados:

Link to arquivo: https://drive.google.com/drive/folders/1p9uJ5GG4nZtfvL_zC3nDc-sjiG3JZWes?usp=sharing

1. **Colunas Extras em CSVs de 2023:**
    - É possível que a resposta da query analítica esteja errada, pois em alguns CSVs de 2023, havia 2 colunas extras com alguns números sem explicação, nem nome da coluna ou descrição no dicionário da página. Logo, considerei apagá-las, pois pareciam rascunhos, mas poderia ser algo importante. Reforço que o CSV do útlimo trimestre de 2023 não estava disponível ainda.

2. **Sobre Índices:**
    - No que tange aos índices, são uma boa prática para agilizar buscas em base de dados, mas podem atrapalhar quando em uma tabela em constante modificação devido ao processamento extra. Como estava trabalhando com tabelas de pesquisa, poderia ter criado alguns índices, e estes ficariam visíveis na estrutura de criação .sql das tabelas. No entanto, os índices criados automaticamente pelo MySQL foram o suficiente, não havia necessidade de criar outros. Mas saibam que levei isso em conta.

3. **Desformatação do CSV 2T2022:**
    - O CSV do segundo trimestre de 2022 estava desformatado, e alguns símbolos não foram renderizados, mas acredito que funcionou do mesmo jeito.

