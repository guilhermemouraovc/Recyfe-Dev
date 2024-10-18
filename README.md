# Recyfe-Dev

## Descrição

Recyfe é um aplicativo desenvolvido com o objetivo de incentivar a reciclagem e o consumo consciente através de práticas sustentáveis. O sistema permite que os usuários acumulem créditos por suas ações sustentáveis, que podem ser trocados por recompensas. Além disso, oferece uma plataforma de compra de produtos feitos a partir de materiais reciclados e facilita a doação e a reciclagem de itens têxteis.

Este projeto foi criado como parte da disciplina de Projetos 2 na CESAR School - turma 2024.2.
 
## Funcionalidades / Historias

1. **Visualização do Feed**

>Como usuário, quero acessar uma página inicial clara e visualmente atraente, onde posso visualizar posts de outros usuários.

2. **Postagem de Práticas Sustentáveis**

>Como usuário, quero postar minhas próprias práticas sobre sustentabilidade na página inicial.

3. **Navegação de Produtos**

>Como usuário, quero poder visualizar detalhes completos dos produtos. Desejo ver a imagem do produto, sua descrição e o tipo de material reutilizado.

4. **Localização de Pontos de Doação e Vendas**

>Como administrador, quero disponibilizar no aplicativo, por meio de GPS, a localização dos pontos de doação e das lojas que vendem produtos reutilizados.

5. **Sistema de Pontuação e Recompensas**

>Como usuário, quero acessar uma aba de recompensas, onde posso visualizar os créditos acumulados por minhas ações sustentáveis e escolher diferentes tipos de recompensas.

6. **Catalogação de Créditos e Opções de Envio**

>Como usuário, desejo acessar uma seção onde posso ver informações sobre opções de envio de residuos texteis para reuso e catalogação de créditos por resíduo enviado.

## Tecnologias

- **Framework de Desenvolvimento**: Django - Framework web em Python para o back-end.
- **Interface**: HTML/CSS/JavaScript - Para a interface do usuário.
- **Banco de dados**: Sqlite/PostgreSQL - Para armazenar informações.
- **Hospedagem**: Azure - O produto final será hospedado na plataforma Azure.

## Ferramentas

- **Prototipação**: Figma - Utilizado para criar e validar protótipos de design da interface do usuário.
- **Gestão de Projetos**: Jira - Ferramenta para o planejamento e acompanhamento das tarefas do projeto.
- **Comunicação e Reuniões**: Discord/WhatsApp - Plataformas utilizadas para reuniões e comunicação da equipe.

## Licença

Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

## Equipe

- [Guilherme Mourão](https://github.com/guilhermemouraovc) - gmvc@cesar.school
- [Henrique Figueiredo](https://github.com/fthenri) - hft@cesar.school
- [Jeronimo Rossi](https://github.com/Jeraross) - jbr2@cesar.school
- [Luis Guilherme](https://github.com/luisgxlauria) - lgals@cesar.school
- [Joao Lucas](https://github.com/JRobalinho) - jlvrf@cesar.school
- [Caio Ferreira](https://github.com/CaioLira18) - cflo@cesar.school



<details>
<summary><h2>Links</h2></summary>

- [Site - Azure](https://recyfe.azurewebsites.net/)

- [Figma - Prototipo Lo-fi](https://www.figma.com/design/41Ibz8AEwuqGG0PivkYSAL/Prot%C3%B3tipo-baixa-fidelidade?node-id=0-1&node-type=canvas)

</details>


<details>
<summary><h2>SR1</h2></summary>

- [Screecast do Protótipo Lo-fi](https://www.youtube.com/watch?v=FWHbXnmOCmE)

- [Screecast do Site](https://youtu.be/bEzvsAhCzDU)

- [Site - Azure](https://recyfe.azurewebsites.net/)

- [Analise_de_Viabilidade_Programacao_em_Par_Projeto_Django.pdf](https://github.com/user-attachments/files/17388785/Analise_de_Viabilidade_Programacao_em_Par_Projeto_Django.pdf)

- **Print Product Backlog**

![Captura de tela 2024-10-16 001422](https://github.com/user-attachments/assets/85b3fbb5-fec5-48c2-86d3-9d452925157d)

- **Print Issues/Bug Tracker**

![Captura de tela 2024-10-16 001519](https://github.com/user-attachments/assets/1bce1d27-25c7-48f8-ab5f-7672a40192b8)

- **Print Diagrama de Atividades do Projeto**

![image](https://github.com/user-attachments/assets/b5ff5f6b-c16d-4836-bc7e-2cefa89e0790)

- **6 Historias de Usuário Bem Definidas / 2 Historias Implementadas**

1. **Visualização do Feed** - **Implementada**

História: Como usuário, quero acessar uma página inicial clara e visualmente atraente, onde posso visualizar posts de outros usuários.

Cenários de Validação:

Cenário 1: Acesso e uso da página inicial com sucesso

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar a página inicial,
Então eu devo ser capaz de ver uma interface clara e atraente,
E eu devo poder postar minhas próprias práticas,
E visualizar dicas sobre reutilização de resíduos têxteis.

Cenário 2: Tentativa de login sem credenciais corretas

Dado que eu não tenha inserido minhas credenciais corretamente,
Quando eu tentar fazer login no sistema,
Então uma mensagem de erro "Credenciais inválidas" deve aparecer,
E o acesso ao sistema deve ser negado.

Cenário 3: Acesso ao Feed com sucesso

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar o Feed,
Então eu devo ser capaz de visualizar posts de outros usuários,
E receber informações sobre sustentabilidade dos administradores.

Cenário 4: Falha ao acessar o Feed

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E houver uma falha no carregamento do Feed,
Então uma mensagem de erro "Erro ao carregar o Feed, tente novamente mais tarde" deve aparecer.

Cenário 5: Tentativa de postar sem estar logado

Dado que eu não esteja logado no sistema,
Quando eu tentar postar uma prática sustentável,
Então uma mensagem "Você precisa estar logado para postar" deve aparecer.

2. **Postagem de Práticas Sustentáveis** - **Implementada**

História: Como usuário, quero postar minhas próprias práticas sobre sustentabilidade na página inicial.

Cenários de Validação:

Cenário 1: Postagem de prática sustentável com sucesso

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E tentar postar uma prática sustentável,
Então o post deve ser criado com sucesso e aparecer no Feed.

Cenário 2: Tentativa de postar sem estar logado

Dado que eu não esteja logado no sistema,
Quando eu tentar postar uma prática sustentável,
Então uma mensagem "Você precisa estar logado para postar" deve aparecer.

3. **Navegação de Produtos**

História: Como usuário, quero poder visualizar detalhes completos dos produtos. Desejo ver a imagem do produto, sua descrição e o tipo de material reutilizado.

Cenários de Validação:

Cenário 1: Visualização dos detalhes do produto com sucesso

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar a página de um produto,
Então eu devo ser capaz de ver uma imagem clara do produto,
E eu devo poder visualizar a descrição completa,
E o tipo de material reutilizado no produto.

Cenário 2: Tentativa de login sem credenciais corretas

Dado que eu não tenha inserido minhas credenciais corretamente,
Quando eu tentar fazer login no sistema,
Então uma mensagem de erro "Credenciais inválidas" deve aparecer,
E o acesso ao sistema deve ser negado.

Cenário 3: Falha ao carregar a página de detalhes do produto

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E houver uma falha ao carregar os detalhes do produto,
Então uma mensagem de erro "Erro ao carregar os detalhes do produto, tente novamente mais tarde" deve aparecer.

Cenário 4: Tentativa de visualizar detalhes sem estar logado

Dado que eu não esteja logado no sistema,
Quando eu tentar acessar a página de detalhes de um produto,
Então uma mensagem "Você precisa estar logado para visualizar os detalhes do produto" deve aparecer.

4. **Localização de Pontos de Doação e Vendas**

História: Como administrador, quero disponibilizar no aplicativo, por meio de GPS, a localização dos pontos de doação e das lojas que vendem produtos reutilizados.

Cenários de Validação:

Cenário 1: Cadastramento de novos pontos de doação ou lojas com sucesso

Dado que eu tenha um perfil de administrador,
Quando eu fizer login no sistema,
E acessar a função de cadastramento de novos pontos de doação ou lojas,
E inserir as informações requeridas,
Então o novo ponto de doação ou loja deve ser cadastrado com sucesso,
E as informações devem aparecer no mapa disponível para os usuários.

Cenário 2: Tentativa de cadastrar novos pontos de doação sem permissão

Dado que eu tenha um perfil de usuário sem permissões de administrador,
Quando eu tentar acessar a função de cadastramento de novos pontos de doação ou lojas,
Então uma mensagem de "Permissão negada" deve aparecer,
E o sistema deve impedir o cadastramento.

Cenário 3: Visualização de locais no mapa com sucesso

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar a função de mapa,
Então eu devo ser capaz de visualizar as localizações dos pontos de doação e lojas próximos a mim,
Baseado na minha localização GPS.

Cenário 4: Visualização de informações detalhadas sobre um local

Dado que eu esteja visualizando o mapa,
Quando eu selecionar um ponto de doação ou loja,
Então as informações detalhadas (como horário de funcionamento e serviços oferecidos) devem ser exibidas para mim.

Cenário 5: Falha ao visualizar o mapa por problemas de GPS

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar a função de mapa,
E houver problemas com o GPS ou sinal de localização,
Então uma mensagem "Falha ao carregar a localização, verifique suas configurações de GPS" deve aparecer.

Cenário 6: Tentativa de visualizar mapa sem permissão

Dado que eu não esteja logado no sistema,
Quando eu tentar acessar a função de mapa,
Então uma mensagem "Você precisa estar logado para visualizar o mapa de pontos de doação e lojas" deve aparecer.

5. **Sistema de Pontuação e Recompensas**

História: Como usuário, quero acessar uma aba de recompensas, onde posso visualizar os créditos acumulados por minhas ações sustentáveis e escolher diferentes tipos de recompensas.

Cenários de Validação:

Cenário 1: Visualização de créditos acumulados com sucesso

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar a aba de recompensas,
Então eu devo ser capaz de visualizar meu saldo de créditos acumulados,
E ver as opções de recompensas disponíveis na plataforma.

Cenário 2: Tentativa de visualizar recompensas sem estar logado

Dado que eu não esteja logado no sistema,
Quando eu tentar acessar a aba de recompensas,
Então uma mensagem "Você precisa estar logado para acessar suas recompensas" deve aparecer.

Cenário 3: Troca de créditos por recompensas com sucesso

Dado que eu tenha créditos suficientes,
Quando eu acessar a aba de recompensas,
E escolher uma recompensa,
Então eu devo ser capaz de trocar meus créditos pela recompensa escolhida,
E uma confirmação da troca deve aparecer.

Cenário 4: Notificação de novas recompensas

Dado que eu tenha acumulado créditos suficientes para desbloquear novas recompensas,
Quando eu acessar a aba de recompensas,
Então eu devo ser notificado de que novas recompensas estão disponíveis para troca.

Cenário 5: Tentativa de trocar créditos insuficientes

Dado que eu tenha um perfil de usuário registrado,
Quando eu acessar a aba de recompensas,
E tentar trocar créditos por uma recompensa sem ter créditos suficientes,
Então uma mensagem "Créditos insuficientes para esta recompensa" deve aparecer.

6. **Catalogação de Créditos e Opções de Envio**

História: Como usuário, desejo acessar uma seção onde posso ver informações sobre opções de envio de residuos texteis para reuso e catalogação de créditos por resíduo enviado.

Cenários de Validação:

Cenário 1: Acesso à seção de reciclagem com sucesso

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar a seção de doação ou reciclagem,
Então eu devo ser capaz de visualizar as opções de envio ou entrega para reuso de itens têxteis.

Cenário 2: Tentativa de acessar a seção de reciclagem sem estar logado

Dado que eu não esteja logado no sistema,
Quando eu tentar acessar a seção de doação ou reciclagem,
Então uma mensagem "Você precisa estar logado para acessar essa seção" deve aparecer,
E o sistema deve bloquear o acesso.

Cenário 3: Acompanhamento de créditos recebidos com sucesso

Dado que eu tenha enviado itens para reciclagem,
Quando eu acessar meu perfil ou a seção de reciclagem,
Então eu devo poder visualizar o histórico de itens enviados,
E ver os créditos recebidos por cada item reciclado.

Cenário 4: Notificação de créditos insuficientes para acompanhamento

Dado que eu tenha enviado itens para reciclagem,
Quando eu acessar meu saldo de créditos,
E não houver crédito suficiente catalogado,
Então uma mensagem "Nenhum crédito disponível para os itens reciclados" deve aparecer.
</details>
