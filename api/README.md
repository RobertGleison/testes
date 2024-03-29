## Observações

Atualmente, minha stack principal é Java com Spring, ainda não sou tão proficiente com JavaScript, embora já tenha usado e pretendo estudar este semestre. Portanto, optei por desenvolver esta interface web sem Vue e sem Single Page Application. 

## Dependências

Deve ter Python instalado, o package manager pip e o Flask:
```
sudo apt-get install python3 python3-pip
pip install Flask
``` 
Para rodar a aplicação, use o comando abaixo e conecte no localhost:9001:
```
python3 app.py
``` 

## Sobre Performance

Em relação à performance, se eu estivesse lidando com uma conexão com banco de dados, provavelmente optaria por implementar um sistema de caching em memória ou Redis (embora para uma tabela de 1000 linhas não mude muita coisa). No entanto, como estou trabalhando com leitura de um arquivo CSV, acredito que isso não seja necessário.

## Meu GitHub

Convido vocês a darem uma olhada no meu humilde GitHub, onde mantenho alguns estudos com APIs em Java. Em especial, destaco o repositório [rinha-backend-v1](https://github.com/RobertGleison/rinha-backend-v1), que foi um desafio que surgiu no Twitter. Através desse projeto, venho aprendendo bastante ao analisar o código de outros desenvolvedores. Tenho alguns outros projetos de API's onde utilizei Swagger como documentação, validação, uso de ORM para geração de tabelas e algumas coisas mais.
